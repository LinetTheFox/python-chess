from chess.cview.util.symbols import *


class Piece:
    # False - black piece, True - white
    p_type = ''
    color = ''

    def __init__(self, p_type: str):
        self.p_type = p_type
        if p_type.startswith("W"):
            self.color = 'white'
        elif p_type.startswith("B"):
            self.color = 'black'
        else:
            self.color = 'none'

    def __repr__(self):
        return globals()[self.p_type]
