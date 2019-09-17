from chess.model.piece import Piece
from chess.util.convert import *


# Represents the core functionality of the game - board, pieces' management and basic operations i.e.
# move a piece, put a piece, remove a piece, clear the board and put the board in starting position
# This part doesn't contain the real in-game mechanics such as checking if king isn't under attack before move
# or not allowing queens jump over pieces etc.
#
# board: the list of lists represents the chessboard. Row indices represent letters (a-h), column indices
# represent numbers (8-1) - in the index order 0 to 7. I.e. a1 corresponds to board[0][7], e7 - to board[4][1]
# etc.
#
# white_pieces & black_pieces: these list store all the pieces of respective color.

class Game:
    board = [[]]

    def __init__(self):
        self.clear_board()

    def clear_board(self):
        self.board = [[Piece('NULL') for i in range(8)] for i in range(8)]

    def set_new_board(self):
        self.clear_board()
        self.board[1] = [Piece('BP') for i in range(8)]
        self.board[6] = [Piece('WP') for i in range(8)]

        self.board[0][0] = Piece('BR')
        self.board[0][1] = Piece('BN')
        self.board[0][2] = Piece('BB')
        self.board[0][3] = Piece('BQ')
        self.board[0][4] = Piece('BK')
        self.board[0][5] = Piece('BB')
        self.board[0][6] = Piece('BN')
        self.board[0][7] = Piece('BR')

        self.board[7][0] = Piece('WR')
        self.board[7][1] = Piece('WN')
        self.board[7][2] = Piece('WB')
        self.board[7][3] = Piece('WQ')
        self.board[7][4] = Piece('WK')
        self.board[7][5] = Piece('WB')
        self.board[7][6] = Piece('WN')
        self.board[7][7] = Piece('WR')

    def move_piece(self, src_field: str, trg_field: str):
        src_piece = self.board[ntf(src_field)[0]][ntf(src_field)[1]]
        trg_piece = self.board[ntf(trg_field)[0]][ntf(trg_field)[1]]
        piece_name = ctn(src_piece.p_type)

        #
        # # check if the source field doesn't contain pieces
        # if src_piece.p_type == 'NULL':
        #     print("This field doesn't contain any pieces!")
        #     return False
        #
        # # check if the target field isn't occupied by own piece
        # if src_piece.color == trg_piece.color:
        #     print("You can't move on your own pieces!")
        #     return False
        #
        # # todo: insert here the validation of the move by chess rules later

        self.board[ntf(trg_field)[0]][ntf(trg_field)[1]] = src_piece
        self.board[ntf(src_field)[0]][ntf(src_field)[1]] = Piece('NULL')

        return piece_name

    def put_piece(self, field: str, piece: str):
        self.board[ntf(field)[0]][ntf(field)[1]] = Piece(piece.upper())

    def remove_piece(self, field: str):
        piece_name = self.board[ntf(field)[0]][ntf(field)[1]]
        self.board[ntf(field)[0]][ntf(field)[1]] = Piece('NULL')

        return ctn(piece_name)
