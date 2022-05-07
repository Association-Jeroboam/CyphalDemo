#!/usr/bin/env python3
# Distributed under CC0 1.0 Universal (CC0 1.0) Public Domain Dedication.
# pylint: disable=ungrouped-imports,wrong-import-position

import os
import sys
import pathlib
import asyncio
import logging
import importlib
import pycyphal
import time

# Production applications are recommended to compile their DSDL namespaces as part of the build process. The enclosed
# file "setup.py" provides an example of how to do that. The output path we specify here shall match that of "setup.py".
# Here we compile DSDL just-in-time to demonstrate an alternative.
compiled_dsdl_dir = pathlib.Path(__file__).resolve().parent / ".dsdl_compiled"

# Make the compilation outputs importable. Let your IDE index this directory as sources to enable code completion.
sys.path.insert(0, str(compiled_dsdl_dir))

try:
#     import sirius_cyber_corp  # This is our vendor-specific root namespace. Custom data types.
    import pycyphal.application  # This module requires the root namespace "uavcan" to be transcompiled.
    import jeroboam.actuators.motion
    import reg.udral.physics.kinematics.cartesian
except (ImportError, AttributeError):  # Redistributable applications typically don't need this section.
    logging.warning("Transcompiling DSDL, this may take a while")
    src_dir = pathlib.Path(__file__).resolve().parent
    pycyphal.dsdl.compile_all(
        [
            src_dir / "public_regulated_data_types/uavcan/",
            src_dir / "public_regulated_data_types/reg/",
            src_dir / "jeroboam",
        ],
        output_directory=compiled_dsdl_dir,
    )
    importlib.invalidate_caches()  # Python runtime requires this.
    import pycyphal.application
    import jeroboam.actuators.motion
    import reg.udral.physics.kinematics.cartesian

# Import other namespaces we're planning to use. Nested namespaces are not auto-imported, so in order to reach,
# say, "uavcan.node.Heartbeat", you have to "import uavcan.node".
import uavcan.node  # noqa


class StatePublisher:
    REGISTER_FILE = "StateSubscriber.db"
    """
    The register file stores configuration parameters of the local application/node. The registers can be modified
    at launch via environment variables and at runtime via RPC-service "uavcan.register.Access".
    The file will be created automatically if it doesn't exist.
    """

    def __init__(self) -> None:
        node_info = uavcan.node.GetInfo_1.Response(
            software_version=uavcan.node.Version_1(major=1, minor=0),
            name="org.jeroboam.state_publisher",
        )
        # The Node class is basically the central part of the library -- it is the bridge between the application and
        # the UAVCAN network. Also, it implements certain standard application-layer functions, such as publishing
        # heartbeats and port introspection messages, responding to GetInfo, serving the register API, etc.
        # The register file stores the configuration parameters of our node (you can inspect it using SQLite Browser).
        self._node = pycyphal.application.make_node(node_info, StatePublisher.REGISTER_FILE)

        # Published heartbeat fields can be configured as follows.
        self._node.heartbeat_publisher.mode = uavcan.node.Mode_1.OPERATIONAL  # type: ignore
        self._node.heartbeat_publisher.health = uavcan.node.Health_1_0.NOMINAL
        self._node.heartbeat_publisher.vendor_specific_status_code = 42

        # Now we can create ports to interact with the network.
        # They can also be created or destroyed later at any point after initialization.
        # A port is created by specifying its data type and its name (similar to topic names in ROS or DDS).
        # The subject-ID is obtained from the standard register named "uavcan.sub.temperature_setpoint.id".
        # It can also be modified via environment variable "UAVCAN__SUB__TEMPERATURE_SETPOINT__ID".
        # self._sub_t_sp = self._node.make_subscriber(jeroboam.actuators.motion., "temperature_setpoint")

        self._sub_t_sp = self._node.make_subscriber(reg.udral.physics.kinematics.cartesian.State_0_1,
                                                    "robot_current_state")
        
        self._pub_v_cmd = self._node.make_publisher(reg.udral.physics.kinematics.cartesian.Twist_0_1, "robot_twist_goal")

        self._node.start()  # Don't forget to start the node!

    async def run(self) -> None:
        """
        The main method that runs the business logic. It is also possible to use the library in an IoC-style
        by using receive_in_background() for all subscriptions if desired.
        """
        robot_current_pose = reg.udral.physics.kinematics.cartesian.Pose_0_1
        robot_current_twist = reg.udral.physics.kinematics.cartesian.Twist_0_1
        previous_ts = 0

        async def on_robot_current_state_msg(msg: reg.udral.physics.kinematics.cartesian.State_0_1, _: pycyphal.transport.TransferFrom) -> None:
            ts = time.time()
            nonlocal previous_ts
            freq = 1/(ts - previous_ts)
            previous_ts = ts
            print(f'Hz {freq}')
            nonlocal robot_current_pose
            robot_current_pose = msg.pose
            nonlocal robot_current_twist
            robot_current_twist= msg.twist
            # print(f'pose  {robot_current_pose.position.value.meter} {robot_current_pose.orientation.wxyz}')
            # print(f'twist {robot_current_twist.linear.meter_per_second} {robot_current_twist.angular.radian_per_second}')
            # print()

        self._sub_t_sp.receive_in_background(on_robot_current_state_msg)  # IoC-style handler.


        # Expose internal states to external observers for diagnostic purposes. Here, we define read-only registers.
        # Since they are computed at every invocation, they are never stored in the register file.
        # self._node.registry["thermostat.error"] = lambda: temperature_error
        # self._node.registry["thermostat.setpoint"] = lambda: temperature_setpoint

        # Read application settings from the registry. The defaults will be used only if a new register file is created.
        # gain_p, gain_i, gain_d = self._node.registry.setdefault("thermostat.pid.gains", [0.12, 0.18, 0.01]).floats

        # logging.info("Application started with PID gains: %.3f %.3f %.3f", gain_p, gain_i, gain_d)
        print("Running. Press Ctrl+C to stop.", file=sys.stderr)

        # This loop will exit automatically when the node is close()d. It is also possible to use receive() instead.
        async for m, _metadata in self._sub_t_sp:
            assert isinstance(m, reg.udral.physics.kinematics.cartesian.State_0_1)
            #compute twist commands
            linear = uavcan.si.unit.velocity.Vector3_1_0()
            linear.meter_per_second = [1., 0., 0.]
            angular = uavcan.si.unit.angular_velocity.Vector3_1_0()
            angular.radian_per_second = [0., 0., 3.14]

            await self._pub_v_cmd.publish(reg.udral.physics.kinematics.cartesian.Twist_0_1(linear=linear, angular=angular))

    def close(self) -> None:
        """
        This will close all the underlying resources down to the transport interface and all publishers/servers/etc.
        All pending tasks such as serve_in_background()/receive_in_background() will notice this and exit automatically.
        """
        self._node.close()


async def main() -> None:
    logging.root.setLevel(logging.INFO)
    app = StatePublisher()
    try:
        await app.run()
    except KeyboardInterrupt:
        pass
    finally:
        app.close()


if __name__ == "__main__":
    asyncio.run(main())

