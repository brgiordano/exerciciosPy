# módulo do ex109
def aumentar(valor: float, taxa: float, formatado: bool = False, symb = 'R$'):
    aumentado = valor * (1 + taxa/100)
    return moeda(aumentado, symb) if formatado else str(aumentado)

def diminuir(valor: float, taxa: float, formatado: bool = False, symb = 'R$'):
    diminuido = valor * (1 - taxa/100)
    return moeda(diminuido, symb) if formatado else str(diminuido)

def dobro(valor: float, formatado: bool = False, symb = 'R$'):
    dobrado = valor * 2
    return moeda(dobrado, symb) if formatado else str(dobrado)

def metade(valor: float, formatado: bool = False, symb = 'R$'):
    dividido = valor / 2
    return moeda(dividido, symb) if formatado else str(dividido)

def moeda(valor: float, symb = "R$"):
    return f"{symb}{valor:.2f}".replace('.', ',')