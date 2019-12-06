# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
#
#     Dicas:
#     Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#     Triângulo Equilátero: três lados iguais;
#     Triângulo Isósceles: quaisquer dois lados iguais;
#     Triângulo Escaleno: três lados diferentes;

lado_triangulo_1 = float(input("Informe um dos lados: "))
lado_triangulo_2 = float(input("Informe o segundo valor:"))
lado_triangulo_3 = float(input("Informe o valor do ultimo lado: "))

soma_lados = lado_triangulo_1 + lado_triangulo_2 + lado_triangulo_3

def valida_triangulo (soma_lados, lado_triangulo_1, lado_triangulo_2, lado_triangulo_3):
    if soma_lados >= lado_triangulo_3:
        if lado_triangulo_1 == lado_triangulo_2 and lado_triangulo_1 == lado_triangulo_3:
            print("Equilatero")
        elif lado_triangulo_1 != lado_triangulo_2 and lado_triangulo_1 != lado_triangulo_3:
            print("Escaleno")
        else:
            print("Isóceles")
valida_triangulo (soma_lados, lado_triangulo_1, lado_triangulo_2, lado_triangulo_3)