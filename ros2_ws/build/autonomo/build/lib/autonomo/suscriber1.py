import rclpy
from std_msgs.msg import Int32, Float32
from time import sleep

# Variables globales para almacenar los valores de velocidad y ángulo
velocidad = 0
angulo = 0.0

def velocidad_callback(msg):
    global velocidad
    velocidad = msg.data
    mostrar_direccion()

def angulo_callback(msg):
    global angulo
    angulo = msg.data
    mostrar_direccion()

# Función para determinar la dirección del vehículo
def mostrar_direccion():
    if velocidad > 0:
        if angulo == 0:
            direccion = "hacia adelante en línea recta"
        elif angulo > 0:
            direccion = "hacia adelante a la derecha"
        else:
            direccion = "hacia adelante a la izquierda"
    elif velocidad < 0:
        if angulo == 0:
            direccion = "hacia atrás en línea recta"
        elif angulo > 0:
            direccion = "hacia atrás a la derecha"
        else:
            direccion = "hacia atrás a la izquierda"
    else:
        direccion = "detenido"

    print(f'Velocidad: {velocidad}, Ángulo: {angulo} -> Dirección: {direccion}')

def main(args=None):
    # Inicializa ROS 2
    rclpy.init(args=args)

    # Crear un nodo
    node = rclpy.create_node('minimal_subscriber1')

    # Crear suscriptores para los tópicos 'velocidad' (Int32) y 'angulo' (Float32)
    velocidad_subscriber1 = node.create_subscription(Int32, 'velocidad', velocidad_callback, 10)
    angulo_subscriber1 = node.create_subscription(Float32, 'angulo', angulo_callback, 10)

    # Bucle para mantener el nodo en ejecución
    try:
        while rclpy.ok():
            # Procesar los mensajes entrantes
            rclpy.spin_once(node)
            sleep(0.1)  # Reduce el uso de CPU
    except KeyboardInterrupt:
        pass

    # Cerrar ROS 2
    rclpy.shutdown()

if __name__ == '__main__':
    main()
