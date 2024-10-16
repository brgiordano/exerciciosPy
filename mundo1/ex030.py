# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

numero = int(input("Digite um número inteiro: "))
print(f"\tO número {numero} é "
      f"{"PAR." if numero%2 == 0 else "ÍMPAR."}")