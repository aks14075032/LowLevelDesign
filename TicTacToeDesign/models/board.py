class Board:
    def __init__(self, size=3):
        self.board = [['' for _ in range(size)] for _ in range(size)]

    def get_board(self):
        return self.board

    def add_piece_to_board(self, x, y, piece):
        if self.board[x][y] != '':
            return False
        self.board[x][y] = piece
        return True

    def print_board(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                print(self.board[i][j], end=" |")
            print("\n")

    def is_free_space(self):
        count = 0
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == '':
                    count += 1
        return count > 0

