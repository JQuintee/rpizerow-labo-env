from gpiozero import LED  # Importa la clase LED de la biblioteca gpiozero
from gpiozero import Buzzer  # Importa la clase Buzzer de la biblioteca gpiozero

# Inicializa el buzzer en el pin 15
buzzer = Buzzer(15)

# Inicializa los LEDs en los pines correspondientes
ledVerde = LED(26)  # LED verde en el pin 26
ledRojo = LED(19)   # LED rojo en el pin 19
ledAzul = LED(13)   # LED azul en el pin 13

# Bucle infinito para esperar y procesar las acciones del usuario
while True:
    accion = input()  # Espera a que el usuario ingrese una acción
    if 'buzz' in accion:
        if 'on' in accion:
            buzzer.on()  # Enciende el buzzer si la acción contiene 'buzz' y 'on'
        elif 'off' in accion:
            buzzer.off()  # Apaga el buzzer si la acción contiene 'buzz' y 'off'
    elif 'rbg' in accion:
        if 'blue' in accion:
            ledAzul.toggle()  # Cambia el estado del LED azul si la acción contiene 'rbg' y 'blue'
        elif 'red' in accion:
            ledRojo.toggle()  # Cambia el estado del LED rojo si la acción contiene 'rbg' y 'red'
        elif 'green' in accion:
            ledVerde.toggle()  # Cambia el estado del LED verde si la acción contiene 'rbg' y 'green'
