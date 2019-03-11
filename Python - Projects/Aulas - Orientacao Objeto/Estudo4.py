#coding: utf-8

__author__ = "Bruno Perotti"

class Retangulo:

    def __init__(self, largura, altura):
        self.a = largura
        self.l = altura

    def area(self):
        return self.a * self.l


r1 = Retangulo(10,5)



print(r1.area())