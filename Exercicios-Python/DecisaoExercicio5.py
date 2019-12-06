# Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
#
#     A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#     A mensagem "Reprovado", se a média for menor do que sete;
#     A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota_1 = float(input("Informe a primeira nota"))
nota_2 = float(input("Informe a segunda nota"))

def calcula_media(nota_1, nota_2):
    media = (nota_1 + nota_2)/2
    return media

def valida_aprovacao(media):
    if media >= 7.00 and media != 10.00:
        print("Aprovado")
    if media == 10.00:
        print("Aprovado com distinção")
    else:
        print("Reprovado")
valida_aprovacao(media=calcula_media(nota_1,nota_2))