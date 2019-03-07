#coding: utf-8


def erro(x):
    try:
        eval(x)
    except (TypeError, NameError):
        print("NameError ou TypeError")
    except ValueError as e:
        print("ValueError")
        print(type(e))
        print(e.args)
    except ZeroDivisionError:
        print("ZeroDivisionError")



#TypeError
erro("int+int")

#NameError
erro("a")

#ValueError
erro("int('a')")

#ZeroDivisionError
erro("5/0")

#sem excessao
erro("10+10")

print("App finalizada")