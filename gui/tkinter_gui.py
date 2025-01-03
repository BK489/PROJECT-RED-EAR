from tkinter import *
from tkinter.ttk import *
from styles.gui_style import load_style
from gui.menufunc import aboutpressed, documentationpressed, licencepressed

class App:
    def __init__(self):
        #main window
        self.root = Tk()
        self.root.title("RED-EAR v1.0-ALPHA")
        self.root.geometry("450x250")
        self.root.resizable(False, False)
        self.root.iconbitmap(False, "assets/red-ear-ico.ico")
        
        #background image
        background_image = PhotoImage(file="assets/red-ear-background.png")
        background_label = Label(self.root, image=background_image)
        background_label.image = background_image  # Keep a reference to avoid garbage collection
        background_label.place(x=-2, y=0)

        #menu bar
        self.setup_menu()

        #load ttk style
        load_style()

    def setup_menu(self):
        """Sets up the menu bar with dropdown menus."""
        menu_bar = Menu(self.root, bg="red")

        #file dropdown
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Config", command=lambda: print("config pressed"))
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)

        #help dropdown
        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=lambda: aboutpressed())
        help_menu.add_separator()
        help_menu.add_command(label="Documentation", command=lambda: documentationpressed())
        help_menu.add_separator()
        help_menu.add_command(label="Licence", command=lambda: licencepressed())

        #add the dropdowns to the menu bar
        menu_bar.add_cascade(label="File", menu=file_menu)
        menu_bar.add_cascade(label="Help", menu=help_menu)

        self.root.config(menu=menu_bar)

    def run(self):
        """Runs the Tkinter main loop."""
        self.root.mainloop()
