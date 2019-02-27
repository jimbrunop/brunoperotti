#coding: utf-8


#intro funçoes

def minha_func():
    print("Fala galera!")

minha_func()


#parametros

def soma(x,y):
    total = x + y
    print("O total da soma de x + y: ", total)

soma(10,50)


#param default

def login(usuario="root", senha="123"):
    print("usuário: ", usuario)
    print("senha: ", senha)
login()


# argumentos posicionais e argumentos nomeados

def dados_pessoais (nome, sobrenome, idade, sexo):
    print("Nome: {} \nSobrenome: {}\nidade: {}\nsexo: {}".format(nome, sobrenome,idade, sexo))

dados_pessoais(nome="Bruno", sobrenome="Perotti", idade=34, sexo=True)


#retorno de valores

def soma2(x3,x4):
    num = x3 * x4
    return num

print(soma2(10,20))

#retorno de valores multiplos
def func():
    return 1,2

a,b = func()

print(a)
print(b)

# função variável

def lista_de_argumentos(*lista):
    print(lista)


def lista_deargumentos_associativos(**dicionario):
    print(dicionario)

def argumentos(*args, **kwargs):
    print(args)
    print(kwargs)

argumentos(1,2,3,4, um=1,dois=2,tres=3)
lista_de_argumentos(1,2,3,4,5,6)
lista_de_argumentos("um","dois", "três", "quatro", "cinco", "seis")

lista_deargumentos_associativos(a=1, b=2, c=3, d=4)
lista_deargumentos_associativos(um=1,dois=2,tres=3,quatro=4)