# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
# o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
print('-'*60)
print(f"{"Ficha do jogador":^60}")
print('-'*60)
def ficha(nome='<desconhecido>', gols=0):
    jogador = {'nome': nome, 'gols': gols}
    return jogador

#captura dos dados
nome_jogador = input('Digite o nome do jogador: ').strip()
gols_jogador = input('Digite a quantidade de gols: ')

# validação
if nome_jogador != '' and (gols_jogador.isnumeric() and int(gols_jogador)>=0):
    ficha_jogador = ficha(nome_jogador, int(gols_jogador))
elif nome_jogador != '':
    ficha_jogador = ficha(nome_jogador)
elif gols_jogador.isnumeric() and int(gols_jogador)>=0:
    ficha_jogador = ficha(gols=int(gols_jogador))
else:
    ficha_jogador = ficha()

# print no resultado da função
print(f"O jogador {ficha_jogador['nome']} fez {ficha_jogador['gols']} gol(s) no campeonato.")