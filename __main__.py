import os
import getpass

from chess.cview.chessboard import Chessboard
from chess.control.cmd import execute
from chess.model.game import Game

os.system('cls' if os.name == 'nt' else 'clear')

chessboard = Chessboard()
game = Game()
first_draw = True


while True:

    if first_draw:
        chessboard.draw_empty_board()
        first_draw = False

    command = input(f"[{getpass.getuser()}]$ ")

    os.system('cls' if os.name == 'nt' else 'clear')

    if command == 'exit':
        os.system('cls' if os.name == 'nt' else 'clear')
        exit(0)

    execute(command, game)
    chessboard.draw_board(game.board)

