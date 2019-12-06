#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

altura = float(input("informe a altura: "))
sexo = str(input("informe seu sexo, M para masculino ou F para feminino: "))

if sexo == 'm':
    peso_ideal = (72.7 * altura) - 58
    print("seu peso ideal é de: " + str(peso_ideal) + " kg")
if sexo == 'f':
    peso_ideal = (62.1 * altura) - 44.7
    print("seu peso ideal é de: " + str(peso_ideal) + " kg")
else:
    print("sexo informado não localizado - deve ser morenona")

