# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#
#       Média de Aproveitamento  Conceito
#       Entre 9.0 e 10.0        A
#       Entre 7.5 e 9.0         B
#       Entre 6.0 e 7.5         C
#       Entre 4.0 e 6.0         D
#       Entre 4.0 e zero        E

nota_prova_1 = float(input("Informe a primeira nota"))
nota_prova_2 = float(input("informe a segunda nota"))
media = (nota_prova_1 + nota_prova_2)/2

def calcula_media(media):
    if media >= 9.00 and media <= 10.00:
        print("Conceito A")
    elif media >= 7.50 and media < 9.00:
        print("Conceito B")
    elif media >= 6.00 and media < 7.50:
        print("Conceito C")
    elif media >= 4.00 and media < 6.00:
        print("Conceito D")
    elif media >= 4.00 and media < 0.00:
        print("Conceito E")
calcula_media(media)