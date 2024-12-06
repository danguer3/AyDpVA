import rclpy
from rclpy.node import Node
from std_msgs.msg import  Float32, Int32

class SubscriberNode(Node):
    def __init__(self):
        super().__init__('subscriber_node')
        self.subscription_angle = self.create_subscription(
            Float32, '/angle', self.listener_callback_angle,10
        )
        self.subscription_speed = self.create_subscription(
            Int32, '/speed', self.listener_callback_speed,10
        )
        self.subscription_angle

    def listener_callback_angle(self, msg):
        self.get_logger().info('el angulo de giro es: "%f"' %msg.data)

    def listener_callback_speed(self, msg):
        self.get_logger().info('la velocidad es: "%f"' %msg.data)

        if msg.data > 0:
            self.get_logger().info('Adelante')
        
        elif msg.data < 0:
            self.get_logger().info('atras')
        else:
            self.get_logger().info('detenido')

def main(args=None):
    try:
        rclpy.init(args=args)
        subscriber_node = SubscriberNode()
        rclpy.spin(subscriber_node)
    except KeyboardInterrupt:
        print('.... Ok boy')
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
