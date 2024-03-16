import socket
from threading import Thread
from connections import HOST_IP, HOST_PORT
SERVER_HOST = str(HOST_IP)
SERVER_PORT = int(HOST_PORT)
separator_token = "<SEP>"

client_sockets = set()
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((SERVER_HOST, SERVER_PORT))
s.listen(5)
print(f"Server created on {SERVER_HOST}:{SERVER_PORT}")

def listen_for_client(cs):
    while True:
        try:
            global msg
            msg = cs.recv(1024).decode()
            print(msg)
        except Exception as e:
            print(f"Error: {e}")
            client_sockets.remove(cs)
        else:
            msg = msg.replace(separator_token, ": ")
        for client_socket in client_sockets:
            client_socket.send(msg.encode())

while True:
    client_socket, client_address = s.accept()
    print(f"New connection from {client_address}")
    client_sockets.add(client_socket)
    t = Thread(target=listen_for_client, args=(client_socket,))
    t.daemon = True
    t.start()

for cs in client_sockets:
    cs.close()
s.close()
