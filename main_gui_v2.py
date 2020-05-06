from functools import partial
from tkinter import *
from tkinter.filedialog import askopenfilename
import os
import sys
import time
import hashlib
import requests
import json
import webbrowser
from PIL import Image, ImageTk
import threading
import pyperclip


def gui_scanning_file(file_user):
    m = hashlib.md5()
    result = m.hexdigest()
    url = 'https://www.virustotal.com/vtapi/v2/file/scan'
    params = {'apikey': 'b7a646d7d89e708cb7fb483d070d10976cabb2a61a26cb7387ea87079b5afeda'}
    files = { 'file' : ( result, open( file_user , 'rb'))}


    response = requests.post(url, files=files, params=params)
    link = response.json()["permalink"] 
    print("Votre naviguateur va s'ouvrir a l'adresse suivante : ", link + "si il ne s'ouvre pas, veuillez directement copier coller le lien dans votre naviguateur")
    time.sleep(2)
    webbrowser.open(link)
    



def scan_selectfileonpc():
    file = askopenfilename()
    gui_scanning_file(file)


def hash_selectfileonpc():
    file = askopenfilename()
    show_hash(file)



#DEFINIR LE HASH D'UN FICHIER
def show_hash(file_user):
    gui_hash = Tk()
    gui_hash.title=("GodZilla 2.0")
    gui_hash.minsize(300, 160)
    gui_hash.maxsize(300, 160)
    gui_hash.config(background='#41403F')

    m = hashlib.md5()
    result = m.hexdigest()

    label_title = Label(gui_hash, text="The hash is : ", font=('Courrier', 17), bg='#41403F', fg="White")
    label_title.place(x=80, y=15)
    label_hash = Label(gui_hash, text=result, font=('Courrier', 10), bg='#41403F', fg="red")
    label_hash.place(x=30, y=60)

    button_copy = Button(gui_hash, text="Copy", font=('Courrier', 10), bg="#41403F", fg="white", padx=58, pady=5,command=pyperclip.copy(result))
    button_leave = Button(gui_hash, text="Quit", font=('Courrier', 10), bg="#BC2B28", fg="black", padx=55, pady=5, command=quit)
    
    button_leave.place(x=153, y=120)
    button_copy.place(x=0, y=120)

    gui_hash.mainloop()



#CREATION ET PARAMETRE DE LA GUI
def main_gui():
    gui = Tk()
    gui.title("GodZilla V2.0")
    gui.minsize(1080, 550)
    gui.maxsize(1080, 550)
    gui.config(background='#41403F')

    #IMAGE TITLE
    canvas = Canvas(gui, width=790, height=180, bg="#41403F", highlightthickness=0)
    img = ImageTk.PhotoImage(Image.open("title.png"))
    canvas.create_image(0, 110,anchor=W, image=img)
    canvas.pack()

    #button to scan
    buton_scan = Button(gui, text="        Scan file        ", font=('Courrier', 13), bg="#3A3837", padx=90, pady=10, fg="white", command=scan_selectfileonpc)
    buton_scan.place(x=365, y=300)

    #button to start no console
    buton_start_back = Button(gui, text="      Show hash       ", font=('Courrier', 13), bg="#3A3837", padx=90, pady=10, fg="white", command=hash_selectfileonpc)
    buton_start_back.place(x=365, y=350)

    #button to quit
    buton_quit = Button(gui, text="           Quit            ", font=('Courrier', 13), bg="#BC2B28", padx=90, pady=10, fg="Black", command=quit)
    buton_quit.place(x=365, y=400)
    #TEXT AUTOR
    label_by_autor = Label(gui, text="Dev By Baki", font=('Courrier', 10), bg='#41403F', fg='white')
    label_by_autor.place(x=490, y=520)

    gui.mainloop()

th_main = threading.Thread(target=main_gui)
th_main.start()
th_main.join()