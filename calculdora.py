# opcao = ""
lista = ""
def soma():
    a = float(input("Digite um numero: "))
    b = float(input("Digite um numero: "))
    c = a + b 
    return print(c)
def diminuição():
    a = float(input("Digite um numero: "))
    b = float(input("Digite um numero: "))   

    return a - b

def multiplicação():
    a = float(input("Digite um numero: "))
    b = float(input("Digite um numero: "))

    return a * b

def divisão():
    a = float(input("Digite um numero: "))
    b = float(input("Digite um numero: "))

    return a / b

while lista != "sair":
    print("***Escolha qual operação quer usar***")
    print("1 - soma")
    print("2 - diminuição")
    print("3 - multiplicação")
    print("4 - divisão")
    print("5 - sair ")
    lista = input("Digite uma opção: ")

    if lista == "1":
        soma()
    elif lista == "2":
        diminuição()
    elif lista == "3":
        multiplicação()
    elif lista == "4":
        divisão()
    else:
        print("O usuário saiu")
        break
    

       


