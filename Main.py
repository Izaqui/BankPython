class Banco:
    #iniciando
    def __init__(self):
        self.saldo = 0.0
        self.depositos = []
        self.saques = []
        self.saques_diarios = 0
    
    #Metodo de deposito
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            print(f'Depósito de R$ {valor:.2f} realizado com sucesso.')
        else:
            print('O valor do depósito deve ser positivo.')
    #Metodo de Saque
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
    #Metodo para impressão do extrato
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
        print(extrato)
        print(f"\nSaldo: R$ {self.saldo:.2f}")
        print("==========================================")
    #Metodo para saida do sistema
    def resetar_saques_diarios(self):
        self.saques_diarios = 0
#Metodos principal e menu
def main():
    banco = Banco()
    menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

    while True: #Loop
        opcao = input(menu).lower()

        if opcao == 'd':
            valor = float(input("Digite o valor a ser depositado: R$ "))
            banco.depositar(valor)
        
        elif opcao == 's':
            valor = float(input("Digite o valor a ser sacado: R$ "))
            banco.sacar(valor)
        
        elif opcao == 'e':
            banco.extrato()
        
        elif opcao == 'q':
            print("Saindo do sistema. Até logo!")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
