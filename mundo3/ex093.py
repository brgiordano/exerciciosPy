# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
print('-'*60)
print(f"{"Cadastro de jogador de futebol":^60}")
print('-'*60)

jogador = {"nome": input("Nome do jogador: "),
           "partidas": int(input("Partidas jogadas: ")),
            "gols": []}

if jogador["partidas"]:
    for i in range(jogador["partidas"]):
        jogador["gols"].append(int(input(f"Quantidade de gols na partida {i+1}: ")))
    jogador["total"] = sum(jogador["gols"])
else:
    jogador["total"] = 0

print("-"*60)
print("Dicionário:")
print('\t',jogador)

print("-"*60)
print("Laço:")
for k, v in jogador.items():
    print(f"\t{k.capitalize()} = {v}")

print("-"*60)
print("Formatado:")
print(f"\tO jogador {jogador["nome"]} jogou {jogador['partidas']} partidas.")
for i, v in enumerate(jogador["gols"]):
    print(f"\t\tPartida {i+1}: {v} gols.")
print(f"\tTotal de {jogador['total']} gols.")