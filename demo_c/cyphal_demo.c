#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdbool.h>

#include <net/if.h>
#include <sys/ioctl.h>
#include <sys/socket.h>
#include <sys/sysinfo.h>

#include <linux/can.h>
#include <linux/can/raw.h>

#include "canard.h"
#include "Heartbeat_1_0.h"


#define SLEEP_TIME_US  500000
#define MAX_FRAME_SIZE 8
#define CAN_RX_MAX_SUBSCRIPTION 20

#define CAN_EXT_ID_MASK ((UINT32_C(1) << 29U) - 1U)

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

CanardInstance instance;
CanardTxQueue  queue;
CanardRxSubscription subscriptions[CAN_RX_MAX_SUBSCRIPTION];
int sub_cnt = 0;
int s;

int send_can_frame(struct can_frame * frame) {
    if (write(s, frame, sizeof(struct can_frame)) != sizeof(struct can_frame)) {
        perror("Write ERROR");
        return 1;
    }
    return 0;
}


bool push_heartbeat( void ) {
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
    bool success;
    int32_t res = canardTxPush(&queue, &instance, 0, &metadata, buf_size, buffer);
    success = (0 <= res);

    return success;
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

bool subscribe(CanardTransferKind transfer_kind,
               CanardPortID port_id,
               size_t extent){

    if(sub_cnt >= CAN_RX_MAX_SUBSCRIPTION) return false;
    int32_t subRet = canardRxSubscribe(&instance,
                                       transfer_kind,
                                       port_id,
                                       extent,
                                       CANARD_DEFAULT_TRANSFER_ID_TIMEOUT_USEC,
                                       &subscriptions[sub_cnt]);
    if(subRet == 1) {
        // subscription created

    } else if(subRet == 0) {
        // Subscription already existing
        //TODO
    } else {
        return false;
    }
    sub_cnt++;
    return true;
}

void checkRxMsg(void) {
    struct can_frame rx_frame;
//    printf("check msg\n");
    int nbytes = read(s, &rx_frame, sizeof(struct can_frame));
//    printf("check end\n");

    if (nbytes >= 0) {
        const CanardMicrosecond timestamp = 0;
        CanardFrame frame = {
                .extended_can_id = rx_frame.can_id & CAN_EXT_ID_MASK,
                .payload_size = rx_frame.can_dlc,
                .payload = rx_frame.data,
        };
        printf("id %X\n", rx_frame.can_id);
        printf("dlc %X\n", rx_frame.can_dlc);
        for (int i = 0; i < rx_frame.can_dlc; ++i) {
            printf("%X ", rx_frame.data[i]);
        }
        printf("\n");

        CanardRxTransfer transfer;
        CanardRxSubscription * sub;
        int32_t ret = canardRxAccept(&instance, timestamp, &frame, 0, &transfer, &sub);
        if(ret == 1) {
            //success
            printf("MSG rcvd\n");
            instance.memory_free(&instance, transfer.payload);

        } else if (ret == 0) {
            // rejected or transfer not completed
        }else {
            //error
            printf("frame error %i\n", ret);
        }
    }
}

int main(int argc, char **argv)
{

    if(argc != 2) {
        print_usage();
        return 1;
    }

    bool hardware = check_parameter(argv[1], "can", 3);
    bool virtual = check_parameter(argv[1], "vcan", 4);


    if(!hardware && !virtual) {
        print_usage();
        return 2;
    }

    char * iface = argv[1];
// can init

    struct sockaddr_can addr;
    struct ifreq ifr;


    if ((s = socket(PF_CAN, SOCK_RAW, CAN_RAW)) < 0) {
        perror("Socket");
        return 1;
    }

    strcpy(ifr.ifr_name, iface );
    ioctl(s, SIOCGIFINDEX, &ifr);

    memset(&addr, 0, sizeof(addr));
    addr.can_family = AF_CAN;
    addr.can_ifindex = ifr.ifr_ifindex;

    if (bind(s, (struct sockaddr *)&addr, sizeof(addr)) < 0) {
        perror("Bind");
        return 1;
    }
// canard init
    instance = canardInit(canardSpecificAlloc, canardSpecificFree);
    instance.node_id = 42;
    queue = canardTxInit(100, MAX_FRAME_SIZE);

    subscribe(CanardTransferKindMessage, uavcan_node_Heartbeat_1_0_FIXED_PORT_ID_, uavcan_node_Heartbeat_1_0_EXTENT_BYTES_);
    // loop

    while (true) {
        printf("loop\n");
        push_heartbeat();
        checkTxQueue();
        checkRxMsg();

        usleep(SLEEP_TIME_US);
    }

    if (close(s) < 0) {
        perror("Close");
        return 1;
    }

    return 0;
}