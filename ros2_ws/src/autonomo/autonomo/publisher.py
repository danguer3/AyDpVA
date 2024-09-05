import rclpy
from std_msgs.msg import String
from time import sleep

def main (args=None):
    #Inicializa ROS 2
    rclpy.init(args=args)

    #Crea un nodo (aqui usamos 'minimal publisher' como nombre del nodo)
    node = rclpy.create_node('minimal_publisher')

    #Crea un publicador para mensajes del tipo String en el topico 'topic'
    publisher = node.create_publisher(String, 'topic', 10)

    #configura el mensaje
    msg = String()

    #Bucle para publicar mensaje
    i = 0
    while rclpy.ok():
        #Asigna un valor al mensaje
        msg.data = f'Hello World: {i}'

        #Publica el mensaje
        publisher.publish(msg)

        #Imprime un mensaje de información
        node.get_logger().info(f'Publishing: "{msg.data}"')

        #Incrementa el contador
        i += 1

        #Espera 0.5 segundos
        sleep(0.5)

    #Cierra ROS2
    rclpy.shutdown()

if __name__=='__main__': # type: ignore
    main()