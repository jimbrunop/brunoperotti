# Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.

sistema_ativo = True

def realiza_calculo(sistema_ativo):
    lista_numeros_total = []
    contador_ate_25 = 0
    contador_de_26_a_50 = 0
    contador_de_51_a_75 = 0
    contador_de_76_a_100 = 0
    contador_alem_101 = 0
    while sistema_ativo == True:
        numero = int(input("Informe um numero positivo para continuar ou negativo para finalizar: "))
        lista_numeros_total.append(numero)
        if numero < 0:
            sistema_ativo = False
        else:
            if numero <= 25:
                contador_ate_25 += 1
            if numero <= 26 and numero <= 50:
                contador_de_26_a_50 += 1
            if numero <= 51 and numero <= 75:
                contador_de_51_a_75 += 1
            if numero <= 76 and numero <= 100:
                contador_de_76_a_100 += 1
            else:
                contador_alem_101 +=1

    print("Quantidade até 25: " + str(contador_ate_25))
    print("Quantidade de 26 a 50: " + str(contador_de_26_a_50))
    print("Quantidade de 51 a 75: " + str(contador_de_51_a_75))
    print("Quantidade de 76 a 100: " + str(contador_de_76_a_100))
    print("Quantidade acima de 101 " + str(contador_alem_101))
realiza_calculo(sistema_ativo)