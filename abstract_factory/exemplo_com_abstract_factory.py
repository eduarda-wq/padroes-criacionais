from abc import ABC, abstractmethod

class Botao(ABC):
    @abstractmethod
    def renderizar(self):
        pass

class BotaoWindows(Botao):
    def renderizar(self):
        print("Botão estilo Windows")

class BotaoMac(Botao):
    def renderizar(self):
        print("Botão estilo Mac")

class UIFactory(ABC):
    @abstractmethod
    def criar_botao(self) -> Botao:
        pass

class WindowsFactory(UIFactory):
    def criar_botao(self):
        return BotaoWindows()

class MacFactory(UIFactory):
    def criar_botao(self):
        return BotaoMac()

# Código cliente
def renderizar_interface(factory: UIFactory):
    botao = factory.criar_botao()
    botao.renderizar()

# Teste
sistema = "mac"
fabrica = MacFactory() if sistema == "mac" else WindowsFactory()
renderizar_interface(fabrica)