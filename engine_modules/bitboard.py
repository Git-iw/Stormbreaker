class Bitboard:
    def __init__(self):
        self.board = {}
        self.pieces = ["pawn", "knight", "bishop", "rook", "queen", "king"]
        self.colors = ["white", "black"]

    def set_bit(self, position: int, color: str, piece: str):
        color = color.lower()
        piece = piece.lower()
        if piece not in self.pieces:
            raise ValueError("Given name must be of a piece in chess!")
        if not (0 <= position <= 63):
            raise ValueError("Given bit is not within the board range!")
        self.board[position] = (color, piece)

    def clear_bit(self, position: int):
        if not (0 <= position <= 63):
            raise ValueError("Given bit is not within the board range!")
        if position in self.board:
            del self.board[position]
        # After the equal to sign, we give the code in brackets which says move 1 to the position,
        # but the NOT symbol inverts it resulting in clearing the bit
        # at the equal to sign, we use AND symbol to remove the bit if it is 1 and remain 0 if it was

    def is_bit_set(self, position: int, color: str, piece: str) -> bool:
        color = color.lower()
        piece = piece.lower()
        if piece not in self.pieces:
            raise ValueError("Given name must be of a piece in chess!")
        if not (0 <= position <= 63):
            raise ValueError("Given bit is not within the board range!")
        return self.board.get(position) == (color, piece)

    def print_board(self) -> None:
        """Prints a visual representation of the bitboard (for debugging)."""
        piece_symbols = {
            'pawn': 'P',
            'knight': 'N',
            'bishop': 'B',
            'rook': 'R',
            'queen': 'Q',
            'king': 'K'
        }
        print("  a b c d e f g h")
        for rank in range(7, -1, -1):
            print(f"{rank + 1} ", end='')
            for file in range(8):
                position = rank * 8 + file
                if position in self.board:
                    color, piece = self.board[position]
                    symbol = piece_symbols[piece]
                    if color == 'black':
                        symbol = symbol.lower()
                    print(symbol, end=' ')
                else:
                    print('0', end=' ')
            print(f" {rank + 1}")
        print("  a b c d e f g h")

def main():
    # Example to set a rook at position 0
    bitboard = Bitboard()
    bitboard.set_bit(0, "white", "rook")
    bitboard.set_bit(1, "white", "knight")
    bitboard.set_bit(2, "white", "bishop")
    bitboard.set_bit(3, "white", "queen")
    bitboard.set_bit(4, "white", "king")
    bitboard.set_bit(5, "white", "bishop")
    bitboard.set_bit(6, "white", "knight")
    bitboard.set_bit(7, "white", "rook")
    bitboard.set_bit(63, "black", "rook")
    bitboard.set_bit(62, "black", "knight")
    bitboard.set_bit(61, "black", "bishop")
    bitboard.set_bit(60, "black", "king")
    bitboard.set_bit(59, "black", "queen")
    bitboard.set_bit(58, "black", "bishop")
    bitboard.set_bit(57, "black", "knight")
    bitboard.set_bit(56, "black", "rook")
    bitboard.print_board()

if __name__ == "__main__":
    main()
    # Yes, I will stop camel case for most of the part.
    # I will start to use type annotations just for my understanding sake.
    # have more plans on changes like in print_board function, advanced bitboard for pieces, and will use these functions in move_generation.py