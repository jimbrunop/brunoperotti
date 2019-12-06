# Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
#
#     C = (5 * (F-32) / 9).


temp_far = float(input("informe a temperatura em Farenheit: "))

temp_cel = (5 * (temp_far - 32) / 9)

print("a temperatura em Celsius é de: " + str(temp_cel))