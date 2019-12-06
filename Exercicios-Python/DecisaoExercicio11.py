# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
#
#     Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#     salários até R$ 280,00 (incluindo) : aumento de 20%
#     salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#     salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#     salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#     o salário antes do reajuste;
#     o percentual de aumento aplicado;
#     o valor do aumento;
#     o novo salário, após o aumento.

salario = float(input("Informe o salário do funcionário"))

def calcula_aumento(salario):
    if salario <= 280.00:
        valor_aumento = (salario * 20) / 100
        salario_ajustado = salario + valor_aumento
        percentual = 20
    elif salario > 280.00 and salario < 700.00:
        valor_aumento = (salario * 15) / 100
        salario_ajustado = salario + valor_aumento
        percentual = 15
    elif salario > 700.00 and salario < 1500.00:
        valor_aumento = (salario * 10) / 100
        salario_ajustado = salario + valor_aumento
        percentual = 10
    else:
        valor_aumento = (salario * 5) / 100
        salario_ajustado = salario + valor_aumento
        percentual = 5
        print(str(salario_ajustado) + '.' + str(percentual) + "." + str(valor_aumento))
    return "Salario ajustado R$: " + str(salario_ajustado), "Percentual de aumento " + str(percentual), "valor aumento R$: " + str(valor_aumento)

print("Salario R$ " + str(salario) + str(calcula_aumento(salario)))