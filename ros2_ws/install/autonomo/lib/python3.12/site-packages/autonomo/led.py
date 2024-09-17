import RPi. GPIO as GPIO
import time
# configuracion del pin GPIO
LED_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.out)
# Ciclo de encendido y apagado del LED
while True:
    GPIO.output(LED_PIN, GPIO.HIGH)
    # Enciende el LED
    time.sleep(1)
    # Espera 1 segundo
    GPIO.output(LED_PIN, GPIO.LOW)
    # Apaga el LED
    time.sleep(1)