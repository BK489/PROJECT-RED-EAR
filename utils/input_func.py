#this file will hold funciton for all input fields and related buttons.

from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog, messagebox
import os

#browse button
def browsedir (inputfield, label):
    filename = filedialog.askdirectory()
    inputfield.delete(0, "end") 
    inputfield.insert(0, '')
    inputfield.config(foreground="black")
    inputfield.insert(0, filename)
    #config search and change attatcehd label 
    label.config(text="check for config here") ##logic search herebut decide on how da json gonna work first!!!think u can do this now

#gen config button
def genconfig(inputfield, label):
    entrypath = inputfield.get()

    if os.path.isdir(entrypath):
        if messagebox.askokcancel("Warning", "Config file will be generated in selected directory"):
            try:
                file = open(os.path.join(entrypath, "PROJECT_RED_EAR.json"), "x")
            except:
                label.config(text="Config File Already Exists")
            else:
                file.close()
                label.config(text="Config File Generated")
    else:
        label.config(text="Invalid Folder Directory Entered")
    #gotta create a list of dicts to be written to a json file!!!
    #keep a top level data like file creation date, last edited date and working dir maybe even size 

