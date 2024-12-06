from math import sin, cos, pi
import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, QoSReliabilityPolicy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

class JoyPublisher(Node):

    def __init__(self):
        # initializa
        super().__init__('joy_publisher')
        qos_profile = QoSProfile(depth=10)

        # define parámetros
        self._linear_scale = 0.2
        self._angular_scale = 0.2

        # inicia suscriptores
        self.joy_status = self.create_subscription(Joy, '/joy', self.joy_callback, QoSReliabilityPolicy.RELIABLE)

        # inicia publicadores
        self.robot_vel = self.create_publisher(Twist, '/cmd_vel', qos_profile)
        self.nodeName = self.get_name()
        self.get_logger().info(f"{self.nodeName} started")

        now = self.get_clock().now()


    def joy_callback(self, msg):
        
        A_button = msg.buttons[0]
        LSTICK_x_axis = int(msg.axes[0]*100)
        LSTICK_y_axis = int(msg.axes[1]*100)

        if A_button:
            self.get_logger().info(f"Motion x: {LSTICK_x_axis}, y: {LSTICK_y_axis}")
            # prepara y publica un mensaje para la velocidad
            cmd_vel = Twist()
            cmd_vel.linear.x = LSTICK_y_axis * self._linear_scale
            cmd_vel.angular.z = LSTICK_x_axis * self._angular_scale
            self.robot_vel.publish(cmd_vel)
            


def main(args=None):
    try:
        rclpy.init(args=args)
        joy_publisher = JoyPublisher()
        rclpy.spin(joy_publisher)
    except KeyboardInterrupt: 
        pass
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()