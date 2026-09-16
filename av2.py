class Veiculo:
    def __init__(self, modelo: str, placa: str, valor_diaria: float):
        self.__modelo = modelo
        self.__placa = placa
        self.valor_diaria = valor_diaria  # Utiliza o setter para validação

    @property
    def modelo(self) -> str:
        return self.__modelo

    @property
    def placa(self) -> str:
        return self.__placa

    @property
    def valor_diaria(self) -> float:
        return self.__valor_diaria

    @valor_diaria.setter
    def valor_diaria(self, valor: float):
        if valor <= 0:
            raise ValueError("O valor da diária deve ser maior que zero.")
        self.__valor_diaria = valor

    def calcular_aluguel(self, dias: int) -> float:
        if dias <= 0:
            raise ValueError("A quantidade de dias deve ser maior que zero.")
        return self.__valor_diaria * dias

    def __str__(self):
        return f"Modelo: {self.__modelo} | Placa: {self.__placa} | Diária: R$ {self.__valor_diaria:.2f}"


class Carro(Veiculo):
    def __init__(self, modelo: str, placa: str, valor_diaria: float, portas: int):
        super().__init__(modelo, placa, valor_diaria)
        if portas <= 0:
            raise ValueError("O número de portas deve ser maior que zero.")
        self.__portas = portas

    @property
    def portas(self) -> int:
        return self.__portas

    # Sobrescrita com regra de negócio do Carro (+ R$ 50 de taxa)
    def calcular_aluguel(self, dias: int) -> float:
        valor_base = super().calcular_aluguel(dias)
        taxa_limpeza = 50.0
        return valor_base + taxa_limpeza

    def __str__(self):
        return f"[CARRO] {super().__str__()} | Portas: {self.__portas}"


class Moto(Veiculo):
    def __init__(self, modelo: str, placa: str, valor_diaria: float, cilindradas: int):
        super().__init__(modelo, placa, valor_diaria)
        if cilindradas <= 0:
            raise ValueError("A cilindrada deve ser maior que zero.")
        self.__cilindradas = cilindradas

    @property
    def cilindradas(self) -> int:
        return self.__cilindradas

    def calcular_aluguel(self, dias: int) -> float:
        valor_base = super().calcular_aluguel(dias)
        desconto = 0.10
        return valor_base * (1 - desconto)

    def __str__(self):
        return f"[MOTO]  {super().__str__()} | Cilindradas: {self.__cilindradas}cc"


def cadastrar_veiculo(frota: list):
    print("\n--- CADASTRO DE VEÍCULO ---")
    print("1 - Carro")
    print("2 - Moto")
    
    tipo = input("Escolha o tipo de veículo: ").strip()
    if tipo not in ["1", "2"]:
        raise ValueError("Opção de tipo inválida. Escolha 1 ou 2.")

    modelo = input("Modelo: ").strip()
    if not modelo:
        raise ValueError("O modelo não pode ser vazio.")

    placa = input("Placa: ").strip().upper()
    if not placa:
        raise ValueError("A placa não pode ser vazia.")

    for v in frota:
        if v.placa == placa:
            raise ValueError("Já existe um veículo cadastrado com esta placa.")

    valor_diaria = float(input("Valor da diária (R$): "))

    if tipo == "1":
        portas = int(input("Quantidade de portas: "))
        veiculo = Carro(modelo, placa, valor_diaria, portas)
    else:
        cilindradas = int(input("Cilindradas (cc): "))
        veiculo = Moto(modelo, placa, valor_diaria, cilindradas)

    frota.append(veiculo)
    print(f"\n{veiculo.modelo} cadastrado com sucesso!")


def listar_e_calcular_aluguel(frota: list):
    if not frota:
        print("\nA frota está vazia no momento.")
        return

    print("\n--- FROTA CADASTRADA ---")
    for i, veiculo in enumerate(frota, start=1):
        print(f"{i}. {veiculo}")

    dias = int(input("\nInforme a quantidade de dias para a simulação do aluguel: "))
    if dias <= 0:
        raise ValueError("A quantidade de dias deve ser maior que zero.")

    print(f"\n--- SIMULAÇÃO DE ALUGUEL ({dias} DIAS) ---")
    for veiculo in frota:
        total = veiculo.calcular_aluguel(dias)
        print(f"{veiculo.modelo} ({veiculo.placa}): R$ {total:.2f}")


def buscar_veiculo_por_placa(frota: list):
    if not frota:
        print("\nA frota está vazia no momento.")
        return

    placa_busca = input("Digite a placa do veículo: ").strip().upper()
    
    veiculo_encontrado = None
    for veiculo in frota:
        if veiculo.placa == placa_busca:
            veiculo_encontrado = veiculo
            break

    if not veiculo_encontrado:
        raise KeyError(f"Veículo com a placa '{placa_busca}' não foi encontrado.")

    print(f"\nVeículo Encontrado: {veiculo_encontrado}")
    dias = int(input("Informe os dias para locação: "))
    total = veiculo_encontrado.calcular_aluguel(dias)
    print(f"Valor total da locação: R$ {total:.2f}")


def main():
    frota = []

    while True:
        print("\n==========================================")
        print("    SISTEMA DE GESTÃO DE FROTA - VIDA TECH")
        print("==========================================")
        print("1 - Cadastrar Veículo")
        print("2 - Listar Frota e Simular Aluguel")
        print("3 - Buscar Veículo por Placa e Calcular Aluguel")
        print("4 - Sair")
        print("==========================================")

        try:
            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                cadastrar_veiculo(frota)
            elif opcao == "2":
                listar_e_calcular_aluguel(frota)
            elif opcao == "3":
                buscar_veiculo_por_placa(frota)
            elif opcao == "4":
                print("\nEncerrando o sistema... Até logo!")
                break
            else:
                raise ValueError("Opção de menu inválida. Escolha entre 1 e 4.")

        except ValueError as e:
            print(f"\n Erro de Entrada/Validação: {e}")
        except KeyError as e:
            print(f"\n Erro de Busca: {e}")
        except Exception as e:
            print(f"\nOcorreu um erro inesperado: {e}")
        else:

            pass
        finally:
            pass


if __name__ == "__main__":
    main()