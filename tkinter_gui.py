#note all tk objects cannot import style 

from tkinter import *
from tkinter.ttk import *
from gui_style import load_style 
from menufunc import aboutpressed, documentationpressed, licencepressed

#make window instance and config
root = Tk()
root.title("RED-EAR v1.0-ALPHA")
root.geometry("450x250")
root.resizable(False, False)
root.iconbitmap(False, "red-ear-ico.ico")
background_image=PhotoImage(file="red-ear-background.png")
background_label = Label(root, image=background_image)
background_label.place(x=-2, y=0)

#menu bar creation and config
menu_bar = Menu(root, bg="red")
#file dropdown
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Config", command=lambda: print("config pressed"))
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
#help dropdown
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=lambda: aboutpressed())
help_menu.add_separator()
help_menu.add_command(label="Documentation", command=lambda: documentationpressed())
help_menu.add_separator()
help_menu.add_command(label="Licence", command=lambda: licencepressed())

# Add the dropdowns to the menu bar
menu_bar.add_cascade(label="File", menu=file_menu)
menu_bar.add_cascade(label="Help", menu=help_menu)

#TTK WIDGETS AFTER THIS
load_style()

root.config(menu=menu_bar)
#run application
root.mainloop()