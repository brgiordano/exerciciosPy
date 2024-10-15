# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
nome = str(input("Digite um nome completo: ").strip())
print("O nome \"{}\" {} \"SILVA\".".format(
    nome.title(),
    "contém" if "SILVA" in nome.upper() else "não contém"))