#coding: utf-8

__author__ = "Bruno Perotti"


class MEstaticos:
    @staticmethod
    def func1():
        print("func ()")

    @staticmethod
    def func2(x, y):
        print("Função () invocada.\n Params ({},{})".format("func2", x, y))

    @staticmethod
    def func3 (a,b,c):
        info = """
        Nome da função: (nome)
        Quantidade de args: (quantidade)
        Args: (args)
        """
        info = info.format(
            nome=MEstaticos.func3.__name__,
            quantidade=MEstaticos.func3.__code__.co_argcount,
            args=MEstaticos.func3.__code__.co_varnames
        )
        print(info)


    # func1 = staticmethod(func1)
    # func2 = staticmethod(func2)
    # func3 = staticmethod(func3)


me = MEstaticos()
me.func1()
MEstaticos.func1()
MEstaticos.func2(100,200)
MEstaticos.func3(5,10,15)
