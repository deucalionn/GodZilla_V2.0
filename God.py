#coding:utf-8
import time
import os
import platform
import sys

sysinfo = platform.system()
 
if sys.argv[0] == "file":
    print(sys.argv[0].split(" ")[1])
        
try:
    import tkinter
except:


    if sysinfo ==  "Linux":
        os.system("sudo apt install python-tk")
        os.system("sudo apt install python-imaging-tk")
        os.system("sudo apt install python3-tk")

    elif sysinfo == "Windows":
        try:
            try:
                os.system("pip install tkinter")
            except:
                os.system("pip3 install tkinter")
        except:
            print("GodZilla ne parvient pas à installer Tkinter.")
            print("Vous pouvez quand même utiliser la version ligne de commande.")
        
        time.sleep(5)
        
    
    else:
        print("Choix introuvable.")



import hashlib
import requests
import json
import webbrowser
from function import *


def present():

    print("""

      ________           ._____________.__.__  .__          
     /  _____/  ____   __| _/\____    /|__|  | |  | _____   
    /   \  ___ /  _ \ / __ |   /     / |  |  | |  | \__  \  
    \    \_\  (  <_> ) /_/ |  /     /_ |  |  |_|  |__/ __ \_
     \______  /\____/\____ | /_______ \|__|____/____(____  /
            \/            \/         \/                  \/ 
    
                       [Dev By Baki]
                          [V 2.0]

                [!] "help" to show option [!]


    """)

present()
time.sleep(1)






#DEFINIR LE HASH D'UN FICHIER
def show_hash(file_user):
    m = hashlib.md5()
    reslut = m.hexdigest()
    print("The Hash is -- > ",reslut)  




#API VIRUS TOTAL 
def scan_total(file_user):
    m = hashlib.md5()
    result = m.hexdigest()
    url = 'https://www.virustotal.com/vtapi/v2/file/scan'
    params = {'apikey': 'b7a646d7d89e708cb7fb483d070d10976cabb2a61a26cb7387ea87079b5afeda'}
    files = { 'file' : ( result, open( file_user , 'rb'))}


    response = requests.post(url, files=files, params=params)
    link = response.json()["permalink"] 
    print("Votre naviguateur va s'ouvrir a l'adresse suivante : ", link + "si il ne s'ouvre pas, veuillez directement copier coller le lien dans votre naviguateur")
    time.sleep(4)
    webbrowser.open(link)



def scan_download():
    test = os.listdir('Téléchargements')
    print(test)








def main():
    q = True
    while q:
        user = input("GodZilla -- > ")

        #BASIQUE COMMANDE

        if user == "help":
            option()
        elif user == "clear":

            if k == 1:
                os.system("clear")
            elif k == 2:
                os.system('cls')
            else:
                print("GodZilla ne reconnait pas votre OS, veuillez relancer le programme")

        elif user == "exit":
            print("Godbye !")
            time.sleep(1)
            q = False

        elif user == "info":
            print("Please Choose a language : ")
            print('French  : 1')
            print("English : 2")
            choice = input('Your Choice -- > ')
            if choice == "1":
                information_godzilla_fr()
            elif choice == "2":
                information_godzilla_agl()
            else:
                print("Error, try again")
        
        elif user == "banner":
            present()


        #OPTION GODZILLA
        elif user == "hash":
            file_user = str(input('Name Of The File -- > '))
            show_hash(file_user)
        
        elif user == "scan":
            file_user = str(input("Name Of The File -- > "))
            scan_total(file_user)
        
        elif user == "gui":
            print("Starting GodZilla Gui . . .")
            time.sleep(1)
            os.system("python3 main_gui_v2.py")
        
        elif user == "analyse":
            scan_download()
               

        else:
            print("GodZilla -- > Commande Introuvable")




#DETECTION OS


if sysinfo == "Linux":
    k = 1
    print("GodZilla à detecté votre os : " + sysinfo)
    print("Vous êtes maintenant prêt à utiliser GodZilla !\n ")
    time.sleep(2)
    main()
elif sysinfo == "Windows":
    k = 2
    print("GodZilla à detecté votre os : " + sysinfo)
    print("Vous êtes maintenant prêt à utiliser GodZilla ! \n")
    time.sleep(2)
    main()
else:
    print("Votre choix est indisponible, veuillez relancer GodZilla.")