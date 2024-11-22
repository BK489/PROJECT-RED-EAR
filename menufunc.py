#here are the functions for the menubar
from tkinter import *
from tkinter.ttk import *
import webbrowser

def aboutpressed():
    try:
        with open("about.txt", "r") as file:
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
        with open("licence-info.txt", "r") as file:
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