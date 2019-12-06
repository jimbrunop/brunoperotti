#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

valor_hora_trabalhada = float(input("informe em reais o valor recebido por hora trabalhada: "))
quantidade_horas_trabalhadas = float(input("Informe quantas horas foram trabalhadas no mês: "))

valor_mensal = valor_hora_trabalhada * quantidade_horas_trabalhadas

print("o seu salário foi de: R$" + str(valor_mensal))