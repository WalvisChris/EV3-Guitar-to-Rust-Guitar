#!/usr/bin/env python3
from ev3dev2.sensor.lego import TouchSensor, InfraredSensor
from ev3dev2.display import Display
from ev3dev2.sensor import INPUT_1, INPUT_4
import socket
import time

touch = TouchSensor(INPUT_1)
infra = InfraredSensor(INPUT_4)
screen = Display()

HOST = 'xxx.xxx.xxx.xxx'
PORT = 00000 

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    print("Connected to the server.")
    screen.text_pixels("Connected", True, 89, 64)
    screen.update()
except Exception as e:
    print("Failed to connect:", e)
    screen.text_pixels("Connection Failed", True, 89, 64)
    screen.update()
    time.sleep(3)
    exit(1)

flag = True

while True:
    if touch.is_pressed and flag:
        try:

            note = round(infra.proximity * 0.11)
            print("note:", note)
            screen.text_pixels(str(note), True, 89, 64)
            screen.update()

            if note < 10:
                data = str(note)
            else:
                data = "0"
            
            s.sendall(data.encode('utf-8'))
            print("Data sent:", data)
            
            flag = False
        
        except Exception as e:
            print("Error during sending:", e)
            screen.text_pixels("Send Error", True, 89, 64)
            screen.update()
            time.sleep(3)
            break

    elif not touch.is_pressed:
        flag = True

s.close()
print("Socket closed.")