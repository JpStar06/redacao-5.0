#textservices.py

from Bot.services.MenssagesBoxes import MessageBox
import unicodedata

class TextProcessor:
    def __init__(self):
        self.text = ""

    def validate(self, text: str) -> str:
        self.text = ""

        for character in text:
            self.text += self._normalize_character(character)

        return self.text

    def _normalize_character(self, character: str) -> str:
        if character == "ç":
            return "c"

        if character == "Ç":
            return "C"

        normalized = unicodedata.normalize("NFD", character)

        return "".join(
            char
            for char in normalized
            if unicodedata.category(char) != "Mn"
        )

def GetInfos(Text, cords, Speed):
    if not Text.strip() or Text == "escreva algo":
        MessageBox.Fail("Insira texto")
        return
    
    if cords is None:
        MessageBox.Fail("Capture as cordenadas do clique")
        return

    try:
        SpeedInt = float(Speed.strip())

        if SpeedInt <= 0:
            MessageBox.Fail("Avelocidade média deve ser maior que 0.")
            return
        else:
            Validator = TextProcessor()
            Text = Validator.validate(Text)
            return Text, cords, SpeedInt
            
    except ValueError:
        MessageBox.Fail("Defina uma velocidade de Digitação média válida (apenas números)")