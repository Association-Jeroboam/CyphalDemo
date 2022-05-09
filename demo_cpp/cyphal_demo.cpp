#include <cstdio>
#include <cstdlib>
#include <thread>
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

constexpr int CAN_RX_MAX_SUBSCRIPTION = 32;
constexpr int MAX_FRAME_SIZE = 8;
const uint32_t CAN_EXT_ID_MASK = (1 <<29) -1;

void * canardSpecificAlloc(CanardInstance * instance, size_t amount);
void canardSpecificFree(CanardInstance * instance, void * pointer);
void rcvThread(void);
void print_usage(void);
bool check_parameter(char * iface, char * name, size_t n);

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
    usleep(250000);
    while(true) {
        pthread_mutex_unlock(&execution_lock);
        usleep(500000);
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
        printf("main value 2\n");
    }
    return 0;
}

void rcvThread(void) {
    while (true) {
        if(canIFace !=0) {
            struct can_frame rx_frame;
            printf("check msg\n");
            int nbytes = read(canIFace, &rx_frame, sizeof(struct can_frame));
            printf("check end\n");

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
        } else {
            usleep(10);
        }

    }
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