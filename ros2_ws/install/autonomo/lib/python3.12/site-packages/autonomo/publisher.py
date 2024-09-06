import rclpy
from std_msgs.msg import String
from time import sleep

def main(args=None):
    #inicializa ros 2
    rclpy.init(args=args)
    #crear un nodo (aqui usamos 'minimal publisher'como nombre de nodo)
    node = rclpy.create_node('minimal_publisher')
    #crear umn publicador para mensages del tipo srting en el topico 'topic'
    publisher = node.create_publisher(String, 'topic', 10)
    #configura el mrensaje
    msg = String()
    # bucle para publicar mensajes
    i =0
    while rclpy.ok():
        #asigna un valor al mensaje
        msg.data = f'Hello world: {i}'
        #publica el mensaje
        publisher.publish(msg)
        #imprime un mensaje de informacion
        node.get_logger().info(f'publishing: "{msg.data}"')
        #incrementa el contador
        i += 1
        #espera 0.5 segundos
        sleep(0.5)
    # cierra ros 2
    rclpy.shutdown()
if __name__ == '_main_':
    main()

