# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#
#     "Telefonou para a vítima?"
#     "Esteve no local do crime?"
#     "Mora perto da vítima?"
#     "Devia para a vítima?"
#     "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

print("responda sim ou nao")
pergunta1 = str(input("Telefonou para a vítima?"))
pergunta2 = str(input("Esteve no local do crime?"))
pergunta3 = str(input("Mora perto da vítima?"))
pergunta4 = str(input("Devia para a vítima?"))
pergunta5 = str(input("Já trabalhou com a vítima?"))

def valida_criminoso(pergunta1, pergunta2, pergunta3, pergunta4, pergunta5):
    lista_qtdade_sim = []
    if pergunta1 == 'sim':
        lista_qtdade_sim.append(pergunta1)
    if pergunta2 == 'sim':
        lista_qtdade_sim.append(pergunta2)
    if pergunta3 == 'sim':
        lista_qtdade_sim.append(pergunta3)
    if pergunta4 == 'sim':
        lista_qtdade_sim.append(pergunta4)
    if pergunta5 == 'sim':
        lista_qtdade_sim.append(pergunta5)

    if len(lista_qtdade_sim) <= 2:
        print("Suspeito")
    elif len(lista_qtdade_sim) >= 3 and len(lista_qtdade_sim) <= 4:
        print("Cúmplice")
    else:
        print("Assassino")
valida_criminoso(pergunta1, pergunta2, pergunta3, pergunta4, pergunta5)
