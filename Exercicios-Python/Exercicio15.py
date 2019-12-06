# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#
#     salário bruto.
#     quanto pagou ao INSS.
#     quanto pagou ao sindicato.
#     o salário líquido.
#     calcule os descontos e o salário líquido, conforme a tabela abaixo:
#
#     + Salário Bruto : R$
#     - IR (11%) : R$
#     - INSS (8%) : R$
#     - Sindicato ( 5%) : R$
#     = Salário Liquido : R$


valor_hora = float(input("Informe o valor da sua hora: "))
quantidade_horas = float(input("Informe a quantidade de horas trabalhadas: "))

total_mensal_bruto = valor_hora * quantidade_horas
desc_imposto_renda = (total_mensal_bruto * 11)/100
desc_inss = (total_mensal_bruto * 8)/100
desc_sindicato = (total_mensal_bruto * 5)/100
total_mensal_liquido = total_mensal_bruto - desc_sindicato - desc_inss - desc_imposto_renda


print("Salario bruto: R$" + str(total_mensal_bruto))
print("IR (11%): R$" + str(desc_imposto_renda))
print("INSS (8%): R$" + str(desc_inss))
print("Sindicato (5%): R$" + str(desc_sindicato))
print("Salário Liquido: R$" + str(total_mensal_liquido) )

