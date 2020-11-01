import requests
import os
#https://vk.com/friends

import  post

#url = input()

os.system("cls||clear")
import time
print("""             
||    ||             ||||||||   ||||||||
||    ||             ||         ||
||||||||      ||       |||      ||||||||                   
||    ||    ||  ||        |||   ||                    ____||||||____
||    ||     ||||    ||||||||   ||||||||             |___||||||||___|
""")

time.sleep(3)

os.system("cls||clear")

status = requests.get("https://vk.com")
print(status)

print("1| Params\n2| Get")
menu = int(input())

if menu == 1:
    print("url: ", end="")
    url = input()
    print("?key=value : ?", end="")
    key_value = input()
    post.post(url, key_value)