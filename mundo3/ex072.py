# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
print('-'*60)
print(f"{"Números por extenso":^60}")
print('-'*60)

numeros_extenso = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez",
                "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

while True:
    try:
        numero = int(input("Digite um número entre 0 e 20: "))
        if not 0 <= numero <= 20:
            raise ValueError
    except ValueError:
        print("Valor incorreto, digite um número entre 0 e 20")
        continue
    print(f"\tVocê digitou o número {numeros_extenso[numero].upper()}")
    break
