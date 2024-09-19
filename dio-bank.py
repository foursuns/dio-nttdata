import os

audit = ""
balance = 0
number_withdrawals = 0
movement = ""

LIMIT_VALUE = 500
LIMIT_WITHDRAWAL = 3

def screen():
  print("********** Menu **********")
  print("**                      **")
  print("**     1. Depósito      **")
  print("**     3. Saque         **")
  print("**     5. Saldo         **")
  print("**     7. Extrato       **")
  print("**     9. Sair          **")
  print("**                      **")
  print("**************************")

def clear():
    input("Pressione enter para continuar...\n")
    os.system('cls')

def transaction(log):
    global movement
    movement += log

def available():
    print(f"💰 Saldo...: R$ {balance:>10.2f}\n")
    clear()

def deposit():
    amount = float(input("Informe o valor para depósito: "))

    global balance

    if amount > 0:
        balance += amount
        transaction(f"➕ Depósito: R$ {amount:>10.2f}\n")
        print("✅ Depósito realizado com sucesso!\n")
    else:
        print("❌ Valor para depósito deve ser maior que zero!\n")

    clear()

def withdrawal():
    amount = float(input("Informe o valor para saque: "))

    global balance
    global number_withdrawals

    if balance >= amount:
        if number_withdrawals >= LIMIT_WITHDRAWAL:
            print("❌ Limite de saques excedido!\n")
        elif amount > LIMIT_VALUE:
            print("❌ Valor do saque maior que limite permitido!\n")
        else:
            balance -= amount
            number_withdrawals += 1
            transaction(f"➖ Saque...: R$ {amount:>10.2f}\n")
            print("✅ Saque realizado com sucesso!\n")
    else:
        print("❌ Saldo insuficiente!\n")

    clear()

def report():
    print(movement)
    print(f"🟰  Saldo...: R$ {balance:>10.2f}\n")
    clear()

def main():
    while True:
        screen()
        option = input("Escolha uma opção: ")
        
        if option == "1":
            deposit()
        elif option == "3":
            withdrawal()
        elif option == "5":
            available()
        elif option == "7":
            report()
        elif option == "9":
            print("💎 Obrigado por utilizar nossos serviços!\n")
            break
        else:
            print("❗ Opção inválida\n")
            clear()

main()
