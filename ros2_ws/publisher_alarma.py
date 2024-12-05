import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool
import sys
import termios
import tty

class AlarmPublisher(Node):
    def __init__(self):
        super().__init__('alarm_publisher')
        self.alarm_state = False  # Estado de la alarma (apagada por defecto)
        self.alarm_publisher = self.create_publisher(Bool, 'alarm_status', 10)
        self.timer = self.create_timer(1.0, self.publish_alarm_status)  # Publicar cada 1 segundo
        self.get_logger().info('Nodo Publicador de la Alarma Iniciado.')

    def publish_alarm_status(self):
        # Publicar el estado de la alarma
        self.alarm_publisher.publish(Bool(data=self.alarm_state))
        self.get_logger().info(f'Alarma {"encendida" if self.alarm_state else "apagada"}.')

    def keypress_listener(self):
        self.get_logger().info('Presiona "e" para encender la alarma.')
        old_attr = termios.tcgetattr(sys.stdin)
        tty.setcbreak(sys.stdin.fileno())

        try:
            while rclpy.ok():
                if sys.stdin.read(1) == 'e':  # Detectar la tecla 'e'
                    self.alarm_state = True
                    self.get_logger().info('Alarma encendida.')
                rclpy.spin_once(self)
        except KeyboardInterrupt:
            self.get_logger().info('Interrupción del nodo.')
        finally:
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_attr)
            rclpy.shutdown()

def main(args=None):
    rclpy.init(args=args)
    alarm_publisher = AlarmPublisher()
    try:
        alarm_publisher.keypress_listener()
    except rclpy.exceptions.ROSInterruptException:
        pass

if __name__ == '__main__':
    main()