import rclpy
import RPi.GPIO as GPIO
import time
from rclpy.node import Node
from sensor_msgs.msg import LaserScan

# Configuracion de lo motores 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


#mMOTOR A
inA=17
in1=27
in2=22
#MOTOR B
inB=23
in3=24
in4=25

#configuracion de los pines GPIO 
#MOTOR A
GPIO.setup(inA, GPIO.OUT)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
#MOTOR B
GPIO.setup(inB, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)

#CONFIGURACION INICIAL DE LOS MOTORES

vel= GPIO.PWM(inA,100)
vel.start(0)
vel1= GPIO.PWM(inB,100)
vel1.start(0)

#Definimos la distancia umbral en metros (30 cm) y tiempo de giro 
THRESHOLD_DISTANCE = 0.4
turn_time=0.5

#Configuracion de movimiento de los motores

def forward_1():
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.HIGH)
    GPIO.output(in4, GPIO.LOW)
    vel.ChangeDutyCycle(50)
    vel1.ChangeDutyCycle(50)

def forward():
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.HIGH)
    GPIO.output(in4, GPIO.LOW)
    vel.ChangeDutyCycle(50)
    vel1.ChangeDutyCycle(50)

def right():
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)
    vel.ChangeDutyCycle(50)
    #vel1.ChangeDutyCycle(100)

def left():
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.HIGH)
    GPIO.output(in4, GPIO.LOW)

def stop():
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)

    THRESHOLD_DISTANCE = 0.4

def lidar_callback(msg):    
    num_ranges =len(msg.ranges)
    right_index = num_ranges // 4 
    back_index = num_ranges // 2 
    left_index = (3 * num_ranges) // 4
    front_index = 0

    #Distancias en cada direccion 
    front_distance = msg.ranges[front_index]
    left_distance = msg.ranges[left_index]
    back_distance = msg.ranges[back_index]
    right_distance = msg.ranges[right_index]

    #Checamos si hay obstaculos a menos de 40 cm en alguna direccion
    state="moving_forward"
    if front_distance < THRESHOLD_DISTANCE:
        print("Obstaculo adelante")
        print('La distancia es:' + str(front_distance))
        while state =="moving_forward":
            forward()
            print("Adelante")
            front_distance = msg.ranges[right_index]
            print("distancia=" +str(front_distance))

            if front_distance < THRESHOLD_DISTANCE:
                break
    if left_distance < THRESHOLD_DISTANCE:
        print("Osbtaculo a la izquierda")
        print('La distancia es:' + str(left_distance))
    if back_distance < THRESHOLD_DISTANCE:
        print("Osbtaculo atras")
        print('La distancia es:' + str(back_distance))
    if right_distance < THRESHOLD_DISTANCE:
        print("Osbtaculo a la derecha")
        print('La distancia es:' + str(right_distance))
        print(len(msg.ranges))
        




"""    if state == "moving_forward" and front_distance>THRESHOLD_DISTANCE:
        forward()
        print("Adelante")
        state = "moving_forward"
"""
""" if state == "moving_forward" and front_distance < THRESHOLD_DISTANCE:
        print("Obstáculo detectado al frente")
        left()
        state = "turning_left"

        if state == "turning_left" and left_distance > THRESHOLD_DISTANCE:  # Cambia de angulo mirando al carril izquierdo 
            forward_1(),print("Avanzando al carril izquierdo.")
            state="forward_front"
"""
"""elif state =="forward_front" and front_distance > THRESHOLD_DISTANCE:
        print("SEGUIR ADELANTE")
        forward_1()

    if distance<=0.3:
            print("Alineando al carril izquierdo")
            right() #gira a la derecha para alinearse al carril izquierdo 
            time.sleep(0.1)  
            state = "aligning_right
                
    if state == "aligning_right":
           if front_distance > THRESHOLD_DISTANCE and right_distance<=THRESHOLD_DISTANCE:  # frente sin obstaculo y empeiza avanzar recto
            print("Carril izquierdo alineado. Avanzando.")
            forward()
            state = "overtaking"
    if state == "overtaking":
        if right_distance > THRESHOLD_DISTANCE:  #El carril derecho esta libre ya se rebaso el obstaculo
            print("Carril derecho libre. Regresando.")
            right()
            time.sleep(0.1)
            state = "turning_right"
    elif state == "turning_right":
        if  right_distance<= THRESHOLD_DISTANCE:  
            print("Regresando al carril derecho, de frente.")
            forward() 
            time.sleep(0.2)  
            state = "forward_right"
    elif state == "forward_right":
        if distance<= THRESHOLD_DISTANCE:  
            print("Carril derecho alineado. Continuando hacia adelante.")
            left()
            state = "turning_left"
    elif state== "turning_left":
        if back_distance>=THRESHOLD_DISTANCE and front_distance>THRESHOLD_DISTANCE:
            print("Avanzando carril derecho libre")
            forward()
    """
def main(args=None):
    rclpy.init(args=args)

    node= rclpy.create_node('simple_lidar_subscriber')

    #creamos el subscriber al topico /scan que utiliza mensajes tipo LaserScan

    node.create_subscription(LaserScan, '/scan', lidar_callback, 10)
    #ejecutamos el nodo hasta que se detenga
    rclpy.spin(node)
    # Deestruimos el nodo cuando se detiene
    node.destroy_node()
    rclpy.shutdown
if __name__ == '__main__':
    main()
