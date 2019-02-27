#Faça um algoritmo que apenas imprima o seu nome na tela e em seguida finalize a aplicação.

print("Bruno")
print()

#Faça um algoritmo que solicite ao usuário digitar o seu nome e em seguida envie a seguinte frase para a saída padrão: "O seu nome é: [nome do usuário]".

nome = input("Digite o seu nome")

print("O seu nome de usuário é: ", nome)
print()

#Faça um algoritmo que solicite o nome e a idade do usuário e então, envie a seguinte frase para o Console: "O seu nome é <nome> e a sua idade é <idade>".

idade = input("Digite sua idade: ")

print("Seu nome é: ", nome, " e sua idade é: ", idade)
print()

#Faça um algoritmo que solicite ao usuário informar um número. Em seguida, armazene este número numa variável. Por fim, envie esse número para a saída padrão.
#Faça um algoritmo que solicite ao usuário informar um número. Em seguida, escreva a seguinte mensagem: "O número digitado foi: ".

numero1 = int(input("Insira um número: "))

print("O número digitado foi: ", numero1)
print()

#Faça um algoritmo que solicite ao usuário informar 3 números. Em seguida, some-os e envie para a saída padrão a seguinte frase: "A soma total é: "

numero2 = int(input("Insira o segundo numero: "))
numero3 = int(input("Insira o terceiro numero: "))
soma = numero1 + numero2 + numero3

print("Soma dos 3 numeros digitado foi: ", soma)
print()

#Faça um algoritmo que solicite ao usuário informar 2 números. Em seguida, some os valores e envie para a saída padrão a seguinte frase: "A soma entre <X> e <Y> é igual <total>".

soma1 = numero1 + numero2

print("A soma entre ", numero1, "e ", numero2, "é igual a ", soma1)
print()

#Faça um algoritmo que solicite a nota das 4 provas semestrais do usuário. Em seguida, calcule e envie para a saída padrão a média:

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media_notas = (nota1 + nota2 + nota3 + nota4)/4

print("A média das 4 notas é ", media_notas)
print()


#Faça um algoritmo em que o usuário informe uma medida em metros. Em seguida, converta essa medida para centímetros e envie para a saída padrão:

medida_metro = float(input("Digite a medida em metros: "))

convesor_medida = medida_metro * 100

print("a medida de ", medida_metro, " metros, em centrimetros é ", convesor_medida)
print()


#Faça um algoritmo que calcule o cubo e o quadrado de um determinado número:

numero_cubo_quadrado = float(input("Digite um número: "))

cubo = numero_cubo_quadrado**3
quadrado = numero_cubo_quadrado**2

print("O quadrado de, ", numero_cubo_quadrado, " é ", quadrado, " e o cubo de ", numero_cubo_quadrado, " é ", cubo)
print()

#Faça um algoritmo que solicite ao usuário digitar 2 números. Em seguida, imprima o total decimal da divisão e o total inteiro (sem casas decimais):

numero4 = float(input("Digite um numero "))
numero5 = float(input("Digite o segundo numero"))

decimal = numero4/numero5
inteiro_divisao = numero4//numero5

print("O valor total decimal é: ", decimal," e a divisão inteira é: ", inteiro_divisao)
print()

#aça um algoritmo que solicite a largura e a altura de um retângulo. Em seguida, imprima para o usuário quantos metros quadrados possui a área total.

largura = float(input("Digite a largura em metros do triangulo: "))
altura = float(input("Digite a altura em metros do retângulo: "))

area_triangulo = largura * altura

print("A area total do triangulo equivale a: ", area_triangulo, " m²")
print()



#Faça um algoritmo que solicite ao usuário informar uma quantidade de dias, horas, minutos e segundos. Em seguida, converta tudo para segundos:

qtd_dias = int(input("Digite a quantidade de dias: "))
qtd_horas = int(input("Diite a quantidade de horas: "))
qtd_minutos = int(input("Digite a quantidade de minutos: "))
qtd_segudos = int(input("Digite a quantidade de segundos: "))

calculo_total_seg = (((qtd_dias*24)*60)*60) + ((qtd_horas*60)*60) + (qtd_minutos*60) + qtd_segudos

print("a quantidade de segundos equivale a : ", calculo_total_seg)
print()

#Faça um algoritmo que solicite ao usuário informar o valor de uma compra. Em seguida, aplique 10% de desconto e imprima na tela tanto o valor total e também o valor com o desconto aplicado.

valor_compra = float(input("Digite o valor da compra: "))

desconto10 = valor_compra - ((10*valor_compra)/100)

print("O valor de sua aquisição é de ", valor_compra, " e o desconto de 10% gera o novo valor de: ", desconto10)
