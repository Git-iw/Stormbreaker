class Bitboard:
    def __init__(self, black_board=0, white_board=0):
        self.white_board = white_board 
        self.black_board = black_board
        self.pieces = ["pawn", "knight", "bishop", "rook", "queen", "king"]

    def set_bit(self, position: int, color: str, piece: str):
        color = color.lower()
        piece = piece.lower()
        if piece not in self.pieces:
            raise ValueError("Given name must be of a piece in chess!")
        if color == "white":
            self.white_board |= 1 << position
        elif color == "black":
            self.black_board |= 1 << position
        else:
            raise ValueError("Given color must be either black or white!")

    def clear_bit(self, position: int, color: str, piece: str):
        color = color.lower()
        piece = piece.lower()
        # After the equal to sign, we give the code in brackets which says move 1 to the position,
        # but the NOT symbol inverts it resulting in clearing the bit
        # at the equal to sign, we use AND symbol to remove the bit if it is 1 and remain 0 if it was
        if piece not in self.pieces:
            raise ValueError("Given name must be of a piece in chess!")
        if not (0 <= position <= 63):
            raise ValueError("Given bit is not within the board range!")
        if color == "white":
            self.white_board &= ~(1 << position)
        elif color == "black":
            self.black_board &= ~(1 << position)
        else:
            raise ValueError("Given color must be either black or white!")
        
    def is_bit_set(self, position: int, color: str, piece: str) -> bool: # As it will return either 0 or 1
        color = color.lower()
        piece = piece.lower()
        if piece not in self.pieces:
            raise ValueError("Given name must be of a piece in chess!")
        if not (0 <= position <= 63):
            raise ValueError("Given bit is not within the board range!")
        # It should return 1 if 1 is in the number mentioned of position
        if color == "white":
            return (self.white_board & (1 << position)) != 0
        elif color == "black":
            return (self.black_board & (1 << position)) != 0
        else:
            raise ValueError("Given color must be either black or white!")

    def print_board(self) -> None:
        """Prints a visual representation of the bitboard (for debugging)."""
        for rank in range(7, -1, -1):
            print(f"{rank + 1} ", end='')
            for file in range(8):
                position = rank * 8 + file
                if self.is_bit_set(position, 'black', 'pawn'):
                    print('p', end=' ')
                elif self.is_bit_set(position, 'black', 'knight'):
                    print('n', end=' ')
                elif self.is_bit_set(position, 'black', 'bishop'):
                    print('b', end=' ')
                elif self.is_bit_set(position, 'black', 'rook'):
                    print('r', end=' ')
                elif self.is_bit_set(position, 'black', 'queen'):
                    print('q', end=' ')
                elif self.is_bit_set(position, 'black', 'king'):
                    print('k', end=' ')
                elif self.is_bit_set(position, 'white', 'pawn'):
                    print('P', end=' ')
                elif self.is_bit_set(position, 'white', 'knight'):
                    print('N', end=' ')
                elif self.is_bit_set(position, 'white', 'bishop'):
                    print('B', end=' ')
                elif self.is_bit_set(position, 'white', 'rook'):
                    print('R', end=' ')
                elif self.is_bit_set(position, 'white', 'queen'):
                    print('Q', end=' ')
                elif self.is_bit_set(position, 'white', 'king'):
                    print('p', end=' ')
                else:
                    print('0', end=' ')
            print(f"{rank + 1}")
        print("  a b c d e f g h")

def main():
    # These are just random positions in which bits are placed, nothing special.
    # Commented out because piece implementation is still left.
    bitboard = Bitboard()
    bitboard.set_bit(0, "white", "rook")
    bitboard.set_bit(63, "black", "rook")
    bitboard.set_bit(3, "white", "king")
    bitboard.set_bit(60, "black", "king")
    bitboard.print_board()

if __name__ == "__main__":
    main()
    # Yes, I will stop camel case for most of the part.
    # I will start to use type annotations just for my understanding sake.
    # have more plans on changes like in print_board function, advanced bitboard for pieces, and will use these functions in move_generation.py