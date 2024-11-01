import socket
from pynput.keyboard import Controller

keyboard = Controller()

HOST = 'xxx.xxx.xxx.xxx'
PORT = 00000 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Waiting for connection...")
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            key = data.decode('utf-8')
            print("Received:", key)
            keyboard.press(key)
            keyboard.release(key)