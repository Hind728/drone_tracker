import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import subprocess
import math

class DroneTracker(Node):
    def __init__(self):
        super().__init__("drone_tracker")
        self.timer = self.create_timer(0.1, self.control_loop)
        self.t = 0.0
        self.state = "takeoff"
        self.drone_x = 0.0
        self.drone_y = 0.0
        self.drone_z = 0.0
        self.target_x = 5.0
        self.target_y = 0.0
        self.target_z = 2.0
        self.get_logger().info("Drone Tracker demarre !")

    def send_twist(self, vx, vy, vz, wz):
        cmd = f"gz topic -t /X3/gazebo/command/twist -m gz.msgs.Twist -p \"linear: {{x:{vx} y:{vy} z:{vz}}} angular: {{z:{wz}}}\""
        subprocess.Popen(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    def control_loop(self):
        self.t += 0.1

        if self.state == "takeoff":
            self.send_twist(0, 0, 0.5, 0)
            if self.t > 4.0:
                self.state = "track"
                self.t = 0.0
                self.get_logger().info("Debut du suivi de la cible rouge !")

        elif self.state == "track":
            # Deplacer la cible en cercle
            self.target_x = 5.0 * math.cos(self.t * 0.3)
            self.target_y = 5.0 * math.sin(self.t * 0.3)

            # Deplacer la boite rouge dans Gazebo
            cmd = f"gz model -m target --pose \"{self.target_x} {self.target_y} 0.5 0 0 0\""
            subprocess.Popen(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

            # Calculer direction vers cible
            dx = self.target_x - self.drone_x
            dy = self.target_y - self.drone_y

            dist = math.sqrt(dx**2 + dy**2)

            if dist > 1.0:
                vx = min(dx * 0.2, 0.5)
                vy = min(dy * 0.2, 0.5)
                wz = math.atan2(dy, dx) * 0.5
            else:
                vx = 0.0
                vy = 0.0
                wz = 0.0

            self.send_twist(vx, vy, 0.0, wz)
            self.get_logger().info(f"Cible: ({self.target_x:.1f}, {self.target_y:.1f}) dist={dist:.1f}")

            # Mise a jour position drone (approximation)
            self.drone_x += vx * 0.1
            self.drone_y += vy * 0.1

def main(args=None):
    rclpy.init(args=args)
    node = DroneTracker()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
