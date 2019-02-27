#desempacotamento

lista = [10,20]

def func(a,b):
    print()

func(*lista)
func(10,20)
func(a=10,b=20)


def pessoa(nome, sobrenome, idade):
    print(nome)
    print(sobrenome)
    print(idade)

tupla = "eXcript", "Brazil", 10

pessoa(tupla[0], tupla[1], tupla[2])

print()

pessoa(*tupla)

