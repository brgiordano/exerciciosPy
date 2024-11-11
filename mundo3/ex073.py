# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
#   a) Os 5 primeiros times.
#   b) Os últimos 4 colocados.
#   c) Times em ordem alfabética.
#   d) Em que posição está o time da Chapecoense.
print('-'*60)
print(f"{"Campeonato Brasileiro 2024":^60}")
print('-'*60)

times_brasileirao = (
    "Botafogo",
    "Palmeiras",
    "Fortaleza",
    "Internacional",
    "Flamengo",
    "São Paulo",
    "Cruzeiro",
    "Bahia",
    "Vasco da Gama",
    "Corinthians",
    "Atlético-MG",
    "Grêmio",
    "EC Vitória",
    "Fluminense",
    "Criciúma",
    "Juventude",
    "Bragantino",
    "Athletico-PR",
    "Cuiabá",
    "Atlético-GO"
)
print(f"Os 5 primeiros colocados são:")
for p, t in enumerate(times_brasileirao[:5]):
    print(f"\t{p+1}º: {t}")

print("Os 4 últimos colocados são:")
for p, t in enumerate(times_brasileirao[-4:], start=len(times_brasileirao)-4):
    print(f"\t{p+1}º: {t}")

print("Os times em ordem alfabética são:")
for t in sorted(times_brasileirao):
    print(f"\t{t}")


# MANEIRA 1 de buscar um time específico:
time_buscado = "Chapecoense"
print(f"O {time_buscado} ", end='')
for p, t in enumerate(times_brasileirao):
    if t.lower() == time_buscado.lower():
        print(f"está na {p+1}ª posição do Brasileirão série A")
        break
else: # esse else só é executado caso o for não seja interrompido com break
    print("não está disputando a série A do Brasileirão.")

# MANEIRA 2 de buscar um time específico:
# porém, o nome do time deve está com a grafia exatamento igual ao que contém na tupla
print(f"O {time_buscado} ", end='')
try:
    print(f"está na {times_brasileirao.index(time_buscado)+1}ª posição do Brasileirão série A")
except ValueError:
    print("não está disputando a série A do Brasileirão.")
