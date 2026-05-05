# Drone Tracker - ROS 2 + Gazebo Sim

Ce projet ROS 2 (Jazzy) simule un drone quadrotor X3 dans Gazebo Sim qui suit automatiquement un autre drone X4 et un cube rouge en temps reel.

## Description
- Le drone X3 decolle automatiquement
- Il detecte la position du drone X4 et du cube rouge
- Il se dirige vers la cible et la suit en vol
- Le cube rouge se deplace en cercle comme cible
- Utilise le plugin MulticopterVelocityControl pour un vol stable
- Monde base sur le fichier multicopter_velocity_control.sdf de Gazebo Sim

## Lancer le projet
```bash
# Terminal 1 - Lancer Gazebo
gz sim -r ~/ros2_ws/src/drone_tracker/worlds/drone_tracker.world

# Terminal 2 - Bridge ROS2/Gazebo
ros2 run ros_gz_bridge parameter_bridge /X3/gazebo/command/twist@geometry_msgs/msg/Twist@gz.msgs.Twist

# Terminal 3 - Lancer le tracker
ros2 run drone_tracker drone_controller
 trim.9CB0843D-AB3C-4FE2-BD7E-DB0B2EB7DAB0.MOV
```

## Topics
- `/X3/gazebo/command/twist` : commandes de vitesse du drone X3
- `/model/x3/odometry` : position du drone X3

## Technologies
- ROS 2 Jazzy
- Gazebo Sim
- Plugin MulticopterVelocityControl
- Python 3
