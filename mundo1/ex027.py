# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input("Digite o nome completo: ")).strip()
print("Olá {} {}.".format(
    nome[: nome.find(' ')],
    nome[nome.rfind(' ')+1 :]))

print("Olá {} {}.".format(
    nome.split()[0],
    nome.split()[-1]))