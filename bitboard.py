class Bitboard:
    def __init__(self, board=0): # Not requried to use type annotation as I know it
        self.board = board # It is initialized 0 because I will use bitwise operators, If i can.

    def set_bit(self, position: int):
        if not (0 <= position <= 63):
            raise ValueError("Given bit is not within the board range!")

        self.board |= 1 << position # The 1(bit) will be moved by the number given below in the main
    
    def clear_bit(self, position: int):
        if not (0 <= position <= 63):
            raise ValueError("Given bit is not within the board range!")

        self.board &= ~(1 << position) # After the equal to sign, we give the code in brackets which says move 1 to the position,
                                       # but the NOT symbol inverts it resulting in clearing the bit
                                       # at the equal to sign, we use AND symbol to remove the bit if it is 1 and remain 0 if is was
        ...
    
    def is_bit_set(self, position: int) -> bool: # As it will return either 0 or 1
        if not (0 <= position <= 63):
            raise ValueError("Given bit is not within the board range!")

        return (self.board & 1 << position) != 0 # It should return 1 if 1 is in the number mentioned of position
        ...

    def print_board(self) -> None:
        """Prints a visual representation of the bitboard (for debugging)."""
        print("  a b c d e f g h")
        for rank in range(7, -1, -1):
            print(f"{rank + 1} ", end='')
            for file in range(8):
                position = rank * 8 + file
                print("R" if self.is_bit_set(position) else '0', end=' ') # R for ready, and 0 for not ready, it will be confusing as there will be rank numbering as well
            print(f"{rank + 1}")
        print("  a b c d e f g h")

def main():
    bitboard = Bitboard(8)
    bitboard.set_bit(0)
    bitboard.set_bit(6)
    bitboard.set_bit(63)
    bitboard.set_bit(56)
    bitboard.print_board()

if __name__ == "__main__":
    main()
    # Yes, I will stop camel case for most of the part.
    # I will start to use type annotations just for my understanding sake.