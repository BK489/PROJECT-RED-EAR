#packages
from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
#my stuff
from styles.gui_style import load_style
from app.guifunc import ( 
    aboutpressed, documentationpressed, licencepressed, 
    dir_click, dir_out, vid_click, vid_out, channel_click, channel_out 
)


class App:
    def __init__(self):
        #main window
        self.root = Tk()
        self.root.title("RED-EAR v1.0.0-ALPHA")
        self.root.geometry("600x400")
        self.root.resizable(False, False)
        self.root.iconbitmap(False, "assets/red-ear-ico.ico")
        
        #background image
        img = Image.open("assets/red-ear-background.png")
        background_image = ImageTk.PhotoImage(img.resize((600, 400)))
        background_label = Label(self.root, image=background_image)
        background_label.image = background_image  # Keep a reference to avoid garbage collection
        background_label.place(x=-1, y=0)

        #menu bar
        self.setup_menu()
        #topframe
        self.setup_widgets()

        #load ttk style
        load_style()

    def setup_menu(self):
        #Sets up the menu bar with dropdown menus.
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

    def setup_widgets(self):
        #sets up widgets on application page
        #title
        title_label = Label(self.root, text="RED-EAR V1.0.0-ALPHA", font="terminal")
        title_label.place(x=175, y=15)

        #download dir stuff
        directory_entry = Entry(self.root, font="terminal 11", width=60)    
        directory_entry.place(x=30, y=53)
        directory_entry.insert(0, "Download Folder...")
        directory_entry.config(foreground="grey")
        directory_entry.bind('<FocusIn>', dir_click)
        directory_entry.bind('<FocusOut>', dir_out)    

        directory_label = Label(self.root, font="terminal 11", text="no config found")
        directory_label.place(x=30,y=72)

        choose_dir_button = Button(self.root, text="Choose Download Folder", style="Custom.TButton", command=lambda: print("choose dir pressed"))
        choose_dir_button.place(x=370, y=50)
        
        #single video URL stuff
        vid_url_entry = Entry(self.root, font="terminal 11", width=60)
        vid_url_entry.place(x=30, y=95)
        vid_url_entry.insert(0, "Insert Video URL...")
        vid_url_entry.config(foreground="grey")
        vid_url_entry.bind('<FocusIn>', vid_click)
        vid_url_entry.bind('<FocusOut>', vid_out)  

        vid_url_label = Label(self.root, font="terminal 11", text="Invalid Video URL")
        vid_url_label.place(x=30,y=114)

        vid_url_button = Button(self.root, text="Add Video URL", style="Custom.TButton", command=lambda: print("add vid pressed"))
        vid_url_button.place(x=370, y=92)

        #channel URL stuff
        channel_url_entry = Entry(self.root, font="terminal 11", width=60)
        channel_url_entry.place(x=30, y=137)
        channel_url_entry.insert(0, "Insert Channel URL...")
        channel_url_entry.config(foreground="grey")
        channel_url_entry.bind('<FocusIn>', channel_click)
        channel_url_entry.bind('<FocusOut>', channel_out)  

        channel_url_label = Label(self.root, font="terminal 11", text="Invalid Channel URL")
        channel_url_label.place(x=30,y=156)

        channel_url_button = Button(self.root, text="Add Channel URL", style="Custom.TButton", command=lambda: print("add channel pressed"))
        channel_url_button.place(x=370, y=134)

    def run(self):
        #Runs the Tkinter main loop.
        self.root.mainloop()
