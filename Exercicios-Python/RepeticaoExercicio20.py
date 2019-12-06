# Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.


num_fatorial = int(input("informe o valor fatorial: "))
def cria_fatoriais(num_fatorial):
    fatorial = 1
    if num_fatorial <= 16:
        while num_fatorial > 0:
            fatorial = fatorial * num_fatorial
            num_fatorial -= 1
        print(fatorial)
    else:
        print("Numero Fatorial precisa ser menor ou iagual a 16")

cria_fatoriais(num_fatorial)

