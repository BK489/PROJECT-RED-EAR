#this file will hold function for all input fields and related buttons.

from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog, messagebox
import os, json

from utils.config_func import load_config, config_exists

#browse button
def browsedir (inputfield, label):
    dirpath = filedialog.askdirectory()
    inputfield.delete(0, "end") 
    inputfield.insert(0, '')
    inputfield.config(foreground="black")
    inputfield.insert(0, dirpath)
    #if config file exists loadconfig() and update label with config info
    if config_exists(dirpath):
        label.config(text="Config File Found and Loaded")
        load_config() ##########
    else:
        label.config(text="No Config File Found - Press Generate")

#check config and load once text entered alternative to using browse button
def dir_confcheck(inputfield, label):
    entrypath = inputfield.get()
    if config_exists(entrypath):
        load_config()##########
        label.config(text="Config File Found and Loaded")
    elif os.path.isdir(entrypath):
        label.config(text="No Config File Found - Press Generate")
    elif entrypath == "": 
        label.config(text="Select Folder")
    elif entrypath == "Download Folder...":
        label.config(text="Select Folder")
    else:
        label.config(text="Invalid Folder Path")

#gen config button
def genconfig(inputfield, label):
    entrypath = inputfield.get()

    if os.path.isdir(entrypath):
        if messagebox.askokcancel("Warning", "Config file will be generated in selected directory"):
            try:
                file = open(os.path.join(entrypath, "RED-EAR-Config.json"), "x")
            except:
                label.config(text="Config File Already Exists")
            else:
                file.close()
                label.config(text="Config File Generated")
    else:
        label.config(text="Invalid Folder Directory Entered")
    #gotta create a list of dicts to be written to a json file!!!
    #keep a top level data like file creation date, last edited date and working dir maybe even size 

    data = {
        "file" : os.path.join(entrypath, "RED-EAR-Config.json"),
        "totalvids" : 0,
        "channels" : [], #list of channels added with another videos inside
        "videos" : [] #list of loose vids
    }
    with open(os.path.join(entrypath, "RED-EAR-Config.json"), "w") as f:
        json.dump(data, f)          

    load_config()#######
    

def add_vid():
    pass

def add_chan():
    pass

def start_button():
    pass

def stop_button():
    pass