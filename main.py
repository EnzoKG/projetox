from tkinter import *

# classe para configuração de janela
class Application:
    def __init__(self, master=None):
        # Frame/container
        self.widget1 = Frame(master)
        self.widget1.pack()
        # Mensagem do container
        self.msg = Label(self.widget1, text="Primeiro widget")
        self.msg["font"] = ("Verdana", "10", "italic", "bold")
        self.msg.pack()
        # Botao
        self.btn = Button(self.widget1)
        self.btn["text"] = "Sair"
        self.btn["font"] = ("Calibri", "10")
        self.btn["width"] = 10
        self.btn.bind("<Button-1>", self.mudarTexto)
        self.btn.pack()

    def mudarTexto(self, event):
        if self.msg["text"] == "Primeiro widget":
            self.msg["text"] = "O botao recebeu um clique"
        else:
            self.msg["text"] = "Primeiro widget"

root = Tk()
Application(root)
root.mainloop()