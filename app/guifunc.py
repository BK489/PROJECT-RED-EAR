#here are the functions for gui operation such as menubar and entry box 
from tkinter import *
from tkinter.ttk import *
import webbrowser

def aboutpressed():
    try:
        with open("assets/about.txt", "r") as file:
            license_text = file.read()
    except FileNotFoundError:
        license_text = "about.txt not found, please check location in directory"

    license_window = Toplevel()
    license_window.title("About")
    license_window.geometry("560x220")
    license_window.resizable(False, False)
    
    textlabel = Label(license_window, text=license_text, font=("terminal", 10))
    textlabel.place(x=-2, y=0)
    textlabel.pack(expand=True, fill="both", padx=10, pady=10)
    return 0

def documentationpressed():
    url = "https://github.com/BK489/PROJECT-RED-EAR"
    webbrowser.open(url)
    return 0

def licencepressed():
    try:
        with open("assets/licence-info.txt", "r") as file:
            license_text = file.read()
    except FileNotFoundError:
        license_text = "licence-info.txt not found, please check location in directory"

    license_window = Toplevel()
    license_window.title("License Agreement")
    license_window.geometry("620x300")
    license_window.resizable(False, False)
    
    textlabel = Label(license_window, text=license_text, font=("terminal", 10))
    textlabel.place(x=-2, y=0)
    textlabel.pack(expand=True, fill="both", padx=10, pady=10)

    return 0

#func for grey infotext on entry fields before input
def dir_click(event):
    if event.widget.get() == "Download Folder...":
        event.widget.delete(0, "end") # delete all the text in the entry
        event.widget.insert(0, '') #Insert blank for user input
        event.widget.config(foreground = 'black')
    
def dir_out(event):
    if event.widget.get() == '':
        event.widget.insert(0, "Download Folder...")
        event.widget.config(foreground = 'grey')

def vid_click(event):
    if event.widget.get() == "Insert Video URL...":
        event.widget.delete(0, "end") 
        event.widget.insert(0, '') 
        event.widget.config(foreground = 'black')
    
def vid_out(event):
    if event.widget.get() == '':
        event.widget.insert(0, "Insert Video URL...")
        event.widget.config(foreground = 'grey')

def channel_click(event):
    if event.widget.get() == "Insert Channel URL...":
        event.widget.delete(0, "end") 
        event.widget.insert(0, '') 
        event.widget.config(foreground = 'black')
    
def channel_out(event):
    if event.widget.get() == '':
        event.widget.insert(0, "Insert Channel URL...")
        event.widget.config(foreground = 'grey')