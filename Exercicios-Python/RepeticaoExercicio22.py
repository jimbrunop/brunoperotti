# Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.

numero_fornecido = int(input("Informe um número inteiro para validação: "))

def valida_numero_primo(numero_fornecido):
    lista_primos = []
    div = 0
    for divisor in range(1, numero_fornecido):
        if numero_fornecido % divisor == 0:
            div = div + 1
            lista_primos.append(div)
            if div > 1:
                break
    if div > 1:
        print("não é primo")
        print("os numeros primos para este caso, no range, seriam" + str(lista_primos))
    else:
        print("é primo")
valida_numero_primo(numero_fornecido)