from mundo3.ex115.utils.colors import Cores as Clr

CAMINHO_BD = "ex115/bd/bd_pessoas.txt"

# retorna o caminho do arquivo do bd e garante que o arquivo existe
def get_caminho():
    try:
        with open(CAMINHO_BD, 'r'):
            return CAMINHO_BD
    except FileNotFoundError:
        # cria o arquivo no caminho especificado
        try:
            with open(CAMINHO_BD, 'x'):
                return CAMINHO_BD
        except FileNotFoundError:
            print("Caminho do arquivo do Banco de Dados não localizado")

class GerenciadorBD:

    @staticmethod
    def bd_view():
        caminho_bd = get_caminho()
        with open(caminho_bd, 'r', encoding='utf-8') as bd:
            bd_vazio = False if bd.read() else True
            bd.seek(0)
            if not bd_vazio:
                for n, dados in enumerate(bd):
                    nome, idade = dados.split(';')
                    pessoa = (nome.strip(), int(idade.strip()))
                    print(
                        Clr.color_str(
                            f'{n + 1:>5} - {pessoa[0]:<25}{pessoa[1]:>3} anos',
                            'BLUE')
                    )
        if bd_vazio:
            return False
        else:
            return True

    @staticmethod
    def bd_cadastrar(pessoa: tuple[str, int]):
        caminho_bd = get_caminho()
        with open(caminho_bd, 'a', encoding='utf-8') as bd:
            bd.write(f'{';'.join([str(dado) for dado in pessoa])}\n')


    @staticmethod
    def bd_excluir(index: int):
        caminho_bd = get_caminho()
        with open(caminho_bd, 'r', encoding='utf-8') as bd:
            pessoas = bd.readlines()
            pessoas.pop(index)

        with open(caminho_bd, 'w', encoding='utf-8') as bd:
            bd.writelines(pessoas)

    @staticmethod
    def bd_refazer(novo_banco: list):
        caminho_bd = get_caminho()
        with open(caminho_bd, 'w', encoding='utf-8') as bd:
            bd.writelines(novo_banco)

    @staticmethod
    def bd_obter_cadastros():
        caminho_bd = get_caminho()
        with open(caminho_bd, 'r', encoding='utf-8') as bd:
            cadastros = bd.readlines()
            return cadastros
