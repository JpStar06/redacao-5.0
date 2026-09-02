from CTkMessagebox import CTkMessagebox

class MessageBox:
    def Sucess(TextMsgBox):
        CTkMessagebox(title="Sucesso", message=TextMsgBox, icon="check")

    def Fail(TextMsgBox):
        CTkMessagebox(title="Falha!", message=TextMsgBox, icon="cancel")