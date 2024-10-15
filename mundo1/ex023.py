# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
numero = int(input("Digite um número de 0 a 9999: "))
print(f"O número {numero} contém:")
print("\t{} Unidades".format(numero % 10))
print("\t{} Dezenas".format(int(numero/10) % 10))
# OBS: a divisão inteira também pode ser feita pelo operador //
print("\t{} Centenas".format((numero//100) % 10))
print("\t{} Milhares".format((numero//1000) % 10))