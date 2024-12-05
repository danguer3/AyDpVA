import rclpy
from std_msgs.msg import String
from time import sleep

def callback(estado):
    #funcion del callback que se llama callback cuando tenga un mensaje
    print(f'Reiceved message: "{estado.data}"')

def main (args=None):
    #Inicializa ROS2
    rclpy.init(args=args)  

    #crea un nodo (Aqui usamos 'alarm_subscriber' como nombre del nodo)
    node= rclpy.create_node('alarm_subscriber')

    #crea un suscriptor para mensajes del tipo String en el topico 'topic'
    node.create_subscription(String, 'alarm', callback, 10)  

    #bucle para mantener el nodo en ejecucion 
    try:
        while rclpy.ok():
            #el nodo sigue corriendo y procesando mensajes
            rclpy.spin_once(node)
            sleep(0.1) #reduce el uso del CPU
    except KeyboardInterrupt:
        pass

    #cierra ROS2
    rclpy.shutdown()

if __name__=='__main__':
    main() 