from chess.control import actions
from chess.history.history import History

history = History()


def execute(cmd, game):

    if cmd == '':
        return "Please enter a non-empty valid command! (start, move, remove, put, clear)"

    parts = cmd.split(" ")

    if parts[0] == 'move':
        return actions.move(parts, game, history)
    elif parts[0] == 'put':
        return actions.put(parts, game)
    elif parts[0] == 'remove':
        return actions.remove(parts, game)
    elif parts[0] == 'start':
        return actions.start(game, history)
    elif parts[0] == 'clear':
        return actions.clear(parts, game, history)
    elif parts[0] == 'undo':
        return actions.undo(game, history)
    elif parts[0] == 'redo':
        return actions.redo(game, history)
    else:
        return f"Unknown command: {parts[0]}"

