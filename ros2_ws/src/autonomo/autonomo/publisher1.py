import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32, Float32
from time import sleep

def main(args=None):
    # Inicializa ROS 2
    rclpy.init(args=args)

    # Crear un nodo
    node = rclpy.create_node('vehicle_publisher1')

    # Crear publicadores para los tópicos 'velocidad' (Int32) y 'angulo' (Float32)
    velocidad_publisher1 = node.create_publisher(Int32, 'velocidad', 10)
    angulo_publisher1 = node.create_publisher(Float32, 'angulo', 10)

    while rclpy.ok():
        try:
            # Pedir valores al usuario
            velocidad = int(input('Introduce la velocidad en {m/s} : '))
            angulo = float(input('Introduce el ángulo en grados : '))

            # Publicar los valores en los respectivos tópicos
            velocidad_publisher1.publish(Int32(data=velocidad))
            angulo_publisher1.publish(Float32(data=angulo))

            # Imprimir los valores publicados
            node.get_logger().info(f'Publicando -> Velocidad: {velocidad}, Ángulo: {angulo}')
        
        except ValueError:
            node.get_logger().error('Error: Entrada no válida.')

        # Espera 0.5 segundos antes de la siguiente iteración
        sleep(0.5)

    # Cerrar ROS 2
    rclpy.shutdown()

if __name__ == '__main__':
    main()
