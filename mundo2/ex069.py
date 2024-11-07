# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
#   A) quantas pessoas tem mais de 18 anos.
#   B) quantos homens foram cadastrados.
#   C) quantas mulheres tem menos de 20 anos.
print('-'*60)
print(f"{"Cadastro de pessoas":^60}")
print('-'*60)

maiores_18 = 0
homens = 0
mulheresAbaixo20 = 0

while True:
    print('-' * 60)
    print(f"{"CADASTRE UMA PESSOA":^60}")
    print('-' * 60)

    while True:
        idade = input("\tIdade: ")
        if not (idade.isnumeric()):
            print("Valor invalido!")
            continue
        idade = int(idade)
        if idade > 18:
            maiores_18 += 1

        while True:
            sexo = input("\tSexo [M/F]: ").strip().upper()
            if not (sexo in ['M', 'F']):
                print("Valor invalido!")
                continue

            if sexo == 'M':
                homens += 1
            else:
                if idade < 20:
                    mulheresAbaixo20 += 1
            break

        break

    while True:
        continuar = input("\tDeseja continuar? [S/N]: ").strip().upper()
        if not continuar in ['S', 'N']:
            print("Valor invalido!")
            continue
        else: break

    if continuar == 'S':
        continue
    else:
        print('-'*60)
        break

print(f"Total de pessoas com mais de 18 anos: {maiores_18}\n"
      f"Total de homens cadastrados: {homens}\n"
      f"Total de mulheres com menos de 20 anos: {mulheresAbaixo20}")