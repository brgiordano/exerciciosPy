# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.
print('-'*60)
print(f"{"Dicionário em python":^60}")
print('-'*60)

aluno = {
    "nome": input("Digite o nome do aluno: "),
    "media": float(input("Digite a media do aluno: ")),
}
aluno["situacao"] = "Aprovado" if aluno["media"] >= 7 else "Reprovado" if aluno["media"] < 5 else "Recuperação"

print('-'*60)
print(f"Aluno: {aluno['nome']} - Média: {aluno['media']} - {aluno['situacao'].upper()}")
