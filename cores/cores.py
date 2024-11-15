from enum import Enum
#   text color
#       30 - white      34 - blue
#       31 - red        35 - purple
#       32 - green      36 - cian
#       33 - yellow     37 - grey (default)

ansiScape = "\033["
class Cores(Enum):
    WHITE = ansiScape + "30m"
    RED = ansiScape + "31m"
    GREEN = ansiScape + "32m"
    YELLOW = ansiScape + "33m"
    BLUE = ansiScape + "34m"
    PURPLE = ansiScape + "35m"
    CYAN = ansiScape + "36m"
    GREY = ansiScape + "37m"  # cor default
    DEFAULT = ansiScape + "m"



