import rclpy
from std_msgs.msg import String
from time import sleep

def main(args=None):
    # Inicializa ROS 2
    rclpy.init(args=args)

    # Crear un nodo (aquí usamos 'minimal_publisher' como nombre del nodo)
    node = rclpy.create_node('minimal_publisher')

    # Crear un publicador para mensajes del tipo String en el tópico 'topic'
    publisher = node.create_publisher(String, 'topic', 10)

    # Configura el mensaje 
    msg = String()

    # Bucle para publicar mensajes
    i = 0
    while rclpy.ok():
        # Asigna un valor al mensaje
        msg.data = f'hello world: {i}'

        # Publica el mensaje
        publisher.publish(msg)

        # Imprime un mensaje de información
        node.get_logger().info(f'Publishing: "{msg.data}"')

        # Incrementa el contador
        i += 1

        # Espera 0.5 segundos
        sleep(0.5)

    # Cierra ROS 2
    rclpy.shutdown()

if __name__ == '__main__':
    main()