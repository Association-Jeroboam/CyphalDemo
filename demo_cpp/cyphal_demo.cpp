#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <thread>
#include <pthread.h>
#include <string.h>
#include <unistd.h>
#include <stdbool.h>

#include <net/if.h>
#include <sys/ioctl.h>
#include <sys/socket.h>
#include <sys/sysinfo.h>
#include <linux/can.h>
#include <linux/can/raw.h>
#include "libcanard/libcanard/canard.h"
#include "Heartbeat_1_0.h"
#include "cartesian/State_0_1.h"

constexpr int CAN_RX_MAX_SUBSCRIPTION = 32;
constexpr int MAX_FRAME_SIZE = 8;
const uint32_t CAN_EXT_ID_MASK = (1 <<29) -1;

void * canardSpecificAlloc(CanardInstance * instance, size_t amount);
void canardSpecificFree(CanardInstance * instance, void * pointer);
void rcvThread(void);
void checkTxQueue(void);
void print_usage(void);
bool check_parameter(char * iface, char * name, size_t n);
void heartbeatRoutine(void);
bool pushQueue(const CanardTransferMetadata* const metadata,
               const size_t                        payload_size,
               const void* const                   payload);
bool subscribe(CanardTransferKind transfer_kind, CanardPortID port_id, size_t extent);
int send_can_frame(struct can_frame * frame);
void initCAN(char * iface);
void initCanard(void);

pthread_mutex_t execution_lock;
pthread_mutex_t queue_lock;



static CanardInstance instance;
CanardTxQueue  queue;
int canIFace;
CanardRxSubscription subscriptions[CAN_RX_MAX_SUBSCRIPTION];
unsigned int subCnt;




void execution_thread() {
    //cheat to simulate an external process
    while(true) {
        heartbeatRoutine();
        pthread_mutex_unlock(&execution_lock);
        usleep(1000000);
    }
}

int main(int argc, char ** argv) {

    if(argc != 2) {
        print_usage();
        return 1;
    }
    char canName[] = "can";
    char vcanName[] = "vcan";
    bool hardware = check_parameter(argv[1], canName, 3);
    bool emulated = check_parameter(argv[1], vcanName, 4);


    if(!hardware && !emulated) {
        print_usage();
        return 2;
    }

    char * iface = argv[1];

    initCAN(iface);
    initCanard();
    CanardPortID portID = 0;
    subscribe(CanardTransferKindMessage, portID, reg_udral_physics_kinematics_cartesian_State_0_1_EXTENT_BYTES_);
    subscribe(CanardTransferKindMessage, uavcan_node_Heartbeat_1_0_FIXED_PORT_ID_, uavcan_node_Heartbeat_1_0_EXTENT_BYTES_);

    if (pthread_mutex_init(&execution_lock, NULL) != 0)
    {
        printf("\nexecution  mutex init failed\n");
        return 1;
    }

    if (pthread_mutex_init(&queue_lock, NULL) != 0)
    {
        printf("\nqueue mutex init failed\n");
        return 1;
    }
    pthread_mutex_lock(&execution_lock);
    std::thread thread_object(rcvThread);
    std::thread thread_execture(execution_thread);
    while (true) {
        pthread_mutex_lock(&execution_lock);
        checkTxQueue();
    }
    return 0;
}

void rcvThread(void) {
    auto lastReceiveTS = std::chrono::high_resolution_clock::now();
    while (true) {
        if(canIFace !=0) {
            struct can_frame rx_frame;
            int nbytes = read(canIFace, &rx_frame, sizeof(struct can_frame));
            auto receiveTS = std::chrono::high_resolution_clock::now();


            if (nbytes >= 0) {
                auto before = std::chrono::high_resolution_clock::now();
                const CanardMicrosecond timestamp = 0;
                CanardFrame frame = {
                        .extended_can_id = rx_frame.can_id & CAN_EXT_ID_MASK,
                        .payload_size = rx_frame.can_dlc,
                        .payload = rx_frame.data,
                };

                CanardRxTransfer transfer;
                CanardRxSubscription * sub;
                int32_t ret = canardRxAccept(&instance, timestamp, &frame, 0, &transfer, &sub);
                if(ret == 1) {
                    //success

                    // process message

                    //then
                    instance.memory_free(&instance, transfer.payload);

                    auto now = std::chrono::high_resolution_clock::now();
                    auto delta = now - before;

                    auto dt = receiveTS - lastReceiveTS;
                    lastReceiveTS = receiveTS;
                    float freq = 1./(std::chrono::duration_cast<std::chrono::microseconds>(dt).count()) * 1000000.;
                    std::cout << "exec time: " << std::chrono::duration_cast<std::chrono::microseconds>(now - before).count() << "µs\n";
                    std::cout << "dt: " << std::chrono::duration_cast<std::chrono::microseconds>(dt).count() << "µs\n";
                    std::cout << "freq: " << freq << "Hz\n";

                } else if (ret == 0) {
                    // rejected because not subscribed or transfer not complete
                }else {
                    //error
                    printf("frame error %i\n", ret);
                }
            }

        } else {
            usleep(10);
        }

    }
}

