from chess.model.game import Game
from chess.control.validation import *
from chess.model.history.history import History
from chess.util.convert import *


history = History()


def execute(cmd: str, game: Game) -> str:

    if cmd == '':
        return "Please enter a non-empty valid command! (start, move, remove, put, clear)"

    parts = cmd.split(" ")

    if parts[0] == 'move':

        if len(parts) > 3:
            return "Too many command arguments! Command 'move' only takes two!"

        if not validate_field(parts[1]):
            return f"First and second arguments must be field names, your first field name {parts[1]} is invalid!"

        if not validate_field(parts[2]):
            return f"First and second arguments must be field names, your second field name {parts[2]} is invalid!"

        (result, status) = game.move_piece(parts[1], parts[2])

        if not result:
            return status

        history.append(game.board)

        return f"Moved a {status} from {parts[1]} to {parts[2]}."

    elif parts[0] == 'put':

        if len(parts) > 3:
            return "Too many command arguments! Command 'put' only takes two!"

        if not validate_field(parts[1]):
            return f"First argument should be field name, your first argument {parts[1]} is invalid!"

        if not validate_piece(parts[2]):
            return f"Second argument should be piece code, your second argument {parts[2]} is invalid!"

        game.put_piece(parts[1], parts[2])
        return f"Put a {ctn(parts[2])} on field {parts[1]}."

    elif parts[0] == 'remove':

        if not (validate_field(parts[1])):
            return f"Parameter should be a field name, your parameter {parts[1]} is invalid!"

        piece_name = game.remove_piece(parts[1])

        return f"Removed the {piece_name} from field {parts[1]}."

    elif parts[0] == 'start':
        game.set_new_board()
        history.reset()
        history.append(game.board)
        return "Started a new game."

    elif parts[0] == 'clear':
        game.clear_board()
        history.reset()
        return "Cleared the board."

    elif parts[0] == 'undo':
        (board, status) = history.undo()
        if status != "success":
            return status
        game.set_board(board)
        return "Undid a move."

    elif parts[0] == 'redo':
        (board, status) = history.redo()
        if status != "success":
            return status
        game.set_board(board)
        return "Redid a move."
    else:
        return f"Unknown command: {parts[0]}"
