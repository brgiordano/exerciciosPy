# Faça um programa que leia algo pelo tecladoe mostre natela o
# seu tipo primitivo e todas as informações possíveis sobre ele.

entradaDoUsuario = input("Digite algo: ")
print("O tipo primitivo desse valor é {}".format(type(entradaDoUsuario)))
print("Contém apenas espaços: ", entradaDoUsuario.isspace())
print("É número: ", entradaDoUsuario.isnumeric())
print("É alfabético: ", entradaDoUsuario.isalpha())
print("É alfanumérico: ", entradaDoUsuario.isalnum())
print("Está todo em maiúsculo: ", entradaDoUsuario.isupper())
print("Está todo em minúsculo: ", entradaDoUsuario.islower())
print("Está capitalizado: ", entradaDoUsuario.istitle())