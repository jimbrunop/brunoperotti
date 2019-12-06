# Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
# Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
# Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
# A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.


salario_inicio_carreira = int(input("Informe o seu salário iniciao "))
ano_inicio_carreira = int(input("Informe o ano de inicio da carreira "))
ano_atual = int(input("Informe o ano atual "))


def calcula_salario(salario_inicio_carreira, ano_inicio_carreira):
    percentual_ao_mes_inicial = 1.5
    while ano_inicio_carreira < ano_atual:
        resultado_salario = (percentual_ao_mes_inicial * salario_inicio_carreira) / 100
        ano_inicio_carreira += 1
        percentual_ao_mes_inicial *= 2
    total = salario_inicio_carreira + resultado_salario
    print("O salário inicial foi de: R$" + str(salario_inicio_carreira))
    print("O aumento de salário de: R$" + str(resultado_salario))
    print("O salário final foi de: R$" + str(total))

calcula_salario(salario_inicio_carreira, ano_inicio_carreira)