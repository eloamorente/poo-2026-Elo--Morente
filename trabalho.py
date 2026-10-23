
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
        if (
            isinstance(ano, int)
            and not isinstance(ano, bool)
            and 1886 <= ano <= 2026
        ):
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


if __name__ == "__main__":
    print("=== TESTANDO A CLASSE VEICULO ===")

    print("\n--- Teste 1: Veículo válido ---")
    veiculo_valido = Veiculo("Toyota", "Corolla", 2024, 120000.00)

    print(f"Marca: {veiculo_valido.get_marca()}")
    print(f"Modelo: {veiculo_valido.get_modelo()}")
    print(f"Ano: {veiculo_valido.get_ano()}")
    print(f"Preço: R$ {veiculo_valido.get_preco():.2f}")

    print("\n--- Teste 2: Marca inválida ---")
    veiculo_marca_invalida = Veiculo("", "Civic", 2023, 100000.00)
    print(f"Marca mantida: {veiculo_marca_invalida.get_marca()}")

    print("\n--- Teste 3: Ano inválido ---")
    veiculo_ano_invalido = Veiculo("Honda", "Civic", 1800, 100000.00)
    print(f"Ano mantido: {veiculo_ano_invalido.get_ano()}")

    print("\n--- Teste 4: Preço negativo ---")
    veiculo_preco_invalido = Veiculo("Ford", "Ka", 2020, -15000.00)
    print(f"Preço mantido: R$ {veiculo_preco_invalido.get_preco():.2f}")

    print("\n--- Teste 5: Alteração para modelo inválido ---")
    veiculo_valido.set_modelo("A")
    print(f"Modelo protegido: {veiculo_valido.get_modelo()}")

    print("\n--- Teste 6: Alteração para preço negativo ---")
    veiculo_valido.set_preco(-5000)
    print(f"Preço protegido: R$ {veiculo_valido.get_preco():.2f}")