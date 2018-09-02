from piece import Piece
from square import Square
from colour import Colour

class Board:
    def __init__(self):
        self.size = 8
        self.board = self.new_board()

    def __repr__(self):
        return "Board({})".format(self.size)

    def __str__(self):
        return "\n".join([" ".join(str(square.color) for square in row)
                          for row in self.board])

    def new_board(self):

        board_matrix = [[None] * self.size] * self.size

        # set square colours
        for x in range(self.size):
            for y in range(self.size):
                if x % 2 == 0:
                    if y % 2 == 0:
                        board_matrix[x][y] = Square(Colour.WHITE)
                    else:
                        board_matrix[x][y] = Square(Colour.BLACK)
                else:
                    if y % 2 == 0:
                        board_matrix[x][y] = Square(Colour.BLACK)
                    else:
                        board_matrix[x][y] = Square(Colour.WHITE)

        # set up pieces
        for y in range(self.size):
            for x in range(3):
                if board_matrix[x][y].color == Colour.BLACK:
                    board_matrix[x][y].occupant = Piece(Colour.WHITE)
            for x in range(5, self.size):
                if board_matrix[x][y].color == Colour.BLACK:
                    board_matrix[x][y].occupant = Piece(Colour.BLACK)

        return board_matrix

    def remove_piece(self, x, y):
        self.board[x][y] = None

    def move_piece(self, start_x, start_y, end_x, end_y):

        self.board[end_x][end_y].occupant = self.board[start_x][start_y].occupant
        self.remove_piece(start_x, start_y)

        if self.board[end_x][end_y].occupant is not None:
            if (self.board[end_x][end_y].occupant.color == Colour.BLACK and end_y == 0) or (
                            self.board[end_x][end_y].occupant.color == Colour.WHITE and end_y == self.size - 1):
                self.board[end_x][end_y].occupant.king = True

if __name__ == "__main__":
    board = Board()
    print(board)