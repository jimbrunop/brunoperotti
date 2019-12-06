# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

num_fatorial = int(input("informe o valor fatorial: "))


def cria_fatoriais(num_fatorial):
    fatorial = 1
    while (num_fatorial > 0):
        fatorial = fatorial * num_fatorial
        num_fatorial -= 1
    print(fatorial)
cria_fatoriais(num_fatorial)

