import RPi.GPIO as GPIO
import time
#CONFIGURACION DEL PIN GPIO

LED_PIN1=17
LED_PIN2=22
LED_PIN3=27
BUTTON=23
#LED 1
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN1, GPIO.OUT)
#LED 2
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN2, GPIO.OUT)
#LED 3
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN3, GPIO.OUT)
# PULSADOR
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON,GPIO.IN)

def main():

    secuencia=0
    while True:
       
        pulsador=GPIO.input(BUTTON)
        if pulsador==GPIO.LOW:
            secuencia = (secuencia+1) % 3
        #Secuencia 1
            if secuencia==0:
                GPIO.output(LED_PIN1, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(LED_PIN2, GPIO.LOW)
                GPIO.output(LED_PIN3, GPIO.LOW)

        #Secuencia 2
            if secuencia==1:
                GPIO.output(LED_PIN1, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(LED_PIN2, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(LED_PIN3, GPIO.LOW)

        #Secuencia 3
            elif secuencia==2:
                GPIO.output(LED_PIN1, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(LED_PIN2, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(LED_PIN3, GPIO.HIGH)
                time.sleep(0.5)
        time.sleep(0.5)            
    pass 

if __name__=='__main__':
    main()