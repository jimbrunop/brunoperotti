#coding: UTF-8

__author__ = "Bruno Perotti"

class MinhaClasse:
    membro_cls = 50
    def __init__(self):
        self.membro_inst = -10
    def func(self):
        print(i1.membro_inst)
        print(self.membro_cls)
        print(MinhaClasse.membro_cls)


i1 = MinhaClasse()
i2 = MinhaClasse()


print(MinhaClasse.membro_cls)
print(i1.membro_cls)
print(i2.membro_cls)

i1.membro_cls = 10000

print("------------------")
print(MinhaClasse.membro_cls)
print(i1.membro_cls)
print(i2.membro_cls)


# i1.membro_inst = 10
# print("i1 "+str(i1.membro_inst))
# print("i2 "+str(i2.membro_inst))
#
# MinhaClasse.membro_cls = 9
#
# print("---------------")
# print("i1 "+str(i1.membro_cls))
# print("i2 "+str(i2.membro_cls))
