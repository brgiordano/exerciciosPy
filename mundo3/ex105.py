# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
# e vai retornar um dicionário com as seguintes informações:
#   – Quantidade de notas
#   – A maior nota
#   – A menor nota
#   – A média da turma
#   – A situação (opcional)
print('-'*60)
print(f"{"Analisando e gerando dicionários":^60}")
print('-'*60)

def notas(*notas_al, sit=False):
    """
    Função para analisar notas e calcular a média e a situação de vários alunos.
    :param notas_al: uma ou mais notas de alunos.
    :param sit: (opt) False (default), True: inclui o campo situação no retorno
    :return: dict contendo as seguintes informações da turma:
        a quantidade de notas,
        a maior nota,
        a menor nota,
        a média,
        e a situação da turma (opcional. param sit=True)
    """
    notas_dict = {"quantidade": len(notas_al),
                  "maior": max(notas_al),
                  "menor": min(notas_al),
                  "media": sum(notas_al) / len(notas_al)}
    if sit:
        if notas_dict["media"] >= 7:
            notas_dict["sit"] = "BOA"
        elif notas_dict["media"] >= 5:
            notas_dict["sit"] = "RAZOÁVEL"
        else:
            notas_dict["sit"] = "RUIM"
    return notas_dict

resposta = notas(5.5,2.5,1.5, sit=True)
print(resposta)
resposta2 = notas(5.5,2.5,1.5)
print(resposta2)
resposta3 = notas(5.5,2.5,10,6.5, sit=True)
print(resposta3)
resposta4 = notas(5.5, 7, 7.5, 8, 10, sit=True)
print(resposta4)
print(help(notas))