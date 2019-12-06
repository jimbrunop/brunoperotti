# Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.

numero_fornecido = int(input("Informe um número inteiro para validação: "))

def valida_numero_primo(numero_fornecido):
    lista_primos = []
    lista_divisores = []
    div = 0
    for divisor in range(1, numero_fornecido):
        if numero_fornecido % divisor == 0:
            div = div + 1
            lista_primos.append(div)
            lista_divisores.append(divisor)
            if div > 1:
                break
    if div > 1:
        print("não é primo")
    else:
        print("é primo" + str(div))
        print("divisores" + str(lista_divisores))
        print("os numeros primos para este caso, no range, seriam" + str(lista_primos))
valida_numero_primo(numero_fornecido)