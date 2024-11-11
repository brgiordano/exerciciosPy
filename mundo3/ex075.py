# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
# No final, mostre:
#   A) Quantas vezes apareceu o valor 9.
#   B) Em que posição foi digitado o primeiro valor 3.
#   C) Quais foram os números pares.
print('-'*60)
print(f"{"Números em Tupla":^60}")
print('-'*60)

numeros = ()
for i in range(0,4):
    n = int(input('Digite um valor: '))
    numeros += (n,)

print(f"\tOs valores digitados foram: {numeros}")
print(f"\tO valor 9 apareceu {numeros.count(9)} vezes.")

if 3 in numeros:
    print(f"\tO primeiro valor 3 foi digitado na {numeros.index(3)+1}ª posição")
else:
    print(f"\tO valor 3 não foi digitado.")

print("\tOs valores pares digitados foram: ", end='')
cont = 0
for i in numeros:
    if i%2 == 0:
        if cont == 0:
            print(i, end='')
        else:
            print(f", {i}", end='')
        cont += 1