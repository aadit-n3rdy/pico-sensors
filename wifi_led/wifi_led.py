import rp2
import network
import time
import socket
from machine import Pin

rp2.country('IN')
led = Pin("LED", Pin.OUT)

# README: Fill in your WLAN's SSID and Password below
ssid = ""
password = ""

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

while True:
    if (wlan.status() in [network.STAT_IDLE, network.STAT_CONNECTING]):
        print("Connecting to WLAN {}...".format(ssid))
        if led.value() != 0:
            led.off()
        else:
            led.on()
    else:
        break
    time.sleep(1)

if wlan.status() != 3:
    print("ERROR CONNECTING TO WLAN: STATUS {}".format(wlan.status()))
    raise RunTimeError("Error connecting to WLAN")
print("Connected to WLAN {}".format(ssid))
print("IP address: {}".format(wlan.ifconfig()[0]))

led.off()

serv_addr = ("", 80)
s = socket.socket()
s.bind(serv_addr)
s.listen()

print("Listening for connections...")

def gen_msg(led):
    return "LED is " + ('ON' if led.value() != 0 else 'OFF')

while True:
    try:
        client, client_addr = s.accept()
        print("Accepted connection from {}".format(client_addr))
        msg = client.recv(2048)
        if '/led/on' in msg:
            led.on()
            client.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
            client.send(gen_msg(led))    
        elif '/led/off' in msg:
            led.off()
            client.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
            client.send(gen_msg(led))
        elif '/led/status' in msg:
            client.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
            client.send(gen_msg(led))
        print("Received message :\n{}\n".format(msg))
        client.close()
    except Exception as e:
        print('ERROR: ', str(e))
        s.close()
        break

