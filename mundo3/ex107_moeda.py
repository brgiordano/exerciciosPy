# módulo do ex107
def aumentar(valor: float, taxa: float):
    return valor * (1 + taxa/100)

def diminuir(valor: float, taxa: float):
    return valor * (1 - taxa/100)

def dobro(valor: float):
    return valor * 2

def metade(valor: float):
    return valor / 2