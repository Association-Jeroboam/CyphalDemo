# Distributed under CC0 1.0 Universal (CC0 1.0) Public Domain Dedication.
"""
This application simulates the plant controlled by the thermostat node: it takes a voltage command,
runs a crude thermodynamics simulation, and publishes the temperature (i.e., one subscription, one publication).
"""
import os
import sys
import pathlib
import time
import asyncio

compiled_dsdl_dir = pathlib.Path(__file__).resolve().parent / ".dsdl_compiled"

# Make the compilation outputs importable. Let your IDE index this directory as sources to enable code completion.
sys.path.insert(0, str(compiled_dsdl_dir))

import uavcan.si.unit.voltage
import uavcan.si.sample.temperature
import uavcan.time
import pycyphal
from pycyphal.application.heartbeat_publisher import Health
from pycyphal.application import make_node, NodeInfo, register
import reg.udral.physics.kinematics.cartesian


UPDATE_PERIOD = 0.5

heater_voltage = 0.0
saturation = False


async def twist_goal_receive(msg: reg.udral.physics.kinematics.cartesian.Twist_0_1, _metadata: pycyphal.transport.TransferFrom) -> None:
    print(f'linear {msg.linear}')
    print(f'angular {msg.angular}')


async def main() -> None:
    with make_node(NodeInfo(name="org.jeroboam.state_publisher"), "StatePublisher.db") as node:

        # Initialize values from the registry. The temperature is in kelvin because in UAVCAN everything follows SI.
        # Here, we specify the type explicitly as "real32[1]". If we pass a native float, it would be "real64[1]".
        temp_environment = float(node.registry.setdefault("model.environment.temperature", register.Real32([292.15])))
        temp_plant = temp_environment
        node.heartbeat_publisher.mode = uavcan.node.Mode_1.OPERATIONAL  # type: ignore
        node.heartbeat_publisher.health = uavcan.node.Health_1_0.NOMINAL
        node.heartbeat_publisher.vendor_specific_status_code = 43
        # Set up the ports.
        pub_state = node.make_publisher(reg.udral.physics.kinematics.cartesian.State_0_1, "robot_current_state")
        pub_state.priority = pycyphal.transport.Priority.HIGH
        sub_twist = node.make_subscriber(reg.udral.physics.kinematics.cartesian.Twist_0_1, "robot_twist_goal")
        sub_twist.receive_in_background(twist_goal_receive)

        # Run the main loop forever.
        next_update_at = asyncio.get_running_loop().time()
        while True:
            # Publish new measurement and update node health.
            # pose = reg.udral.physics.kinematics.cartesian.Pose_0_1(
            #     reg.udral.physics.kinematics.cartesian.Point_0_1(
            #         uavcan.si.unit.length.WideVector3_1_0([ 1., 2., 3.])
            #     ),
            #     uavcan.si.unit.angle.Quaternion_1_0([1., 1., 1., 1.,])
            # )
            #
            # twist = reg.udral.physics.kinematics.cartesian.Pose_0_1(
            #     uavcan.si.unit.velocity.Vector3_1_0([1., 2., 3.]),
            #     uavcan.si.unit.velocity.Vector3_1_0([4., 5., 6.])
            # )
            pose = reg.udral.physics.kinematics.cartesian.Pose_0_1()
            pose.position.value = uavcan.si.unit.length.WideVector3_1_0([1., 2., 3.])
            pose.orientation.wxyz = [1., 1., 1., 1.,]

            twist = reg.udral.physics.kinematics.cartesian.Twist_0_1()
            twist.linear.meter_per_second= [1., 2., 3.]
            twist.angular.radian_per_second=[4., 5., 6.]

            await pub_state.publish(
                reg.udral.physics.kinematics.cartesian.State_0_1(
                    pose = pose, twist = twist,
                )
            )
            # Sleep until the next iteration.
            next_update_at += UPDATE_PERIOD
            await asyncio.sleep(next_update_at - asyncio.get_running_loop().time())

            # Update the simulation.


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
