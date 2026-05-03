import os
from glob import glob
from setuptools import setup

package_name = "drone_tracker"

setup(
    name=package_name,
    version="0.0.0",
    packages=[package_name],
    data_files=[
        ("share/ament_index/resource_index/packages",
            ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
        (os.path.join("share", package_name, "launch"),
            glob("launch/*.py")),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="cocci",
    maintainer_email="hindkanoun05@gmail.com",
    description="Drone tracker ROS 2 Gazebo",
    license="MIT",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "drone_controller = drone_tracker.drone_controller:main",
        ],
    },
)
