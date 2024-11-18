# Crie um programa que leia nome, ano de nascimento e carteira de trabalho
# e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
# OBS.: o único critério para o tempo para aposentadoria será de 35 anos de contribuição. Apenas para fins didáticos
from datetime import datetime
print('-'*60)
print(f"{"Cadastro de trabalhador":^60}")
print('-'*60)

trabalhador = {"nome": input("Nome: "),
               "idade": datetime.now().year - int(input("Ano de nascimento: ")),
               "ctps": int(input("Nº da Carteira de trabalho (0 se não tiver): "))}

if trabalhador["ctps"] != 0:
    trabalhador["contratacao"] = int(input("Ano de contratação: "))
    trabalhador["salario"] = float(input("Salário: R$ "))
    trabalhador["aposentadoria"] = (trabalhador["contratacao"] + 35) - (datetime.now().year - trabalhador["idade"])

print('-'*60)
print("Dados do trabalhador:")
for k, v in trabalhador.items():
    print(f"\t{k.upper()}: {"RS "f"{v}" if k == "salario" else f"{v}"}")