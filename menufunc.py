#here are the functions for the menubar
from tkinter import *
from tkinter.ttk import *

def aboutpressed():
    print("aboutpressed")
    return 0

def documentationpressed():
    print("doc pressed")
    return 0

def licencepressed():
    try:
        with open("LICENCE.txt", "r") as file:
            license_text = file.read()
    except FileNotFoundError:
        license_text = "LICENCE.txt not found, please check location in directory"

    license_window = Toplevel()
    license_window.title("License Agreement")
    license_window.geometry("620x300")
    license_window.resizable(False, False)
    
    textlabel = Label(license_window, text=license_text, font=("terminal", 10))
    textlabel.place(x=-2, y=0)
    textlabel.pack(expand=True, fill="both", padx=10, pady=10)

    return 0