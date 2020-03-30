from copy import deepcopy

from chess.util.metaclass.singleton import Singleton


class History(metaclass=Singleton):

    history = []
    cur_pos = -1
    can_redo = False

    def append(self, board):
        if self.can_redo and self.cur_pos != -1 and self.cur_pos < len(self.history):
            self.history = self.history[0:self.cur_pos+1]

        self.history.append(deepcopy(board))
        self.cur_pos += 1

        self.can_redo = False

    def undo(self):
        if self.cur_pos <= 0 or len(self.history) == 0:
            return [], "Cannot undo any further."

        self.cur_pos -= 1
        self.can_redo = True
        return deepcopy(self.history[self.cur_pos]), "success"

    def redo(self):
        if not self.can_redo or len(self.history) == 0 or self.cur_pos == -1 or self.cur_pos == len(self.history)-1:
            return [], "Cannot redo any further"

        self.cur_pos += 1
        return deepcopy(self.history[self.cur_pos]), "success"

    def reset(self):
        self.history = []
        self.cur_pos = -1
        self.can_redo = False