# Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
#   A) Quantas pessoas foram cadastradas
#   B) A média de idade
#   C) Uma lista com as mulheres
#   D) Uma lista de pessoas com idade acima da média
from cores.colorPrint import color_print

print('-'*60)
print(f"{"Unindo dicionários e listas":^60}")
print('-'*60)

pessoas = []
continuar = True
while continuar:
    temp = {"nome": input("Digite o nome: ").strip()}
    while True:
        temp["sexo"] = input("Digite o sexo [M/F]: ").strip().upper()
        if temp["sexo"] not in ["M", "F"]:
            color_print("\tOpção inválida!", "red")
        else:
            break
    temp["idade"] = int(input("Digite a idade: "))
    color_print(f"\t{temp["nome"]} cadastrad{"o" if temp["sexo"] == "M" else "a"} com sucesso!", "green")

    pessoas.append(temp.copy())
    temp.clear()

    while True:
        resposta = input("\tDeseja continuar? [S/N]: ").strip().upper()
        if resposta in ["S", "N"]:
            if resposta == "N":
                continuar = False
            break
        else:
            color_print("\tResposta incorreta!", "red")
print("-"*60)

print(f"A) Foram cadastradas {len(pessoas)} pessoas.")

media = sum([pessoa["idade"] for pessoa in pessoas])/len(pessoas)
print(f"B) A média de idades é de {media:.1f} anos.")

print(f"C) As mulheres cadastradas foram: {", ".join([mulher["nome"] for mulher in pessoas if mulher['sexo'] == 'F'])}.")

print("D) As pessoas com idade acima da média são:")
for pessoa in pessoas:
    if pessoa["idade"] > media:
        print(f"\t{pessoa["nome"]} - "
              f"Sexo: {"Masculino" if pessoa["sexo"] == "M" else "Feminino"}, "
              f"Idade: {pessoa["idade"]}.")

print("Programa finalizado com sucesso!")