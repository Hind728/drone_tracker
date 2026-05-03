import os
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        ExecuteProcess(
            cmd=["gz", "sim", "-r", "/usr/share/gz/gz-sim8/worlds/quadcopter.sdf"],
            output="screen"
        ),
        Node(
            package="ros_gz_bridge",
            executable="parameter_bridge",
            arguments=[
                "/X3/gazebo/command/motor_speed@actuator_msgs/msg/Actuators@gz.msgs.Actuators",
            ],
            output="screen"
        ),
        Node(
            package="drone_tracker",
            executable="drone_controller",
            output="screen"
        ),
    ])
