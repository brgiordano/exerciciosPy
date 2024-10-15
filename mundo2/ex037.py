# Escreva um programa em Python que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.

numero = int(input("Digite um número inteiro: "))
print('''Digite a base de conversão:
    [1] - Binária
    [2] - Octal
    [3] - Hexadecimal''')
while True:
    base = int(input("OPÇÃO: "))
    if base in {1, 2, 3}:
        break
    print("\tOpção inválida, tente novamente!")

if base == 1:
    numeroConvertido = bin(numero)
elif base == 2:
    numeroConvertido = oct(numero)
else:
    numeroConvertido = hex(numero)

print("\tO número {} na base {} é: {}".format(
    numero, {1: "BINÁRIA", 2: "OCTAL", 3: "HEXADECIMAL"}.get(base), numeroConvertido[2:]
))