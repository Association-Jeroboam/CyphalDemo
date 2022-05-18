#!/bin/bash
export UAVCAN__CAN__IFACE='socketcan:can0'
export UAVCAN__CAN__MTU=8
export UAVCAN__CAN__BITRATE=500000
export UAVCAN__NODE__ID=42

#yakut pub -T 1 uavcan.node.Heartbeat.1.0 '305419896'
#yakut pub -T 0.01 1:reg.udral.physics.kinematics.cartesian.Pose.0.1 '[[1,2,3],[1,2,3,4]]'
#yakut pub -T 0.1 2:reg.udral.physics.kinematics.cartesian.Twist.0.1 '[[1,0,0],[0,0,2]]'
#yakut pub -T 0.05 11:jeroboam_datatypes.actuators.servo.ServoAngle.0.1 '!$ "[n%16,3.0]"'
#yakut pub -T 0.1 12:jeroboam_datatypes.actuators.servo.ServoConfig.0.1 '!$ "[n%16,25, 30, [[1,2,3], 4]]"'
#yakut pub -T 0.1 16:jeroboam_datatypes.actuators.pneumatics.PumpStatus.0.1 '!$ "[n%2,0]"'
#yakut pub -T 1 18:jeroboam_datatypes.actuators.pneumatics.ValveStatus.0.1 '!$ "[n%2,1]"'
#yakut pub -T 1 6:jeroboam_datatypes.actuators.motion.AdaptativePIDConfig.0.1 '!$ "[ [[[0.1,0.1,0], 0],[[0.1,0.1,0],0],[[0.1,0.1,0], 0]],[50, 200, 400],n%2]"'
yakut pub -T 1 7:jeroboam_datatypes.actuators.motion.MotionConfig.0.1 '!$ "[0.2, 0.002825, 0.002825, 400, 6.28,400, 6.28]"'


