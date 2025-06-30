class Lanche:
    def __init__(self):
        self.pao = None
        self.carne = None
        self.salada = None
        self.molho = None
        self.bebida = None

    def __str__(self):
        return f"Lanche: {self.pao}, {self.carne}, {self.salada}, {self.molho}, {self.bebida}"

class LancheBuilder:
    def __init__(self):
        self.lanche = Lanche()

    def adicionar_pao(self, pao):
        self.lanche.pao = pao
        return self

    def adicionar_carne(self, carne):
        self.lanche.carne = carne
        return self

    def adicionar_salada(self, salada):
        self.lanche.salada = salada
        return self

    def adicionar_molho(self, molho):
        self.lanche.molho = molho
        return self

    def adicionar_bebida(self, bebida):
        self.lanche.bebida = bebida
        return self

    def construir(self):
        return self.lanche

# Uso com Builder
builder = LancheBuilder()
lanche2 = (builder.adicionar_pao("francês")
                  .adicionar_carne("hambúrguer")
                  .adicionar_salada("alface")
                  .adicionar_molho("maionese")
                  .adicionar_bebida("refrigerante")
                  .construir())

print("Com Builder:", lanche2)
