#coding: utf-8

__author__ = "Bruno Perotti"

class Cachorro():

    patas = 4

    def __init__ (self, nome):
        self.nome = nome

    def som(self):
        return 'auau'

    def movimento(self):
        return 'andar'


cachorro1 = Cachorro('Bolota')
cachorro2 = Cachorro('Nina')

