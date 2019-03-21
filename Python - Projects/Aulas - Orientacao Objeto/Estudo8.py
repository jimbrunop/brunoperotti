#Coding: utf-8

__author__= "Bruno Perotti"


class Retangulo:

    def __init__(self, largura, altura):
        self._largura = 0
        self._altura = 0
        self.altura = altura
        self.largura = largura

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def _altura (self, num):
        self._altura = num
        if (not(isinstance(num, int)and(num > 0))):
            raise ValueError("Altura inválida: {}".format(num))
        self._altura = num

    @property
    def largura(self):
        return self._largura

    @largura.setter
    def largura(self, num):
        if(not(isinstance(num,int)and(num > 0))):
            raise ValueError("Largura inválida: {}".format(num))
        self._largura = num

    @property
    def area(self):
        return self._altura * self._largura




    # altura = property(fget=_get_altura, fset=_set_altur)
    # largura = property(fget=_get_largura, fset=_set_largura)
    # area = property(fget=_get_area)


r = Retangulo(largura=5, altura=5)


r.largura = 10
r.altura = 5

# r.area = 10

print(r.altura)
print(r.largura)
print()




