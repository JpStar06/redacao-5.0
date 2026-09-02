from Bot.services import MenssagesBoxes
import pyautogui as pt
from Bot.services import TextServices

class WriterFunction:
    @staticmethod
    def write(text, coords, speed):
        x, y = coords

        pt.click(x, y)
        pt.write(text, interval=speed)