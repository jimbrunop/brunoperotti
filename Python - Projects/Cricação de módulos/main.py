#coding: utf-8


import estudo


print("Programa acabou")

print(__name__)


def func():
    print("Fala galera")

import dis

dis.dis(func)