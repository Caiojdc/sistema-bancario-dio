import os
clear = lambda: os.system('cls')
clear()

menu = """
[d] DEPÓSITO
[s] SACAR
[e] EXTRATO
[q] SAIR

ESCOLHA O SERVIÇO: """

saldo = 0 
limite = 500 
extrato = ""
numeros_saque = 0
limites_saque = 3

print("====== BEM VINDO AO JOSÉ BANK ======")
while True:
    opção = input(menu)

    if opção == "d" :
        clear()
        print("=========== Depósito ===========\n")
        valor_dep = float(input("Qual valor deseja depositar? R$ "))
        if valor_dep <= 0:
            print("Valor digitado inválido. Digite Novamente")
        else: 
            saldo += valor_dep
            extrato += f"[+] Depósito: R$ {valor_dep:.2f}\n"
            print("\nDepósito realizado!")

    elif opção == "s":
        clear()
        print("=========== Saque ===========")
        valor_saque = float(input("Qual o valor que deseja sacar? R$ "))
        if valor_saque > saldo:
            print("Você não possui Saldo suficiente. Tente novamente.")

        elif valor_saque > limite:
            print("O valor do saque excede o seu limite (R$ 500.00")

        elif numeros_saque >= limites_saque:
            print("Número de saques excedido (3)")

        else:
            saldo -= valor_saque
            extrato += f"[-] Saque: R$ {valor_saque:.2f}\n"
            numeros_saque += 1
            print("Saque realizado!")
            


    elif opção == "e":
        clear()
        print("=========== Extrato ===========\n")
        print("Não foram realizadas operações" if not extrato else extrato)
        print("\nSaldo Atual: R$", f"{saldo:.2f}")

    elif opção == "q":
        break

    else:
        clear() 
        print("Operação Inválida, por favor selecione novamente o serviço desejado.")