#Coding: utf-8

__author__ = "Bruno Perotti"

class A:
    def __init__(self):
        print(id(self))

a= A()
print(id(a))

