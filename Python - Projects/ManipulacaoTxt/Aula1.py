#coding-utf8
# r - apenas leitura
# w - somente para escrever
# a - abre o arquivo para acrescentar

__author__ = "Bruno Perotti"


frases = ['o ceu é azul', 'Bruno é legal']

arq = open('arquivoTeste', mode='w', encoding='utf-8')
for frases in frases:
    arq.write(frases+'\n')
arq.close()


with open('arquivoTeste', mode='r', encoding='utf-8') as arq:
    for line in arq.readline():
        print(line.strip())


with open('arquivoTeste', mode='a', encoding='utf-8') as arq:
    arq.write('teste inserir umas paradas'+'\n')
    arq.write('mais uma linha so para ter certeza')

with open('arquivoTeste', mode='r', encoding='utf-8') as arq:
    print(line.strip())