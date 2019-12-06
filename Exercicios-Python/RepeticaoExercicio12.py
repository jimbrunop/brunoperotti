# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
#
#     Tabuada de 5:
#     5 X 1 = 5
#     5 X 2 = 10
#     ...
#     5 X 10 = 50


numero_tabuada = int(input("infortme o numero para a tabuada desejada: "))
index = 1

def tabuada(index, numero_tabuada):
    while index <= 10:
        valor_multiplicacao = numero_tabuada * index
        print("Tabuada de " + str(numero_tabuada) + " x " + str(index) + " = " + str(valor_multiplicacao))
        index += 1
tabuada(index,numero_tabuada)