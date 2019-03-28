#coding: utf-8

__author__ = "Bruno Perotti"

class Passaro():

    patas = 4

    def __init__ (self, nome):
        self.nome = nome

    def som(self):
        return 'piu piu'

    def movimento(self):
        return 'voar'


passaro1 = Passaro('Bolota')
passaro2 = Passaro('Nina')

