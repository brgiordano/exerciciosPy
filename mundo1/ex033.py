# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

numero1 = int(input("Primeiro número: "))
numero2 = int(input("Segundo número: "))
numero3 = int(input("Terceiro número: "))
maior: int
menor: int

if numero1 > numero2 :
    if numero1 > numero3 :
        maior = numero1
        menor = numero3 if numero2 > numero3 else numero2
    else:
        maior = numero3
        menor = numero2
else:
    if numero2 > numero3:
        maior = numero2
        menor = numero3 if numero1 > numero3 else numero1
    else:
        maior = numero3
        menor = numero1

print(f"O menor valor digitado foi: {menor}\n"
      f"O maior valor digitado foi: {maior}")
