# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random

aluno1 = str(input("Primeiro aluno: "))
aluno2 = str(input("Segundo aluno: "))
aluno3 = str(input("Terceiro aluno: "))
aluno4 = str(input("Quarto aluno: "))

alunos = [aluno1, aluno2, aluno3, aluno4]
print(f"O(A) aluno(a) escolhido(a) foi: {random.choice(alunos)}")


print("-"*30), "\n"


alunos2: list[str] = [""]*4
for i in range(4):
    alunos2[i] = str(input(f"{i+1}º aluno: "))
print(f"O(A) aluno(a) escolhido(a) foi: {random.choice(alunos2)}")


