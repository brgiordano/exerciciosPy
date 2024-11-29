# Adapte o código do desafio #107, criando uma função adicional chamada moeda()
# que consiga mostrar os números como um valor monetário formatado.
# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.
print('-'*60)
print(f"{"Formatando moedas em Python":^60}")
print('-'*60)
import ex108_moeda as moeda

valor = float(input('Digite um valor: R$'))
print(f"{moeda.moeda(valor, "R$")} aumentado em 10% fica: {moeda.moeda(moeda.aumentar(valor, 10), "R$")}")
print(f"{moeda.moeda(valor)} diminuído em 10% fica: {moeda.moeda(moeda.diminuir(valor, 10))}")
print(f"O dobro de {moeda.moeda(valor)} é: {moeda.moeda(moeda.dobro(valor))}")
print(f"A metade de {moeda.moeda(valor)} é: {moeda.moeda(moeda.metade(valor))}")