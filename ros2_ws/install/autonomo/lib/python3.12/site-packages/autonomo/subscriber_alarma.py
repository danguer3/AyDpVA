import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool

class AlarmSubscriber(Node):
    def __init__(self):
        super().__init__('alarm_subscriber')
        self.subscription = self.create_subscription(
            Bool,
            'alarm_status',  # Debe coincidir con el nombre del tópico del publicador
            self.alarm_status_callback,
            10)
        self.subscription  # Previene que el garbage collector elimine la suscripción
        self.get_logger().info('Nodo Suscriptor de la Alarma Iniciado.')

    def alarm_status_callback(self, msg):
        # Procesa el mensaje recibido
        estado_alarma = "encendida" if msg.data else "apagada"
        self.get_logger().info(f'Alarma {estado_alarma}')

def main(args=None):
    rclpy.init(args=args)
    alarm_subscriber = AlarmSubscriber()
    rclpy.spin(alarm_subscriber)
    alarm_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
