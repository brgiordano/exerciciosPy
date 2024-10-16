# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes
#           DESAFIO 35: # Desenvolva um programa que leia o comprimento de três retas
#                       # e diga ao usuário se elas podem ou não formar um triângulo.

print("-=-"*20)
print("TIPOS DE TRIÂNGULOS".center(60))
print("-=-"*20)

ladoA = float(input("\tDigite o primeiro segmento de reta: "))
ladoB = float(input("\tDigite o segundo segmento de reta: "))
ladoC = float(input("\tDigite o terceiro segmento de reta: "))

print("Os segmentos de reta de tamanhos {:.2f}, {:.2f}, e {:.2f} ".format(ladoA, ladoB, ladoC), end="")
if (ladoA + ladoB > ladoC) and (ladoA + ladoC > ladoB) and (ladoC + ladoB > ladoA):
    print("FORMAM um triângulo ", end="")
    if ladoA == ladoB == ladoC:
        print("EQUILÁTERO.")
    elif (ladoA == ladoB) or (ladoA == ladoC) or (ladoB == ladoC):
        print("ISÓSCELES.")
    else:
        print("ESCALENO.")
else:
    print("NÃO são capazes de formar um triângulo.")