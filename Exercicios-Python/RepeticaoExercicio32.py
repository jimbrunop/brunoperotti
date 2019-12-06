# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
# Fatorial de: 5
# 5! =  5 . 4 . 3 . 2 . 1 = 120

num_fatorial = int(input("informe o valor fatorial: "))

def cria_fatoriais(num_fatorial):
    fatorial = 1
    lista_anteriores = []
    lista_fatorial = []
    while (num_fatorial > 0):
        lista_fatorial.append(num_fatorial)
        fatorial = fatorial * num_fatorial
        num_fatorial -= 1
        lista_anteriores.append(num_fatorial)
    lista_anteriores.remove(0)
    frase_fatoria = "O valor fatorial é: " + str(lista_fatorial[0]) + "!= " + str(lista_anteriores) + " = " + str(fatorial)
    frase_sem_virgula = frase_fatoria.replace(",",".")
    frase_sem_col_inicio = frase_sem_virgula.replace("[", " ")
    frase_sem_col_fim = frase_sem_col_inicio.replace("]"," ")
    print(frase_sem_col_fim)
cria_fatoriais(num_fatorial)

