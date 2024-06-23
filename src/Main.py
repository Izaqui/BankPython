from abc import ABC, abstractmethod
from datetime import date

class Historico:
    def __init__(self):
        self.transacoes = []
    
    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        conta.saldo += self.valor
        conta.historico.adicionar_transacao(self)

class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        conta.saldo -= self.valor
        conta.historico.adicionar_transacao(self)

class Conta:
    def __init__(self, cliente, numero, agencia):
        self.saldo = 0.0
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = Historico()

    def saldo(self):
        return self.saldo
    
    def nova_conta(cliente, numero, agencia):
        return Conta(cliente, numero, agencia)
    
    def sacar(self, valor):
        if valor > self.saldo:
            return False
        saque = Saque(valor)
        saque.registrar(self)
        return True
    
    def depositar(self, valor):
        deposito = Deposito(valor)
        deposito.registrar(self)
        return True

class ContaCorrente(Conta):
    def __init__(self, cliente, numero, agencia, limite, limite_saques):
        super().__init__(cliente, numero, agencia)
        self.limite = limite
        self.limite_saques = limite_saques
        self.saques_diarios = 0

    def sacar(self, valor):
        if self.saques_diarios >= self.limite_saques:
            print('Limite de saques diários atingido.')
            return False
        if valor > self.limite:
            print('O valor máximo para saque é R$ 500,00.')
            return False
        if super().sacar(valor):
            self.saques_diarios += 1
            return True
        return False

    def resetar_saques_diarios(self):
        self.saques_diarios = 0

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
    
    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, endereco, cpf, nome, data_nascimento):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

def criar_usuario():
    nome = input("Digite o nome do usuário: ")
    cpf = input("Digite o CPF do usuário: ")
    data_nascimento = input("Digite a data de nascimento do usuário (dd/mm/aaaa): ")
    endereco = input("Digite o endereço do usuário: ")
    return PessoaFisica(endereco, cpf, nome, data_nascimento)

def criar_conta(cliente):
    numero = int(input("Digite o número da conta: "))
    agencia = input("Digite a agência da conta: ")
    tipo_conta = input("Escolha o tipo de conta a ser criada:\n[c] Conta Corrente\n[p] Conta Poupança\n=> ").lower()
    if tipo_conta == 'c':
        limite = float(input("Digite o limite da conta corrente: "))
        limite_saques = int(input("Digite o limite de saques diários: "))
        return ContaCorrente(cliente, numero, agencia, limite, limite_saques)
    elif tipo_conta == 'p':
        return Conta(cliente, numero, agencia)
    else:
        print("Opção inválida. Tente novamente.")
        return criar_conta(cliente)

def main():
    usuario = criar_usuario()
    conta = criar_conta(usuario)
    usuario.adicionar_conta(conta)
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
            conta.historico.extrato()
        
        elif opcao == 'q':
            print("Saindo do sistema. Até logo!")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
