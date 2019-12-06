# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.

temp_cel = float(input("informe a temperatura em Celsius: "))

temp_far = (temp_cel * 1.8) + 32

print("a temperatura em Fahrenheit é de: " + str(temp_far))