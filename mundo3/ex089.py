# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um
# e permita que o usuário possa mostrar as notas de cada aluno individualmente.
from cores.colorPrint import color_print

print('-'*60)
print(f"{"Boletin com listas compostas":^60}")
print('-'*60)

alunos = []
continuar = True
while continuar:
    aluno_dados = [input("Digite o nome do aluno: "),
                   float(input("Digite a primeira nota: ")),
                   float(input("Digite a segunda nota: "))]
    alunos.append(aluno_dados)
    color_print("\tNotas cadastradas!", "green")
    while True:
        resp = input("\tDeseja continuar? [S/N]: ").upper()
        if resp in ['S', 'N']:
            if resp == 'N':
                continuar = False
            break
        else:
            color_print("\tResposta inválida!", "red")

print('-'*60)
print(f"{"Nº":4} {"NOME":20} {"MÉDIA"}")

print('='*32)
for i, aluno in enumerate(alunos):
    print(f"{i:<4} {aluno[0]:20} {(aluno[1] + aluno[2])/2:>4.1f}")
print('='*32)

continuar = True
while continuar:
    while True:
        n = input("Nº do aluno p/ visualizar notas ['F' p/ finalizar]: ").upper()
        try:
            n = int(n)
            if not 0 <= n < len(alunos):
                color_print(f"\tAluno '{n}' não existe!", "red")
                continue
        except ValueError:
            if n == 'F':
                continuar = False
            else:
                color_print("\tResposta inválida!", "red")
                continue
        break
    if continuar:
        color_print(f"\tNotas de {alunos[n][0]}: {alunos[n][1:]}", "cyan")