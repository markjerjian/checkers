class Board:
    def __init__(self, size: int = 8):
        self.size = size
        self.board = [[0] * self.size] * self.size

    def __repr__(self):
        return "Board({})".format(self.size)

    def __str__(self):
        return "\n".join([" ".join(str(square) for square in row)
                          for row in self.board])


if __name__ == "__main__":
    board = Board(size=4)

    print(board)
