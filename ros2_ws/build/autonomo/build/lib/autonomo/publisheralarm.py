import rclpy
import rclpy.node 
from std_msgs.msg import Bool
import termios
import sys
import tty
from time import sleep 


def main(args=None):
    #INicializa ROS2
    rclpy.init(args=args) 

    #crea un nodo (aqui usamos 'alarm_publisher' como nombre del nodo)
    node= rclpy.create_node('alarm_publisher')

    #crea un publicador para mensajes en el topico 'alarm'
    alarm_pub=node.create_publisher(Bool, 'alarm', 10) 

    # Estado de la alarma 
    estado=False
    
    def estatus_alarma():
    
        nonlocal estatus_alarma
        msg=bool()
        msg.data=estado
        alarm_pub.publish(msg.data)
        node.get_logger().info(f'Alarma {"Encendida" if estado else "apagada"}')

        timer= node.create_timer(1.0, estatus_alarma)

        node.get_logger().info('Presiona "e" para encender la alarma.')
        old_attr = termios.tcgetattr(sys.stdin)
        tty.setcbreak(sys.stdin.fileno())

    try:
        while rclpy.ok():

            if  sys.stdin.read(1) == 'e':  
                estado=True
                node.get_logger().info(f'"La alarma esta Encencida"')
            rclpy.spin_once(node) 
    except KeyboardInterrupt:
        node.get_logger().info('Error.')
    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_attr)
        node.destroy_node()


        rclpy.shutdown()

    
if __name__ == '__main__':
    main()