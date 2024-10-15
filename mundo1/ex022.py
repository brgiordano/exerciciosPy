# Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao tod0 (sem considerar espaços).
# – Quantas letras tem o primeiro nome.

nome = str(input("Digite o nome completo: ").strip())
print(f"O nome em maiúsculas: {nome.upper()}")
print(f"O nome em minúsculas: {nome.lower()}")
print(f"O nome contém {len(nome) - nome.count(' ')} letras")            # contando todos os caracteres e subtraindo espaços em branco
print(f"O nome contém {len(''.join((nome.split())))} letras")           # usando split e depois join sem separador
print(f"O nome contém {len(nome.replace(' ', ''))} letras") # usando replace de espaços em branco por nenhum espaço
# algumas maneiras de verificar o primeiro nome:
print(f"O primeiro nome é \"{nome[0:nome.find(' ')]}\" e contém {len(nome[0:nome.find(' ')])} letras")
# usando split para separar as sub-strings e contar apenas a primeira
print(f"O primeiro nome é \"{nome.split()[0]}\" e contém {len(nome.split()[0])} letras")