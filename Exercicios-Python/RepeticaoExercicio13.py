# Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.

base = int(input("Informe a base: "))
expoente = int(input("Informe o expoente: "))

def calcula_valor (base, expoente):
    print("To usando sim a porra da função da linguagem... ")
    resultado = (base**expoente)
    print("Resultado: " + str(resultado))
calcula_valor(base, expoente)