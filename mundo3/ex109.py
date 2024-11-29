# Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais,
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(),
# desenvolvida no desafio 108.
print('-'*60)
print(f"{"Formatando moedas em Python":^60}")
print('-'*60)
import ex109_moeda as moeda

valor = float(input('Digite um valor: R$'))
print(f"{moeda.moeda(valor, "R$")} aumentado em 10% fica: {moeda.aumentar(valor, 10, True, "R$")}")
print(f"{moeda.moeda(valor)} diminuído em 10% fica: {moeda.diminuir(valor, 10, True)}")
print(f"O dobro de {moeda.moeda(valor)} é: {moeda.dobro(valor, True)}")
print(f"A metade de {moeda.moeda(valor)} é: {moeda.metade(valor, True)}")