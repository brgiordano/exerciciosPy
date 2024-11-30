# Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
# Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.
print('-'*60)
print(f"{"Transformando módulos em pacotes":^60}")
print('-'*60)
from utilidades import moeda

valor = float(input('Digite um valor: R$ '))
moeda.resumo(valor, 80, 35)
moeda.resumo()