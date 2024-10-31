# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

while True:
    dicionario = {'M': "Masculino", 'F': "Feminino"}
    sexo = str(input('Informe o sexo [M/F]: ')).upper().strip()
    if sexo not in ['M', 'F']:
        print(f'\tValor <{sexo}> inválido.Informe um valor válido: [M/F]')
    else:
        break

print(f"\tSexo escolhido: {dicionario[sexo]}")