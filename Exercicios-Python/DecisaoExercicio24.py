#Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
    #
    # par ou ímpar;
    # positivo ou negativo;
    # inteiro ou decimal.

numero_1 = float(input("Informe o primeiro numero"))
numero_2 = float(input("Informe o segundo numero"))
operacao = input("informe a operação: + para adição, - para subtração, * para multiplicaçao e / para divisão")

def calucula_valor(numero_1, numero_2, operacao):
    if operacao == '+':
        total = numero_1 + numero_2
        if total % 2 == 0:
            print("Valor par")
        else:
            print("Valor impar")
        if total >= 0:
            print("Valor posito")
        else:
            print("Valor negativo")
        if round(total) == total:
            print("Valor inteiro")
        else:
            print("Valor decimal")
    elif operacao == '-':
        total = numero_1 - numero_2
        if total % 2 == 0:
            print("Valor par")
        else:
            print("Valor impar")
        if total >= 0:
            print("Valor posito")
        else:
            print("Valor negativo")
        if round(total) == total:
            print("Valor inteiro")
        else:
            print("Valor decimal")
    elif operacao == '*':
        total = numero_1 * numero_2
        if total%2 == 0:
            print("Valor par")
        else:
            print("Valor impar")
        if total >= 0:
            print("Valor posito")
        else:
            print("Valor negativo")
        if round(total) == total:
            print("Valor inteiro")
        else:
            print("Valor decimal")
    elif operacao == '/':
        total = numero_1 / numero_2
        if total % 2 == 0:
            print("Valor par")
        else:
            print("Valor impar")
        if total >= 0:
            print("Valor posito")
        else:
            print("Valor negativo")
        if round(total) == total:
            print("Valor inteiro")
        else:
            print("Valor decimal")
    else:
        print("Operação incorreta")
calucula_valor(numero_1, numero_2, operacao)