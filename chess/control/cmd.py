from chess.model.game import Game


def execute(cmd: str, game: Game) -> bool:

    if cmd == '':
        # todo: retry
        return False

    parts = cmd.split(" ", 3)

    if parts[0] == 'move':
        game.move_piece(parts[1], parts[2])
        # move a piece in given space to desired space
        return True

    elif parts[0] == 'put':
        game.put_piece(parts[1], parts[2])
        # place a new piece to desired space
        return True

    elif parts[0] == 'remove':
        # todo
        # remove a piece from the space
        return True

    elif parts[0] == 'start':
        game.set_new_board()
        # start the new game
        return True

    elif parts[0] == 'clear':
        # todo
        # clear the board
        return True

    else:
        print(f'Unknown command: {parts[0]}')
        return False
