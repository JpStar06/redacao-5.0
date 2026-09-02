from pynput import mouse
from Bot.services.MenssagesBoxes import MessageBox


class MouseTracker:
    def __init__(self, on_click_callback, on_stop_callback):
        self.x = None
        self.y = None
        self.on_click_callback = on_click_callback
        self.on_stop_callback = on_stop_callback
        self.active = False

    def Start(self, widget):
        if not self.active:
            self.active = True
            self._countdown(widget, 3)

    def _countdown(self, widget, seconds):
        if not self.active:
            return

        if seconds > 0:
            widget.ConfigStatusClickLabel.configure(text=f"Posicione o mouse | capturando em {seconds}")
            widget.after(1000, lambda: self._countdown(widget, seconds - 1))
        else:
            self.x = widget.winfo_pointerx()
            self.y = widget.winfo_pointery()

            self.on_click_callback(self.x, self.y)
            self.Stop()

    def VerifyCoord(self):
        if self.x is not None and self.y is not None:
            return self.x , self.y
        else:
            return None

    def Stop(self):
        self.active = False
        self.on_stop_callback()