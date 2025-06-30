class Botao:
    def renderizar(self):
        print("Botão padrão")

class BotaoWindows(Botao):
    def renderizar(self):
        print("Botão estilo Windows")

class BotaoMac(Botao):
    def renderizar(self):
        print("Botão estilo Mac")

def criar_interface(sistema):
    if sistema == "windows":
        botao = BotaoWindows()
    elif sistema == "mac":
        botao = BotaoMac()
    else:
        botao = Botao()
    
    botao.renderizar()

# Teste
criar_interface("windows")