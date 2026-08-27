class Funcionario:
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base

    def calcular_bonus(self):
        return self.salario_base * 0.05


class Gerente(Funcionario):
    def calcular_bonus(self):
        return super().calcular_bonus() + 1000


class Vendedor(Funcionario):
    def __init__(self, nome, salario_base, total_vendas):
        super().__init__(nome, salario_base)
        self.total_vendas = total_vendas

    def calcular_bonus(self):
        return self.total_vendas * 0.10


funcionario = Funcionario("Eloá Morente", 3000)
gerente = Gerente("Ana Paula Morente", 5000)
vendedor = Vendedor("Fabio Morente", 2500, 20000)

print("Funcionário:", funcionario.nome)
print(f"Bônus: R$ {funcionario.calcular_bonus():.2f}")

print("\nGerente:", gerente.nome)
print(f"Bônus: R$ {gerente.calcular_bonus():.2f}")

print("\nVendedor:", vendedor.nome)
print(f"Bônus: R$ {vendedor.calcular_bonus():.2f}")