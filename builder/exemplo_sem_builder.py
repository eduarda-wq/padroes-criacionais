class Lanche:
    def __init__(self, pao, carne, salada, molho, bebida):
        self.pao = pao
        self.carne = carne
        self.salada = salada
        self.molho = molho
        self.bebida = bebida

    def __str__(self):
        return f"Lanche: {self.pao}, {self.carne}, {self.salada}, {self.molho}, {self.bebida}"

# Uso sem Builder
lanche1 = Lanche("francês", "hambúrguer", "alface", "maionese", "refrigerante")
print("Sem Builder:", lanche1)
