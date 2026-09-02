import customtkinter as ctk
from Bot.interface.Themes import ChangerMode, CommunButton
from Bot.interface.Frames import MainTabView, TiTleFrame

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("test")
        self.geometry("800x600")
        self.resizable(False, False)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=3)

        self.SetTitleFrame = TiTleFrame(master=self)
        self.SetTitleFrame.grid(row=1, column=0, columnspan=2, padx=20, pady=20, sticky="nsew")

        self.SetMainTabView = MainTabView(master=self, width= 500, height=400)
        self.SetMainTabView.grid(row=2, column=0, columnspan=2, padx=20, pady=20, sticky="nsew")

def start():
    app = MainWindow()
    app.mainloop()
