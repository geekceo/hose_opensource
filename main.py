import requests
import os
import json
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

comms = {"help": "connect [-url value]\ndisconnect []\nprint [value] [$variable]\nvar [name] [value]"}
env_var = {}

сur_comm = []

_input = ""

def main_line():
    global _input
    global cur_comm
    print("HoSE#> ", end="")
    _input = input()
    cur_comm = _input.split()

    comm_handler()

def comm_handler():
    global cur_comm
    global env_var


    all = ""
    if (cur_comm[0] == "print"):
        for i in range(1, len(cur_comm)):
            all += cur_comm[i]

        words = all.split()

        for word in words:
            if ('$' in word):
                print(env_var.get(word[1:]), end="")
            else:
                print(word, end="")

        print()
        main_line()

    elif (cur_comm[0] == "var"):
        env_var.update({cur_comm[1]:cur_comm[2]})
        main_line()

main_line()