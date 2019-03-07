def erro(x):
    try:
        eval(x)
    except (TypeError, NameError):
        print("NameError ou TypeError")
    except ValueError:
        print("ValueError")
    except ZeroDivisionError:
        print("ZeroDivisionError")
    else:
        print("Nenhuma exceção ocorreu")


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