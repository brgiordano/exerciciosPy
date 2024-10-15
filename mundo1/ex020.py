# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random

alunos: list[str] = [""]*4
for i in range(len(alunos)):
    alunos[i] = str(input(f"{i+1}º aluno: "))
print(f"Lista original: {alunos}")

print("Ordem de apresentação será:")

print(f"\t{random.sample(alunos, 4)}")
# poderia usar shuffle para embaralhar o vetor, depois printar ele
# mas o sample não mexe no vetor original, apenas faz uma escolhar única, diferente do choices ele não repete valores
print(f"Usando shuffle:")
print(f"Ordem de apresentação[shuffle] será:")

random.shuffle(alunos)
for i in range(len(alunos)):
    print(f"\t{i+1}º: {alunos[i]}")
