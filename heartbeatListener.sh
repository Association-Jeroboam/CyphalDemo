#!/bin/bash
export UAVCAN__CAN__IFACE='socketcan:can0'
export UAVCAN__CAN__MTU=8
export UAVCAN__CAN__BITRATE=500000
yakut sub 7509:uavcan.node.Heartbeat.1.0
