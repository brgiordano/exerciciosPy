# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre:
#   - a média de idade do grupo;
#   - qual é o nome do homem mais velho
#   - e quantas mulheres têm menos de 20 anos.

QTD_PESSOAS = 4

sexoOpt = {"M": "MASCULINO", "F": "FEMININO"}
mediaIdades = 0
nomeHomemMaisVelho = ""
idadeHomemMaisVelho = 0
qtdMulheresAbaixoDe20 = 0

for i in range(0, QTD_PESSOAS):
    print(f"{"-"*10} {i+1}ª PESSOA {"-"*10}")
    nome = str(input(f"\tNome: ")).strip().title()
    idade = int(input(f"\tIdade: "))
    mediaIdades += idade

    while True:
        sexo = str(input(f"\tSexo [M/F]: ")).strip().upper()
        if sexo in sexoOpt:
            break
        else:
            print("Opção inválida. Escolha M para 'MASCULINO' ou F para 'FEMININO'.")

    if sexoOpt.get(sexo) == sexoOpt.get("M"):
        if i == 0:
            nomeHomemMaisVelho = nome
            idadeHomemMaisVelho = idade
        elif idade > idadeHomemMaisVelho:
            nomeHomemMaisVelho = nome
            idadeHomemMaisVelho = idade
    else:
        if idade < 20:
            qtdMulheresAbaixoDe20 += 1

mediaIdades = mediaIdades / QTD_PESSOAS

print(f"\nMédia de idade do grupo: {mediaIdades} anos")
print("Homem mais velho: ", end="")
if nomeHomemMaisVelho == "":
    print("Não há homens no grupo")
else:
    print(f"{nomeHomemMaisVelho} ({idadeHomemMaisVelho} anos)")
print(f"Mulheres abaixo de 20 anos: {qtdMulheresAbaixoDe20}")