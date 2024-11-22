from tkinter.ttk import Style

def load_style():

    s = Style()
    s.theme_use('classic') #Available themes: ('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')
    #configure for general, map for dynamic

    #menubar
    s.configure( 
        "custom.TMenu",
        background="#ff6666",
        foreground="black",
        padding=5
    )
    s.map(
        "custom.menubar",
        background=[("active", ""), ("disabled", "lightgrey")],
        foreground=[("disabled", "grey")]
    )

    return s