void checkTxQueue(void) {
    const CanardTxQueueItem* item = canardTxPeek(&queue);

    while(item != NULL) {
        CanardTxQueueItem* extractedItem = canardTxPop(&queue, item);
        uint32_t           size          = item->frame.payload_size;

        do {
            struct can_frame frame;
            frame.can_id = item->frame.extended_can_id | 1 << 31;

            if (size >= MAX_FRAME_SIZE) {
                frame.can_dlc = MAX_FRAME_SIZE;
                size -= MAX_FRAME_SIZE;
            } else {
                frame.can_dlc= size;
                size      = 0;
            }
            memcpy(&frame.data, item->frame.payload, frame.can_dlc);

            send_can_frame(&frame);
        } while (size > 0);

        instance.memory_free(&instance, extractedItem);
        item = canardTxPeek(&queue);
    }
}

void heartbeatRoutine(void) {
    static CanardTransferID transfer_id = 0;
    struct sysinfo info;
    sysinfo(&info);

    uint32_t now = info.uptime;
    const uavcan_node_Heartbeat_1_0 heartbeat = {
            .uptime = now,
            .health = {
                    .value = uavcan_node_Health_1_0_NOMINAL
            },
            .mode = {
                    .value = uavcan_node_Mode_1_0_OPERATIONAL,
            },
            .vendor_specific_status_code = 42,
    };

    size_t buf_size = uavcan_node_Heartbeat_1_0_SERIALIZATION_BUFFER_SIZE_BYTES_;
    uint8_t buffer[uavcan_node_Heartbeat_1_0_SERIALIZATION_BUFFER_SIZE_BYTES_];

    uavcan_node_Heartbeat_1_0_serialize_(&heartbeat, buffer, &buf_size);


    const CanardTransferMetadata metadata = {
            .priority = CanardPriorityNominal,
            .transfer_kind = CanardTransferKindMessage,
            .port_id = uavcan_node_Heartbeat_1_0_FIXED_PORT_ID_,
            .remote_node_id = CANARD_NODE_ID_UNSET,
            .transfer_id = transfer_id,
    };
    transfer_id++;
    bool success = pushQueue(&metadata, buf_size, buffer);
    if (!success ) {
        printf("Queue push failed\n");
    }
}

int send_can_frame(struct can_frame * frame) {
    if (write(canIFace, frame, sizeof(struct can_frame)) != sizeof(struct can_frame)) {
        perror("Write ERROR");
        return 1;
    }
    return 0;
}

bool pushQueue(const CanardTransferMetadata* const metadata,
               const size_t                        payload_size,
               const void* const                   payload) {
    bool success;
    pthread_mutex_lock(&queue_lock);
    int32_t res = canardTxPush(&queue, &instance, 0, metadata, payload_size, payload);
    pthread_mutex_unlock(&queue_lock);
    success = (0 <= res);
    return success;
}

bool subscribe(CanardTransferKind transfer_kind, CanardPortID port_id, size_t extent){

    if(subCnt >= CAN_RX_MAX_SUBSCRIPTION) return false;

    int32_t subRet = canardRxSubscribe(&instance,
                                       transfer_kind,
                                       port_id,
                                       extent,
                                       CANARD_DEFAULT_TRANSFER_ID_TIMEOUT_USEC,
                                       &subscriptions[subCnt]);
    if(subRet == 1) {
    // subscription created

    } else if(subRet == 0) {
    // Subscription already existing
    //TODO
    }

    bool res = subRet >= 0;
    if(res) {
        subCnt++;
    }
    return res;
}

void initCAN(char * iface) {
    struct sockaddr_can addr;
    struct ifreq ifr;


    if ((canIFace = socket(PF_CAN, SOCK_RAW, CAN_RAW)) < 0) {
        perror("Socket");
        return;
    }

    strcpy(ifr.ifr_name, iface );
    ioctl(canIFace, SIOCGIFINDEX, &ifr);

    memset(&addr, 0, sizeof(addr));
    addr.can_family = AF_CAN;
    addr.can_ifindex = ifr.ifr_ifindex;

    if (bind(canIFace, (struct sockaddr *)&addr, sizeof(addr)) < 0) {
        perror("Bind");
        return;
    }
}

void initCanard(void) {
    instance = canardInit(canardSpecificAlloc, canardSpecificFree);
    instance.node_id = 42;
    queue = canardTxInit(100, MAX_FRAME_SIZE);
}

void * canardSpecificAlloc(CanardInstance * instance, size_t amount) {
    (void) instance;
    return malloc(amount);
}

void canardSpecificFree(CanardInstance * instance, void * pointer) {
    (void)instance;
    free(pointer);
}

void print_usage(void) {
    printf("usage:\n\tchyphal_demo can_interface (can0, vcan0...)\n");
}

bool check_parameter(char * iface, char * name, size_t n) {
    return memcmp(iface, name, n) == 0;
}