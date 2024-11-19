# Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
# DESAFIO 93:
#       Crie um programa que gerencie o aproveitamento de um jogador de futebol.
#       O programa vai ler o nome do jogador e quantas partidas ele jogou.
#       Depois vai ler a quantidade de gols feitos em cada partida.
#       No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
from cores.colorPrint import color_print
print('-'*60)
print(f"{"Cadastro de jogador de futebol 2":^60}")
print('-'*60)

jogadores = []
continuar = True
while continuar:
    jogador = {"nome": input("Nome do jogador: ")}
    while True:
        try:
            jogador["partidas"] = int(input("Partidas jogadas: "))
            if jogador["partidas"] < 0:
                raise ValueError
            jogador["gols"] = []
            break
        except ValueError:
            color_print("\tValor inválido!", "red")

    if jogador["partidas"]:
        for i in range(jogador["partidas"]):
            while True:
                try:
                    gols = int(input(f"Quantidade de gols na partida {i+1}: "))
                    if gols < 0:
                        raise ValueError
                    jogador["gols"].append(gols)
                    break
                except ValueError:
                    color_print("\tValor inválido!", "red")
        jogador["total"] = sum(jogador["gols"])
    else:
        jogador["total"] = 0

    jogadores.append(jogador.copy())
    color_print("\tJogador cadastrado com sucesso!", "green")
    jogador.clear()

    while True:
        resposta = input("\tDeseja continuar? [S/N]: ").strip().upper()
        if resposta in ["S", "N"]:
            if resposta == "N":
                continuar = False
            break
        else:
            color_print("\tResposta inválida!", "red")

print("-"*60)
print(f"{"Cod.":<4} {"Nome":<20} {"Gols":<20} {"Total"}")
print("="*52)
for i, jogador in enumerate(jogadores):
    print(f"{i:<4} {jogador["nome"]:<20} {str(jogador["gols"]):<20} {jogador["total"]}")
print("="*52)
while True:
    try:
        cod_jogador = int(input("Cód. do jogador para detalhes [-1 para finalizar]: "))
        if -1 <= cod_jogador < len(jogadores):
            if cod_jogador > -1:
                print(f"\tDados do jogador {jogadores[cod_jogador]['nome']}")
                if jogadores[cod_jogador]['partidas'] > 0:
                    for i, gols in enumerate(jogadores[cod_jogador]['gols']):
                        print(f"\t\tNo jogo {i+1} foram marcados {gols} gols.")
                else:
                    print(f"\t\tO jogador jogou {jogadores[cod_jogador]['partidas']} partidas.")
                print("-" * 52)
            else:
                break
        else:
            raise ValueError
    except ValueError:
        color_print("\tCód. Inválido!", "red")

print("Programa finalizado com sucesso!")