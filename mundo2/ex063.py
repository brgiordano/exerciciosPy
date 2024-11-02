# Escreva um programa que leia um número N inteiro qualquer
# e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
# Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8

print('-'*30)
print(f"{"Sequência de Fibonacci":^30}")
print('-'*30)

penultimo_termo = 0
ultimo_termo = 1
qtd_termos = int(input("Quantos termos deseja exibir: "))

while qtd_termos > 0:
    print(ultimo_termo, end="  ")
    aux = ultimo_termo
    ultimo_termo += penultimo_termo
    penultimo_termo = aux

    qtd_termos -= 1