import requests
import os
#https://vk.com/friends

import  post

os.system("cls||clear")
import time
print("""             
||    ||             ||||||||   ||||||||
||    ||             ||         ||
||||||||      ||       |||      ||||||||                   
||    ||    ||  ||        |||   ||                    ____||||||____
||    ||     ||||    ||||||||   ||||||||             |___||||||||___|
""")

time.sleep(2)

os.system("cls||clear")

#status = requests.get("https://vk.com")

comms = {"help": "connect [-url value]\ndisconnect []"}
сur_comm = []

_input = ""

def main_line():
    global _input
    global cur_comm
    print("HoSE#> ", end="")
    _input = input()
    cur_comm = _input.split()

    print(cur_comm)
    print(comms.get(cur_comm[0]))

main_line()