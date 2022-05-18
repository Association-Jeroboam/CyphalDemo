#!/bin/bash
export UAVCAN__CAN__IFACE='socketcan:can0'
export UAVCAN__CAN__MTU=8
export UAVCAN__CAN__BITRATE=500000
#export UAVCAN__NODE__ID=$(yakut accommodate)  # Pick an unoccupied node-ID automatically for this shell session.
#echo "Auto-selected node-ID for this session: $UAVCAN__NODE__ID"
#yakut sub 7509:uavcan.node.Heartbeat.1.0
#yakut sub 1:reg.udral.physics.kinematics.cartesian.Pose.0.1
#yakut sub 0:reg.udral.physics.kinematics.cartesian.State.0.1
yakut sub 11:jeroboam_datatypes.actuators.servo.ServoAngle.0.1
