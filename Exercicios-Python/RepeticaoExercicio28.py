# Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.

quantidade_cds = int(input("Informe a quantidade de cd's: "))

def valor_medio_cds(quantidade_cds):
    contador = 0
    lista_precos_cds = []
    while contador < quantidade_cds:
        valor_unidade_cd = float(input("Informe o valor do primeiro cd: "))
        lista_precos_cds.append(valor_unidade_cd)
        contador += 1
    total_gasto_cds = sum(lista_precos_cds)
    media_gasto = total_gasto_cds / quantidade_cds
    print("Total gasto da coleção: " + str(total_gasto_cds))
    print("Média gasto da coleção: " + str(media_gasto))
valor_medio_cds(quantidade_cds)