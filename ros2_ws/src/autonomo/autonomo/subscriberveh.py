import rclpy
from std_msgs.msg import Float32, Int32
from time import sleep

def speed_callback(speed):
    #funcion del callback que se llama speed cuando tenga un mensaje
    
    global velocidad
    velocidad=int(speed.data)
    print(f'Velocidad: "{velocidad}"')

    if velocidad>=0:
        print("El auto esta acelerando hacia adelante")
    elif velocidad<0:
         print("El auto va hacia atras")

def angle_callback(angle):
    #funcion del callback que se llama angle cuando tenga un mensaje
    global angulo
    angulo=float(angle.data)
    print(f'Angulo: "{angulo}"')

    if angulo==0 or 180:
        print("El vehiculo va en linea recta")
    elif angulo<0>-179:
         print("El vehiculo va hacia la izquierda")
    elif angulo>0<179:
         print("El vehiculo va hacia derecha")
        
def main(args=None):
    #Inicializa ROS2
    rclpy.init(args=args)

    #crea un nodo (Aqui usamos 'vehicle_publisherveh' como nombre del nodo)
    node= rclpy.create_node('vehicle_publisherveh')

    #crea un suscriptor para mensajes''
    node.create_subscription(Int32, 'speed', speed_callback, 10)  
    node.create_subscription(Float32, 'angle',angle_callback,10)

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
