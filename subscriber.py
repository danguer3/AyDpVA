import rclpy 
from rclpy.node import Node
from std_msgs.msg import String

class MySubscriber(Node):
    def __init__(self):
        super().__init__('my_subscriber')
        timer_period = 0.5 #seg
        self.subscription = self.create_subscription(
            String,
            'my_topic',
            self.listener_callback,
            10
        )
    def listener_callback(self,msg):
        self.get_logger().info('resived : "%s"' % msg.data)


def main(args=None):
    try:
        rclpy.init(args=args)
        my_subscriber = MySubscriber()
        rclpy.spin(my_subscriber)
    except KeyboardInterrupt:
        print('.... fuck exit node')
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
