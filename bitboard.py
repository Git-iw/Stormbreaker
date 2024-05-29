class Bitboard:
    def __init__(self, board=0): # Not requried to use type annotation as I know it
        self.board = board # It is initialized 0 because I will use bitwise operators, If i can.

    def set_bit(self, postition: int):
        ...
    
    def clear_bit(self, position: int):
        ...
    
    def isBit_set(self, position: int):
        ...
    
    def print_board(self) -> None:
        """Prints a visual representation of the bitboard (for debugging)."""
        ...

def main():
    bitboard = Bitboard(8)
    bitboard.print_board()

if __name__ == "__main__":
    main()
    # Yes, I will stop camel case for most of the part.
    # I will start to use type annotations just for my understanding sake.