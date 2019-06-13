import datetime
import random
def calculaFuncao(funcao):
    def calcula():
        print(datetime.datetime.now())
        funcao()
        print(datetime.datetime.now())

    return calcula



@calculaFuncao
def outroCalculo():
    for i in range(10000000):
        continue

    lista = random.sample(range(10), 4)
    print(lista)
    print(sum(lista))

outroCalculo()