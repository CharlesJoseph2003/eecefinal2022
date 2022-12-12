import pygame


class Constants:
    def __init__(self):
        """
        Initialize Constants
        """
        # rgb
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.GREY = (128, 128, 128)
        self.W, self.H = 600, 600
        self.ROWS, self.COLS = 8, 8
        self.SQUARE = self.W // self.COLS
        self.PROMOTE = pygame.transform.scale(pygame.image.load('crown_image.png'), (44, 25))
