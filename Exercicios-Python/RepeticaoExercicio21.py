#Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.

numero_fornecido = int(input("Informe um número inteiro para validação: "))

def valida_numero_primo(numero_fornecido):
    div = 0
    for divisor in range(1, numero_fornecido):
        if numero_fornecido % divisor == 0:
            div = div + 1
            if div > 1:
                break
    if div > 1:
        print("não é primo")
    else:
        print("é primo")
valida_numero_primo(numero_fornecido)