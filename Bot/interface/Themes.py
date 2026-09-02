import customtkinter as ctk

is_dark_mode = True

CommunButton = {
    "fg_color" : ("#18669A", "#5A189A"),
    "hover_color": ("#042547", "#3c096c"),
    "text_color": ("#FFFFFF", "#FFFFFF")
}

def ChangerMode():
    global is_dark_mode
    if is_dark_mode:
        ctk.set_appearance_mode("light")
        is_dark_mode= False
    else:
        ctk.set_appearance_mode("dark")
        is_dark_mode = True