#coding: utf-8

__author__ = 'Bruno Perotti'


import json
from pprint import pprint

dados = [('Bruno','22442266'),
         ('Joana','22220022')]
pessoas = [{'nome':nome,'telefone':telefone} for (nome,telefone) in dados]


#escrevendo
with open('jsonTeste1', mode='w', encoding='utf-8') as arq:
    json.dump(pessoas,arq)

#lendo
with open('jsonTeste1', mode='r', encoding='utf-8') as arq:
    read = json.load(arq)
    print(read)
