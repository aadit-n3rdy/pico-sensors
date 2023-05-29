from machine import Pin
from time import sleep
# We need these to run the program

led = Pin(25, Pin.OUT) # Here we tell the Pico that we want to use pin 25 as an output pin. (25 is the pin assigned to the onboard LED by default)

while True: # This loop executes indefinitely
    try:
        led.value(1) # This puts pin 25 at a logical HIGH, turning the LED on
        sleep(0.5) # We wait for 0.5 seconds
        led.value(0) # This puts pin 25 at a logical LOW, turning the LED off
        sleep(0.5)
    except KeyboardInterrupt: # This block ensures that the LED is turned off before exiting the program.
        led.value(0)
        break
    
# Note : You can also use led.toggle() to toggle the LED on and off
