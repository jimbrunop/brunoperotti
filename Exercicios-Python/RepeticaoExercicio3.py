# Faça um programa que leia e valide as seguintes informações:
#
#     Nome: maior que 3 caracteres;
#     Idade: entre 0 e 150;
#     Salário: maior que zero;
#     Sexo: 'f' ou 'm';
#     Estado Civil: 's', 'c', 'v', 'd';


nome = input("Informe seu nome completo: ")
idade = int(input("Informe sua idade: "))
salario = float(input("Informe seu salário"))
sexo = input("Informe seu sexo f - feminino ou m - masculino")
estado_civil = input("Informe seu estado civil: s - solteiro, c - casado, v - viuvo ou d - divorciado")

def valida_nome(nome):
    while len(nome) <= 3:
        nome = input("Nome com menos de 3 Chars, Informe seu nome completo: ")
    else:
        return nome

def valida_idade(idade):
    while idade < 0 or idade > 150:
        idade = int(input("Idade inferior a 0 ou superior a 150, Informe a sua idade correta: "))
    else:
        return idade

def valida_salario(salario):
    while salario < 0:
        salario = float(input("Salário informado inferior a zero, Informe seu salário novamente: "))
    else:
        return salario

def valida_sexo(sexo):
    while sexo != 'f' and sexo != "m":
        sexo = input("Sexo informado incorreto, digite f - feminino ou m - masculino")
    else:
        return sexo

def valida_estado_civil (estado_civil):
    while estado_civil != 's' and  estado_civil != 'c' and estado_civil != 'v' and estado_civil != 'd':
        estado_civil = input("Informe seu estado civil: s - solteiro, c - casado, v - viuvo ou d - divorciado")
    else:
        return estado_civil

nome_cliente = valida_nome(nome)
idade_cliente = valida_idade(idade)
salario_cliente = valida_salario(salario)
sexo_cliente = valida_sexo(sexo)
estado_civil_cliente = valida_estado_civil(estado_civil)

print("nome: " + str(nome_cliente))
print("Idade: " + str(idade_cliente))
print("Salário: R$" + str(salario_cliente))
print("Sexo (f - feminino / m - masculino): " + str(sexo_cliente))
print("Estado civil (s - solteiro, c - casado, v - viuvo ou d - divorciado): " + str(estado_civil_cliente))
