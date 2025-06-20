# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

from cores.cores import *

print("\n"+"-=-"*4, end = "")
print("Cálculo de média", end = "")
print("-=-"*5)
qtdNotas = 2
notas: list[float] = [0] * qtdNotas
for i in range(len(notas)):
    notas[i] = float(input(f"\tDigite a {i+1}ª nota: "))
media = sum(notas) / len(notas)

print(f"{cyan}Sua média foi {media:.1f}{default}")
if 5 < media < 7:
    print(f"Você está em {yellow}RECUPERAÇÃO{default}")
elif media < 5:
    print(f"Você está {red}REPROVADO{default}")
else:
    print(f"PARABÉNS! Você foi {green}APROVADO{default}")



