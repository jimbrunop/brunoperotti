#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

import math

raio = float(input("informe o valor do raio: "))

area = math.pi * (raio * raio)

print("A área do círculo é: " + str(area))