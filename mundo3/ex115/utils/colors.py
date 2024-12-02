from enum import Enum

class Cores(Enum):
    WHITE = "\33[30m"
    RED = "\33[31m"
    GREEN = "\33[32m"
    YELLOW = "\33[33m"
    BLUE = "\33[34m"
    PURPLE = "\33[35m"
    CYAN = "\33[36m"
    GREY = "\33[37m"  # cor default
    DEFAULT = "\33[m"

    @staticmethod
    def color_str(msg = '', color = 'DEFAULT'):
        match color.upper():
            case 'WHITE':
                color = Cores.WHITE.value
            case 'RED':
                color = Cores.RED.value
            case 'GREEN':
                color = Cores.GREEN.value
            case 'YELLOW':
                color = Cores.YELLOW.value
            case 'BLUE':
                color = Cores.BLUE.value
            case 'PURPLE':
                color = Cores.PURPLE.value
            case 'CYAN':
                color = Cores.CYAN.value
            case 'GREY':
                color = Cores.GREY.value
            case _:
                color = Cores.DEFAULT.value
        return color + msg + Cores.DEFAULT.value
