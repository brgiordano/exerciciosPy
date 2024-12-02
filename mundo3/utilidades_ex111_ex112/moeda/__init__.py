# módulo do ex111
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

def resumo(valor: float = 0, aumento: float = 0, desconto: float = 0):
    print('-' * 30)
    print(f"{"RESUMO DO VALOR":^30}")
    print('-' * 30)
    print(f"Valor analisado: {moeda(valor)}\n"
          f"Dobro do valor : {dobro(valor, formatado=True)}\n"
          f"Metade do valor: {metade(valor, formatado=True)}\n"
          f"{f"{aumento}% de aumento":<15}: {aumentar(valor, aumento, formatado=True)}\n"
          f"{f"{desconto}% de desconto":<15}: {diminuir(valor, desconto, formatado=True)}")
    print('-' * 30)
