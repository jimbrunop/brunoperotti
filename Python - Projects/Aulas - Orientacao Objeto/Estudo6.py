#coding: UTF-8

__author__ = "Bruno Perotti"


class A:
    def __init__(self):
        self._var = 0
    def _get_var(self):
        print("valor esta sendo lido")
        return self._var
    def _set_var(self, x):
        print("valor esta sendo escrito")
        self._var = x

    var = property(fget=_get_var, fset=_set_var)

a = A()
a.var = 10
print(a.var)


