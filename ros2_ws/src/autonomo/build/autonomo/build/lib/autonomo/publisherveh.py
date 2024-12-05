
import rclpy

from std_msgs.msg import  Int32, Float32
from time import sleep 


def main(args=None):
    #INicializa ROS2
    rclpy.init(args=args)

    #crea un nodo (aqui usamos 'vehicle_publisherveh' como nombre del nodo)
    node= rclpy.create_node('vehicle_publisherveh')

    #crea un publicador para mensajes del tipo Float32 para angulo y Int32 para velocidad
    speed_pub=node.create_publisher(Int32, 'speed',10)
    angle_pub=node.create_publisher(Float32,'angle',10 )
    

    while rclpy.ok():
        try:
            #Asignar una variable al valor ingresado
            velocidad=int(input('Introduce el valor de velocidad: '))
            angulo=float(input('Introduce el angulo: '))
            #Publica el mensaje
            speed_pub.publish(Int32(velocidad))
            angle_pub.publish(Float32(angulo))
            
            
            #Imprime un mensaje de informacion
            node.get_logger().info(f'"Velocidad: {velocidad} Km/h, Angulo:{angulo}°"')
        except ValueError:
             node.get_logger().error('Error')
        sleep(0.5)
    rclpy.shutdown()
        
    
if __name__ == '__main__':
    main()     
