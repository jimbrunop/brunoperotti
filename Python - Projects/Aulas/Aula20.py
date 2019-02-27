#funcoes aninhadas

def func():
    print("func")

    def func_inter():
        print("Função interna")

    func_inter()

func()