# Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
#
#     Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
#     326 = 3 centenas, 2 dezenas e 6 unidades
#     12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

numero_inserido = str(input("Informe um valor real entre 0 e 1000: "))
qtdade_numero = len(numero_inserido)

print(qtdade_numero)

def valida_valor(numero_inserido, qtdade_numero):
    if qtdade_numero == 3:
        centena = numero_inserido[0:1]
        dezena = numero_inserido[1:2]
        unidade = numero_inserido[2:3]
        print("centena: " + str(centena) + "dezena: " + str(dezena) + "unidade: " + str(unidade))
    elif qtdade_numero == 2:
        dezena = numero_inserido[0:1]
        unidade = numero_inserido[1:2]
        print("dezena: " + str(dezena) + "unidade: " + str(unidade))
    elif qtdade_numero == 1:
        unidade = numero_inserido[0:1]
        print("unidade: " + str(unidade))
    else:
        print("numero maior que 1000, n vai rolar")
valida_valor(numero_inserido, qtdade_numero)