# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.
print('-'*60)
print(f"{"Exercitando módulos em Python":^60}")
print('-'*60)
import ex107_moeda as moeda

valor = float(input('Digite um valor: R$'))
print(f"R${valor:.2f} aumentado em 10% fica: R${moeda.aumentar(valor, 10):.2f}")
print(f"R${valor:.2f} diminuído em 10% fica: R${moeda.diminuir(valor, 10):.2f}")
print(f"O dobro de R${valor:.2f} é: R${moeda.dobro(valor):.2f}")
print(f"A metade de R${valor:.2f} é: R${moeda.metade(valor):.2f}")