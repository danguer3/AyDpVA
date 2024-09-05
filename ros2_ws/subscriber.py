import rcply
from std_msgs.msg import String
from time import sleep

def callback(msg):
    #Funcion de callback que se llama cuando llega un mensaje
    print(f'Received message: "{msg.data}"')

def main(args=None):
    #Inicializa ROS2
    rcply.init (args=args)

    #Crea un nodo (aqui usamos 'minimal_subscriber' como nombre del nodo)
    node = rcply.create_node('minimal_subscriber')

    #Crea un subscriptor para mensajes del tipo String en el topico 'topic'
    node.create_subscription(String, 'topic', callback, 10)

    #Bucle para mantener el nodo en ejecución 
    try:
        while rcply.ok():
            #El nodo sigue corriendo y procesando mensajes
            rcply.spin_once(node)
            sleep(0.1) #Reduce el uso del CPU
    except KeyboardInterrupt:
        pass
    
    #Cierra Ros2 
    rcply.shutdown()
    
if __name__ == '__main__':
    main()
     