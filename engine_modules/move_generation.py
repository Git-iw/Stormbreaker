# this file will not have the entire logic of search and eval, it will just have basic logic the main engine will have to end and start the game.

from bitboard import Bitboard

def setup_board() -> None:
    bitboard = Bitboard()
    bitboard.set_bit(0, "white", "rook")
    bitboard.set_bit(1, "white", "knight")
    bitboard.set_bit(2, "white", "bishop")
    bitboard.set_bit(3, "white", "queen")
    bitboard.set_bit(4, "white", "king")
    bitboard.set_bit(5, "white", "bishop")
    bitboard.set_bit(6, "white", "knight")
    bitboard.set_bit(7, "white", "rook")
    bitboard.set_bit(8, "white", "pawn")
    bitboard.set_bit(9, "white", "pawn")
    bitboard.set_bit(10, "white", "pawn")
    bitboard.set_bit(11, "white", "pawn")
    bitboard.set_bit(12, "white", "pawn")
    bitboard.set_bit(13, "white", "pawn")
    bitboard.set_bit(14, "white", "pawn")
    bitboard.set_bit(15, "white", "pawn")
    bitboard.set_bit(63, "black", "rook")
    bitboard.set_bit(62, "black", "knight")
    bitboard.set_bit(61, "black", "bishop")
    bitboard.set_bit(60, "black", "king")
    bitboard.set_bit(59, "black", "queen")
    bitboard.set_bit(58, "black", "bishop")
    bitboard.set_bit(57, "black", "knight")
    bitboard.set_bit(56, "black", "rook")
    bitboard.set_bit(55, "black", "pawn")
    bitboard.set_bit(54, "black", "pawn")
    bitboard.set_bit(53, "black", "pawn")
    bitboard.set_bit(52, "black", "pawn")
    bitboard.set_bit(51, "black", "pawn")
    bitboard.set_bit(50, "black", "pawn")
    bitboard.set_bit(49, "black", "pawn")
    bitboard.set_bit(48, "black", "pawn")
    bitboard.print_board()

def main():
    setup_board()
    # move input should be in a classic chess notation format.
    # logic to handle the move input given by user eg: conversion from notation to bitboard methods.
    # Take that input from the user and print it immediately.
    ...

if __name__ == "__main__":
    main()