# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
qtdNotas = 2
media: float = 0
notas: list[float] = [0] * qtdNotas
for i in range(qtdNotas):
    notas[i] = float(input(f"Digite a {i + 1}ª nota: "))
    media += notas[i]
media = media / qtdNotas
print(f"A media é: {media:.2f}")
