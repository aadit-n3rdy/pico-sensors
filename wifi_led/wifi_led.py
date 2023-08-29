import rp2
import network
import time
import socket
from machine import Pin

rp2.country('IN')
led = Pin("LED", Pin.OUT)

# TODO: Fill in your WLAN's SSID and Password below
ssid = ""
password = ""


wlan = network.WLAN(network.STA_IF) # Specified that the Pico W is connecting to an existing network, as a client
wlan.active(True) 					# Enables the wireless module
wlan.connect(ssid, password)

while True:
    ''' Polls for the status of the connection, and waits
    till either connection fails, or a connection has been established'''
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
    raise Exception("Error connecting to WLAN: status code {}".format(wlan.status()))
print("Connected to WLAN {}".format(ssid))
print("IP address: {}".format(wlan.ifconfig()[0]))

led.off()

serv_addr = ("", 80) # Specifies that the server will listen on the self IP address (indicated by the empty string), on port 80
s = socket.socket()
s.bind(serv_addr)
s.listen()

print("Listening for connections...")

def gen_msg(led):
    ''' Helper function to generate a string which specifies the state of the LED'''
    return "LED is " + ('ON' if led.value() != 0 else 'OFF')

while True:
    try:
        client, client_addr = s.accept()
        print("Accepted connection from {}".format(client_addr))
        msg = client.recv(2048)
        '''
        The following statements check if the string '/led/<action>' is present in the
        HTTP Request. The entire request is not parsed. Thus, requests which would be considered
        invalid HTTP Requests would still work in this example (such as those created using telnet).
        While this method has its own disadvantages, it does not require the use of an additional HTTP
        parser library, which reduces the load on the processor.
        '''
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
        print("Received message :\n{}\n".format(msg.decode('ascii')))
        client.close()
    except Exception as e:
        print('ERROR: ', str(e))
        s.close()
        break

