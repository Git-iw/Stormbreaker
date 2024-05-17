import pygame
import sys

class Board:
    size = 8
    square_size = 80  # Size of each square on the board

    @classmethod
    def draw(cls, screen):
        colors = [pygame.Color(0, 0, 0), pygame.Color(255, 255, 255)]  # Black and white
        for row in range(cls.size):
            for col in range(cls.size):
                color = colors[(row + col) % 2]
                pygame.draw.rect(screen, color, pygame.Rect(col * cls.square_size, row * cls.square_size, cls.square_size, cls.square_size))

def main():
    pygame.init()
    board_size = Board.size * Board.square_size
    screen = pygame.display.set_mode((board_size, board_size))
    pygame.display.set_caption('Stormbreaker Chess')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        Board.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()
