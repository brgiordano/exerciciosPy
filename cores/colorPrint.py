from cores.cores import Cores
def color_print(msg: str, color: str = "DEFAULT"):
    if color.upper() in Cores.__members__:
        cor = Cores[color.upper()]
    else:
        cor = Cores["DEFAULT"]
    print(f"{cor.value}{msg}{Cores.DEFAULT.value}")