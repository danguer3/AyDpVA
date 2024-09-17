import rclpy
from std_msgs.msg import String
from time import sleep

def callback(msg):
    # Función de callback que se llama cuando llega un mensaje
    print(f'Received message: "{msg.data}"')

def main(args=None):
    # Inicializa ROS 2
    rclpy.init(args=args)

    # Crea un nodo (sin clases)
    node = rclpy.create_Node('minimal_subscriber')

    # Crear un suscriptor para mensajes del tipo String en el tópico 'topic'
    node.create_subscription(String, 'topic', callback, 10)

    # Bucle para mantener el nodo en ejecución
    try:
        while rclpy.ok():
            # Corriendo y procesando mensajes
            rclpy.spin_once(node)
            sleep(0.1)  # Reduce el uso de CPU
    except KeyboardInterrupt:
        pass
    
    # Cierra ROS 2
    
    rclpy.shutdown()

if __name__ == '__main__':
    main()
    