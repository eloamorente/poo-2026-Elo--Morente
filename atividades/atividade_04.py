# atividade 1
class Veiculo:
    def __init__(self, marca, modelo, valor_diaria):
        self.marca = marca
        self.modelo = modelo
        self.__valor_diaria = valor_diaria

    def get_valor_diaria(self):
        return self.__valor_diaria

    def calcular_aluguel(self, dias):
        return self.get_valor_diaria() * dias


# atividade 2
class Carro(Veiculo):
    def __init__(self, marca, modelo, valor_diaria, portas):
        super().__init__(marca, modelo, valor_diaria)
        self.portas = portas

    def calcular_aluguel(self, dias):
        return super().calcular_aluguel(dias)