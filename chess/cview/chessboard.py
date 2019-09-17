class Chessboard:

    def __init__(self):
        pass

    def clear(self):
        import os
        os.system('cls' if os.name == 'nt' else 'clear')

    def draw_empty_board(self):
        self.clear()
        print("┌───┬───┬───┬───┬───┬───┬───┬───┐")
        j = 0
        for i in range(15):
            if i % 2 == 0:
                print(f"│   │   │   │   │   │   │   │   │ {8-j}")
                j += 1
            else:
                print("├───┼───┼───┼───┼───┼───┼───┼───┤")
        print("└───┴───┴───┴───┴───┴───┴───┴───┘")
        print("  a   b   c   d   e   f   g   h")

    def draw_board(self, board: []):
        self.clear()
        j = 0
        print("┌───┬───┬───┬───┬───┬───┬───┬───┐")
        for i in range(15):
            if i % 2 == 0:
                print(f"│ {board[j][0]} │ {board[j][1]} │ {board[j][2]} │ {board[j][3]} │ {board[j][4]} │ {board[j][5]} │ {board[j][6]} │ {board[j][7]} │ {8-j}")
                j += 1
            else:
                print("├───┼───┼───┼───┼───┼───┼───┼───┤")

        print("└───┴───┴───┴───┴───┴───┴───┴───┘")
        print("  a   b   c   d   e   f   g   h")
