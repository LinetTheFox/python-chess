from chess.cview.util.symbols import *


class Piece:
    # False - black piece, True - white
    p_type = ''
    color = ''

    def __init__(self, p_type: str):
        self.p_type = p_type
        if p_type.startswith("W"):
            color = 'white'
        else:
            color = 'black'

    def __str__(self):
        return globals()[self.p_type]
