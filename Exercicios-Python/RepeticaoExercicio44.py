# Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
# 1 , 2, 3, 4  - Votos para os respectivos candidatos
# (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
# 5 - Voto Nulo
# 6 - Voto em Branco
# Faça um programa que calcule e mostre:
# O total de votos para cada candidato;
# O total de votos nulos;
# O total de votos em branco;
# A percentagem de votos nulos sobre o total de votos;
# A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.

sistema_ativo = True

def votacao(sistema_ativo):
    voto_bruno = 0
    voto_teste = 0
    voto_teste1 = 0
    voto_teste2 = 0
    voto_nulo = 0
    voto_em_branco = 0
    while sistema_ativo == True:
        print("1 - Bruno , 2 - Teste, 3 - Teste1, 4 - Teste2 - Votos para os respectivos candidatos")
        print("5 - Voto Nulo")
        print("6 - Voto em Branco")
        print("0 - Encerrar eleição")
        voto = int(input("Informe o codigo do candidato: "))
        if voto == 0:
            sistema_ativo == False
            total_votos = voto_bruno + voto_teste + voto_teste1 + voto_teste2 + voto_nulo + voto_em_branco
            percentual_votos_nulos = (voto_nulo*100)/total_votos
            percentual_votos_em_branco = (voto_em_branco*100)/total_votos
            print("---------------Eleições 2019----------------")
            print("Totoal de votos Bruno: " + str(voto_bruno))
            print("Totoal de votos Bruno: " + str(voto_teste))
            print("Totoal de votos Bruno: " + str(voto_teste1))
            print("Totoal de votos Bruno: " + str(voto_teste2))
            print("Totoal de votos Bruno: " + str(voto_nulo))
            print("Totoal de votos Bruno: " + str(percentual_votos_nulos) + " %")
            print("Percentual de votos nulos: " + str(percentual_votos_em_branco) + " %")
            print("--------------------------------------------")
            break
        if voto == 1:
            voto_bruno += 1
        if voto == 2:
            voto_teste += 1
        if voto == 3:
            voto_teste1 += 1
        if voto == 4:
            voto_teste2 += 1
        if voto == 5:
            voto_nulo += 1
        if voto == 6:
            voto_em_branco += 1
        else:
            print("Voto inválido, informe de 1 a 6")
votacao(sistema_ativo)

