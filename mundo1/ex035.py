# Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo.

print("-=-"*20)
print("Analisador de triângulos".center(60))
print("-=-"*20)

reta1 = float(input("\tDigite o tamanho do primeiro segmento de reta: "))
reta2 = float(input("\tDigite o tamanho do segundo segmento de reta: "))
reta3 = float(input("\tDigite o tamanho do terceiro segmento de reta: "))

print("As retas de tamanho {}, {}, e {} {} um triângulo".format(
    reta1, reta2, reta3,
    "NÃO FORMAM" if reta1 + reta2 <= reta3 or reta1 + reta3 <= reta2  or reta2 + reta3 <= reta1 else "FORMAM"
))