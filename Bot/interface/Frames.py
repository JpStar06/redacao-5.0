import customtkinter as ctk
from Bot.interface.Themes import ChangerMode , CommunButton
from Bot.services.TextServices import GetInfos
from Bot.services.InputsServices import MouseTracker
from Bot.services.WriterServices import WriterFunction

class MainTabView(ctk.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.tracker = MouseTracker(on_click_callback=self.OnCoordinateCaptured, on_stop_callback=self.OnTrackerStopped)

        self.configure(anchor="w", segmented_button_selected_color=("#18669A", "#5A189A"), segmented_button_selected_hover_color=("#042547", "#3c096c"), segmented_button_unselected_hover_color=("#042547", "#3c096c"), text_color=("#FFFFFF", "#FFFFFF"))
        # create tabs
        self.add("Home")
        self.add("Config")
        self.tab("Home").grid_columnconfigure(0, weight=1)
        self.tab("Home").grid_rowconfigure(0, weight=1)
        self.tab("Config").grid_columnconfigure(0, weight=0)
        self.tab("Config").grid_columnconfigure(1, weight=1)

        self.HomeTextBoxMain = ctk.CTkTextbox(master=self.tab("Home"), font=("Segoe UI", 14), width=400, corner_radius=15, activate_scrollbars=True, border_width=1, border_color="#3A3A3A")
        self.HomeTextBoxMain.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.HomeTextBoxMain.insert("0.0", "escreva algo")
        self.HomeStartWriteButton = ctk.CTkButton(master=self.tab("Home"), text="Start write", command=self.StartWriter, **CommunButton)
        self.HomeStartWriteButton.grid(row=4, column=0, columnspan=2, pady=10, padx=10, sticky="ew")

        self.ConfigSpeedWriteLabael = ctk.CTkLabel(master=self.tab("Config"), text="velocidade média de escrita:", font=("Segoe UI", 20, "bold"), fg_color="transparent", anchor="nw")
        self.ConfigSpeedWriteLabael.grid(row=0, column=0, padx=(20, 10), pady= 20, sticky="w")
        self.ConfigSpeedWriteEntry = ctk.CTkEntry(master=self.tab("Config"), fg_color="transparent")
        self.ConfigSpeedWriteEntry.grid(row= 0, column=1, padx=(0, 20), pady=20, sticky="w")
        self.ConfigCaptureClickButton = ctk.CTkButton(master=self.tab("Config"), text="Capturar Posição do Clique", command=self.HandleButtonPress, **CommunButton)
        self.ConfigCaptureClickButton.grid(row=1, column=0, columnspan=2, padx=(20, 10), pady=10, sticky="w")
        self.ConfigStatusClickLabel = ctk.CTkLabel(master=self.tab("Config"), text=f"(X:  | Y: )", font=("Segoe UI", 20, "bold"))
        self.ConfigStatusClickLabel.grid(row=1, column=1, columnspan=2, padx=(0, 20), pady=5, sticky="w")
        self.ConfigChangerTheme = ctk.CTkButton(master=self.tab("Config"), text="Mudar Tema", command=ChangerMode, **CommunButton)
        self.ConfigChangerTheme.grid(row=2, column=0, columnspan=2, padx=20, pady=20, sticky="w")

    def StartWriter(self):
        text = self.HomeTextBoxMain.get("1.0", "end-1c")
        coords = self.tracker.VerifyCoord()
        speed = self.ConfigSpeedWriteEntry.get()

        infos = GetInfos(text, coords, speed)

        if infos is None:
            return
        text, coords, speed = infos
        WriterFunction.write(text, coords, speed)
    
    def HandleButtonPress(self):
        if not self.tracker.active:
            self.ConfigCaptureClickButton.configure(text="contando...", **CommunButton)
            self.tracker.Start(self)
        else:
            self.tracker.Stop()

    def OnCoordinateCaptured(self, x, y):
        self.after(0, lambda: self.ConfigStatusClickLabel.configure(text=f"(X: {x} | Y: {y})"))
        self.ConfigCaptureClickButton.configure(text="Capturar Posição do Clique", **CommunButton)

    def OnTrackerStopped(self):
        self.after(0, lambda: self.ConfigCaptureClickButton.configure(text="Capturar Posição do Clique", **CommunButton))

class TiTleFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.label = ctk.CTkLabel(master=self, text="Bot redação 5.0", font=("Segoe UI", 40, "bold"), fg_color="transparent", anchor="center")
        self.label.grid(row=0, column=0, padx= 20, pady= 20, sticky="nsew")