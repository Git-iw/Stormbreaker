class Bitboard:
    def __init__(self,piece: str ,black_board=0, white_board=0): # Not requried to use type annotation as I know it
        self.white_board = white_board 
        self.black_board = black_board
        self.piece = piece

    def set_bit(self, position: int, color: str, piece: str):
        color = color.lower()
        piece = piece.lower()
        if not (0 <= position <= 63):
            raise ValueError("Given bit is not within the board range!")
        if color == "black":
            self.black_board |= 1 << position
        elif color == "white":
            self.white_board |= 1 << position
        else:
            raise ValueError(" Given color must be either black or white!")

        # self.board |= 1 << position # The 1(bit) will be moved by the number given below in the main
    
    def clear_bit(self, position: int, color: str, piece: str):
        color = color.lower()
        piece = piece.lower()
        if not (0 <= position <= 63):
            raise ValueError("Given bit is not within the board range!")

         # After the equal to sign, we give the code in brackets which says move 1 to the position,
                                       # but the NOT symbol inverts it resulting in clearing the bit
                                       # at the equal to sign, we use AND symbol to remove the bit if it is 1 and remain 0 if is was
        if color == "white":
            self.white_board &= ~(1 << position)
        elif color == "black":
            self.black_board &= ~(1 << position)
        else:
            raise ValueError("Given color must be either black or white!")
        ...
    
    def is_bit_set(self, position: int, color: str, piece: str) -> bool: # As it will return either 0 or 1
        color = color.lower()
        piece = piece.lower()
        if not (0 <= position <= 63):
            raise ValueError("Given bit is not within the board range!")

        # It should return 1 if 1 is in the number mentioned of position
        if color == "white":
            return (self.white_board & 1 << position) != 0
        elif color == "black":
            return (self.black_board & 1 << position) != 0
        else:
            raise ValueError("Given color must be either black or white!")
        ...

    def print_board(self) -> None:
        """Prints a visual representation of the bitboard (for debugging)."""
        # piece implementation will start soon, so until then shanthi karo, it will work for sure.
        for rank in range(7, -1, -1):
            print(f"{rank + 1} ", end='')
            for file in range(8):
                position = rank * 8 + file
                if self.is_bit_set(position, 'black'):
                    print('B', end=' ')
                elif self.is_bit_set(position, 'white'):
                    print('W', end=' ')
                else:
                    print('0', end=' ')
            print(f"{rank + 1}")
        print("  a b c d e f g h")

def main():
    # These are just random positions in which bits are placed, nothing special.
    # Commented out because piece implementation is still left.
    # bitboard = Bitboard()
    # bitboard.set_bit(0, "white")
    # bitboard.set_bit(63, "black")
    # bitboard.set_bit(53, "black")
    # bitboard.set_bit(10, "white")
    # bitboard.set_bit(43, "black")
    # bitboard.set_bit(20, "white")
    # bitboard.print_board()
    ...

if __name__ == "__main__":
    main()
    # Yes, I will stop camel case for most of the part.
    # I will start to use type annotations just for my understanding sake.
    # have more plans on changes like in print_board function, advanced bitboard for pieces, and will use these functions in move_generation.py