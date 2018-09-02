from typing import Tuple

from colour import Colour


class Piece:
    def __init__(self,
                 colour: Colour,
                 is_king: bool = False):
        self.colour = colour
        self.is_king = is_king

    def promote(self):
        if self.is_king:
            raise ValueError("Cannot promote a piece that is already a king.")
        else:
            self.is_king = True

    def __repr__(self):
        return str(self.colour.value * (2 if self.is_king else 1))


if __name__ == "__main__":
    piece = Piece(Colour.WHITE, True)
    print(piece)