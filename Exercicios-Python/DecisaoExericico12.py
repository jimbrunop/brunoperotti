# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#
#     Desconto do IR:
#     Salário Bruto até 900 (inclusive) - isento
#     Salário Bruto até 1500 (inclusive) - desconto de 5%
#     Salário Bruto até 2500 (inclusive) - desconto de 10%
#     Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#
#             Salário Bruto: (5 * 220)        : R$ 1100,00
#             (-) IR (5%)                     : R$   55,00
#             (-) INSS ( 10%)                 : R$  110,00
#             FGTS (11%)                      : R$  121,00
#             Total de descontos              : R$  165,00
#             Salário Liquido                 : R$  935,00


horas_trabalhadas_mes = float(input("Informe quantas horas trabalhou no mês: "))
valor_hora = float(input("Informe o valor da hora de trabalho: "))

def calcula_salario (horas_trabalhadas, valor_hora):
    valor_bruto = horas_trabalhadas * valor_hora
    print("Salário bruto: R$" +  str(valor_bruto))
    if valor_bruto <= 900.00:
        desconto_ir = (valor_bruto * 5) / 100
        desconto_inss = (valor_bruto * 10) / 100
        desconto_fgts = (valor_bruto * 11) / 100
        total_descontos = desconto_fgts + desconto_inss + desconto_ir
        valor_liq = valor_bruto - total_descontos
    if valor_bruto > 900.00 and valor_bruto <= 1500:
        desconto_ir = (valor_bruto * 5) / 100
        desconto_inss = (valor_bruto * 10) / 100
        desconto_fgts = (valor_bruto * 11) / 100
        total_descontos = desconto_fgts + desconto_inss + desconto_ir
        valor_liq = valor_bruto - total_descontos - ((valor_bruto * 5)/100)
    return "IR: R$" + str(desconto_ir), "INSS R$: " + str(desconto_inss), "FGTS R$: " + str(desconto_fgts), "Total descontos; R$ " + str(total_descontos),"Salário Liquido R$: " + str(valor_liq)

print(calcula_salario(horas_trabalhadas_mes,valor_hora))