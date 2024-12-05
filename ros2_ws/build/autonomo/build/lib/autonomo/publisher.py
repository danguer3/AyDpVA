import rclpy
from std_msgs.msg import String
from time import sleep 


def main(args=None):
    #INicializa ROS2
    rclpy.init(args=args) 

    #crea un nodo (aqui usamos 'minimal:publisher' como nombre del nodo)
    node= rclpy.create_node('minimal_publisher')

    #crea un publicador para mensajes del tipo String en el topico 'topic'
    publisher=node.create_publisher(String, 'topic', 10) 

    #Confiura el mensaje
    msg=String()

    #bucle para publicar mensajes
    i=0

    while rclpy.ok():
        #Asigna un valor al mensaje
        msg.data= f'Hello World: {i}'

        #Oublica el mensaje
        publisher.publish(msg)

        #Imprime un mensaje de informacion
        node.get_logger().info(f'Publishing:"{msg.data}"')

        #INcrementa el contador
        i+= 1
        #Espera 0.5 segundos
        sleep(0.5)
    #cierra ROS 2
    rclpy.shutdown()
if __name__ == '__main__':
    main()     



