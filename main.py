from microbit import *
import dht

# Configurar el sensor DHT conectado al pin0
sensor = dht.DHT11(pin0)

def on_forever():
    # Leer la humedad del sensor
    sensor.measure()
    humedad = sensor.humidity()
    
    # Mostrar la humedad en la pantalla LED
    basic.show_string(str(humedad) + "%")
    
    # Pausa de 1 segundo antes de la siguiente lectura
    sleep(1000)

basic.forever(on_forever)
