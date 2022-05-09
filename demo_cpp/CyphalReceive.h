#ifndef __CYPHALRECEIVE_H__
#define __CYPHALRECEIVE_H__
#include "canard.h"

constexpr int CAN_RX_MAX_SUBSCRIPTION = 32;

class CyphalReceive{
public:
    CyphalReceive(CanardInstance* instance);
    void run();

    inline void setCanIFace(int iface) {m_canIFace = iface;};

private:
    CanardInstance * m_instance;
    int m_canIFace;
    CanardRxSubscription m_subscriptions[CAN_RX_MAX_SUBSCRIPTION];
    unsigned int m_subCnt;
};


#endif //__CYPHALRECEIVE_H__
