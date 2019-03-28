
#coding: utf-8

__author__ = "Bruno Perotti"

class Animal():
    def __init__(self, nome, patas = 4):
        self.nome = nome
        self.patas = patas

    def som(self):
        return 'som genŕico'
    def movimento(self):
        return 'andar'


class Cachorro(Animal):

    def __init__ (self, nome, patas = 4):
        Animal.__init__(self,nome,patas)
        self.nome = nome

    def som(self):
        return 'auau'


class Passaro(Animal):

    def __init__ (self, nome, patas = 2):
        Animal.__init__(self,nome,patas)
        self.nome = nome

    def som(self):
        return 'piu piu'

    def movimento(self):
        return 'voar'



