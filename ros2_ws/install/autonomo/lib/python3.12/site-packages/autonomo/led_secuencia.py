import RPi.GPIO as GPIO
import time

# Configuración de los pines GPIO
LED1_PIN = 17  # LED 1
LED2_PIN = 27  # LED 2
LED3_PIN = 22  # LED 3
BUTTON_PIN = 18  # Botón

# Configuración inicial de GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED1_PIN, GPIO.OUT)
GPIO.setup(LED2_PIN, GPIO.OUT)
GPIO.setup(LED3_PIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Botón con resistencia pull-up

# Variables para controlar la secuencia
sequence_index = 0  # Inicia en la primera secuencia
sequences = [
    (GPIO.HIGH, GPIO.LOW, GPIO.LOW),   # Secuencia 1
    (GPIO.HIGH, GPIO.HIGH, GPIO.LOW),  # Secuencia 2
    (GPIO.HIGH, GPIO.HIGH, GPIO.HIGH)  # Secuencia 3
]

def set_leds(led1_state, led2_state, led3_state):
    GPIO.output(LED1_PIN, led1_state)
    GPIO.output(LED2_PIN, led2_state)
    GPIO.output(LED3_PIN, led3_state)

# Ciclo principal
try:
    while True:
        button_state = GPIO.input(BUTTON_PIN)

        # Si el botón está presionado (estado bajo)
        if button_state == GPIO.LOW:
            # Cambia a la siguiente secuencia
            sequence_index = (sequence_index + 1) % len(sequences)
            
            # Actualiza el estado de los LEDs según la secuencia actual
            set_leds(*sequences[sequence_index])
            
            # Evitar rebote del botón
            time.sleep(0.3)

        # Pequeño retraso para evitar lecturas erráticas
        time.sleep(0.1)

except KeyboardInterrupt:
    # Limpiar configuración GPIO al finalizar
    GPIO.cleanup()
