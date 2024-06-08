class Usuario:
    def __init__(self, nome, cpf, data_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento

class Conta:
    def __init__(self, usuario):
        self.usuario = usuario
        self.saldo = 0.0
        self.depositos = []
        self.saques = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            print(f'Depósito de R$ {valor:.2f} realizado com sucesso.')
        else:
            print('O valor do depósito deve ser positivo.')

    def extrato(self):
        extrato = ""
        if not self.depositos and not self.saques:
            extrato = "Não foram realizadas movimentações."
        else:
            for deposito in self.depositos:
                extrato += f'Depósito: R$ {deposito:.2f}\n'
            for saque in self.saques:
                extrato += f'Saque: R$ {saque:.2f}\n'
        
        print("\n================ EXTRATO ================")
        print(f"Titular: {self.usuario.nome}")
        print(f"CPF: {self.usuario.cpf}")
        print(f"Data de Nascimento: {self.usuario.data_nascimento}")
        print(extrato)
        print(f"\nSaldo: R$ {self.saldo:.2f}")
        print("==========================================")

class ContaCorrente(Conta):
    def __init__(self, usuario):
        super().__init__(usuario)
        self.saques_diarios = 0

    def sacar(self, valor):
        if self.saques_diarios >= 3:
            print('Limite de saques diários atingido.')
        elif valor > 500:
            print('O valor máximo para saque é R$ 500,00.')
        elif valor > self.saldo:
            print('Saldo insuficiente.')
        else:
            self.saldo -= valor
            self.saques.append(valor)
            self.saques_diarios += 1
            print(f'Saque de R$ {valor:.2f} realizado com sucesso.')

    def resetar_saques_diarios(self):
        self.saques_diarios = 0

class ContaPoupanca(Conta):
    def sacar(self, valor):
        if valor > self.saldo:
            print('Saldo insuficiente.')
        else:
            self.saldo -= valor
            self.saques.append(valor)
            print(f'Saque de R$ {valor:.2f} realizado com sucesso.')

def criar_usuario():
    nome = input("Digite o nome do usuário: ")
    cpf = input("Digite o CPF do usuário: ")
    data_nascimento = input("Digite a data de nascimento do usuário (dd/mm/aaaa): ")
    return Usuario(nome, cpf, data_nascimento)

def criar_conta(usuario):
    tipo_conta = input("Escolha o tipo de conta a ser criada:\n[c] Conta Corrente\n[p] Conta Poupança\n=> ").lower()
    if tipo_conta == 'c':
        return ContaCorrente(usuario)
    elif tipo_conta == 'p':
        return ContaPoupanca(usuario)
    else:
        print("Opção inválida. Tente novamente.")
        return criar_conta(usuario)

def main():
    usuario = criar_usuario()
    conta = criar_conta(usuario)
    menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

    while True:
        opcao = input(menu).lower()

        if opcao == 'd':
            valor = float(input("Digite o valor a ser depositado: R$ "))
            conta.depositar(valor)
        
        elif opcao == 's':
            valor = float(input("Digite o valor a ser sacado: R$ "))
            conta.sacar(valor)
        
        elif opcao == 'e':
            conta.extrato()
        
        elif opcao == 'q':
            print("Saindo do sistema. Até logo!")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
