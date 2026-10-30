class Veiculo:
    def __init__(self, marca, modelo, ano, preco):
        self.__marca = ""
        self.__modelo = ""
        self.__ano = 2000
        self.__preco = 0.0

        self.set_marca(marca)
        self.set_modelo(modelo)
        self.set_ano(ano)
        self.set_preco(preco)

    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo

    def get_ano(self):
        return self.__ano

    def get_preco(self):
        return self.__preco

    def set_marca(self, marca):
        if isinstance(marca, str) and len(marca.strip()) >= 2:
            self.__marca = marca.strip()
        else:
            print("Erro: a marca deve ter pelo menos 2 caracteres.")

    def set_modelo(self, modelo):
        if isinstance(modelo, str) and len(modelo.strip()) >= 2:
            self.__modelo = modelo.strip()
        else:
            print("Erro: o modelo deve ter pelo menos 2 caracteres.")

    def set_ano(self, ano):
        if isinstance(ano, int) and not isinstance(ano, bool) and 1886 <= ano <= 2026:
            self.__ano = ano
        else:
            print("Erro: informe um ano válido entre 1886 e 2026.")

    def set_preco(self, preco):
        if (
            isinstance(preco, (int, float))
            and not isinstance(preco, bool)
            and preco >= 0
        ):
            self.__preco = float(preco)
        else:
            print("Erro: o preço deve ser um número não negativo.")

    def apresentar(self):
        print(
            f"{self.get_marca()} {self.get_modelo()} "
            f"({self.get_ano()}) - R$ {self.get_preco():.2f}"
        )


class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, preco, portas):
        super().__init__(marca, modelo, ano, preco)
        self.portas = portas

    def apresentar(self):
        print(
            f"Carro: {self.get_marca()} {self.get_modelo()}, "
            f"ano {self.get_ano()}, {self.portas} portas, "
            f"preço R$ {self.get_preco():.2f}"
        )


class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, preco, cilindradas):
        super().__init__(marca, modelo, ano, preco)
        self.cilindradas = cilindradas

    def apresentar(self):
        print(
            f"Moto: {self.get_marca()} {self.get_modelo()}, "
            f"ano {self.get_ano()}, {self.cilindradas} cilindradas, "
            f"preço R$ {self.get_preco():.2f}"
        )


if __name__ == "__main__":
    veiculos = [
        Carro("Toyota", "Corolla", 2024, 120000.00, 4),
        Moto("Honda", "CB 500", 2023, 40000.00, 500),
        Carro("Ford", "Mustang", 2022, 350000.00, 2),
        Moto("Yamaha", "Fazer", 2025, 25000.00, 250)
    ]

    print("=== VEÍCULOS CADASTRADOS ===")

    for veiculo in veiculos:
        veiculo.apresentar()