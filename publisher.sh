#!/bin/bash
export UAVCAN__CAN__IFACE='socketcan:can0'
export UAVCAN__CAN__MTU=8
export UAVCAN__CAN__BITRATE=500000
export UAVCAN__NODE__ID=$(yakut accommodate)  # Pick an unoccupied node-ID automatically for this shell session.
echo "Auto-selected node-ID for this session: $UAVCAN__NODE__ID"
#yakut pub -T 1 uavcan.node.Heartbeat.1.0 '305419896'
#yakut pub -T 0.01 1:reg.udral.physics.kinematics.cartesian.Pose.0.1 '[[1,2,3],[1,2,3,4]]'
yakut pub -T 0.1 2:reg.udral.physics.kinematics.cartesian.Twist.0.1 '[[1,0,0],[0,0,2]]'

