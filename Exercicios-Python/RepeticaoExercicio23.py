# Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.
#

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