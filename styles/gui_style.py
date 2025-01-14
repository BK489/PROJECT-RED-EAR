from tkinter.ttk import Style

def load_style():

    s = Style()
    s.theme_use('default') #Available themes: ('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')
    #configure for general, map for dynamic

    #buttons
    s.configure(
    "Custom.TButton",
    font=("Terminal", 11),
    background="firebrick1",
    foreground="white",
    )
    s.map(
    "Custom.TButton",
    background=[
        ("active", "firebrick2"),
        ("pressed", "firebrick4"),
    ],
    foreground=[
        ("disabled", "gray"),
    ],
    )

    #treeview - table
    s.configure(
        "Custom.Treeview.Heading",
        font=("Terminal", 11),
        background="firebrick1",
        foreground="white",
    )
    s.map(
        "Custom.Treeview.Heading",
    background=[
        ("active", "firebrick2"),
        ("pressed", "firebrick4"),
    ],
    foreground=[
        ("disabled", "gray"),
    ], 
    )

    #progressbar
    s.configure(
        "Custom.Horizontal.TProgressbar",
        font=("Terminal", 11),
        background="firebrick1",
        foreground="white",
    )


    return s
