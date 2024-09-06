import rclpy
from std_msgs.msg import String
from time import sleep

def callback(msg)
    # Funcion de callback que se llama cuando llega un mensaje
    print(f'Received message: "{msg.data}",)
          
def main(args=none):
    # Inicializa ROS 2
    rclpy.init(args=args)

    # crea un nodo (aqui usamos 'minimal_subscriber' como nombre del nodo)
    node = rclpy.create_node('minimal_subscriber')

    #crear un subscritor para mensajes del tipo String en el topico 'topic'
    node.create_subscriptor(String, 'topic', callback, 10)
    # Bucle para mantener el nodo en ejecucion
    try:
        while rclpy.ok():
            # corriendo y procesando mensajes
            rclpy.spin_once(node)
            sleep(0.1)  # Reduce el uso CPU
    except keyboardInterrupt:
        pass
    
    #cierra ROS 2
    rclpy.shutdown()
if_name_ =='_main_'
    main()
                                