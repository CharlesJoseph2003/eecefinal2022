import pygame
from checkers.piece import Piece
import random


class AngryPiece(Piece):
    def __init__(self, row, col, color):
        """
        Initialize a new trash-talking checker piece at the given row and column, with the given color.
        """
        super().__init__(row, col, color)

    def move_piece(self, row, col, window=None):
        """
        Move the piece to the given row and column, and display a randomly chosen trash-talking message in the Pygame window.

        :param row: the new row in which to place the piece
        :type row: int
        :param col: the new column in which to place the piece
        :type col: int
        :param window: the pygame window in which the piece will be drawn and the trash-talking message will be displayed
        :type window: pygame.Surface
        """
        super().move_piece(row, col)
        trash_talk_phrases = [
            "I'm gonna crush you!",
            "You don't stand a chance against me!",
            "I'm the king of the checkerboard!",
            "You're no match for my checker skills!",
            "I'm the greatest checker player of all time!",
            "You're going down, buddy!",
            "I'm gonna wipe the floor with you!",
            "You're gonna regret challenging me to a game of checkers!",
            "I'm gonna make you look like a beginner!",
            "You're gonna be begging for mercy by the time I'm done with you!",
            "I'm the master of checkers and you're just a pawn in my game!",
            "You don't have what it takes to beat me!",
            "I'm gonna make you wish you never picked up a checker!",
            "You're gonna regret the day you crossed paths with me!",
            "I'm gonna teach you a lesson in checkers you'll never forget!",
            "You're gonna be sorry you ever challenged me to a game!",
            "I'm the best checker player in the world and there's nothing you can do about it!",
            "You're gonna be crying like a baby when I'm done with you!",
            "I'm the undisputed champion of checkers and you're just a rookie!",
            "You're gonna wish you stayed home and played with your dolls instead of challenging me!",
            "I'm the greatest checker player who ever lived and you're just a poor excuse for a player!",
            "You're gonna be begging me to stop once I get started!",
            "I'm the master of the checkerboard and you're just a mere mortal!",
            "You're gonna be begging for mercy once I get my checkers on the board!",
            "I'm the champion of checkers and there's nothing you can do to stop me!",
            "You're gonna regret the day you ever met me on the checkerboard!",
            "I'm the king of the checkerboard and you're just a measly pawn in my game!",
            "You're gonna be begging me to let you go once I get started with my checkers!",
            "I'm the master of checkers and there's nothing you can do to stop me from crushing you!"
        ]
        trash_talk = random.choice(trash_talk_phrases)

        # Display the trash-talking message in the Pygame window
        font = pygame.font.SysFont("comicsans", 30)
        text = font.render(trash_talk, 1, self.color)
        print(trash_talk)

        window.blit(text, (self.x - text.get_width() // 2, self.y - text.get_height() // 2))