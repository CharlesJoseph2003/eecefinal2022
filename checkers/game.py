from checkers.constants import Constants
from checkers.board import Board
import pygame


class Game:
    def __init__(self, window):
        """
        Initializes Game

        window (Window): The game window where the game is rendered.
        """
        self.c = Constants()
        self.turn = None
        self.valid_moves = None
        self.initialize()
        self.window = window


    def initialize(self):
        """Initialize the game state. This is called at the start of a game.
        """
        self.turn = self.c.GREY
        self.valid_moves = {}
        self.selected = None
        self.board = Board()

    def update(self):
        """Update the game state. This should be called every frame.
        """
        # Draw the game board and all of the pieces on it
        self.board.draw_board(self.window)
        # Update the Pygame display with the new game state
        pygame.display.update()
        

    def winner(self):
            """Determine the winner of the game.

            Returns:
                str: The color of the winning player, or None if there is no winner.
            """
            return self.board.winner()


