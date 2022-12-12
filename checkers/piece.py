from checkers.constants import Constants
import pygame


class Piece:
    OUTLINE = 2

    def __init__(self, row, col, color, window=None):
        """Initialize a new piece.
        """
        self.c = Constants()
        self.window = window
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.row = row
        self.col = col
        self.find_pos()
        
    def __repr__(self):
        """
        Return a string representation of the piece's color.
        """
        return str(self.color)

    def find_pos(self):
        """
        Calculate the pixel coordinates of the center of the piece.
        """
        self.y = self.c.SQUARE * self.row + self.c.SQUARE // 2
        self.x = self.c.SQUARE * self.col + self.c.SQUARE // 2

    

    def draw_piece(self, window):
        """
        Draw the piece on the given pygame window.

        :param window: the pygame window on which to draw the piece
        :type window: pygame.Surface
        """
        # Calculate the radius of the piece as half the size of a square on the game board
        radius = self.c.SQUARE // 2
        # Draw a circle on the window with the given color at the calculated coordinates and with the calculated radius
        pygame.draw.circle(window, self.color, (self.x, self.y), radius - 5) 
        # If the piece is a king, draw the promotion image on the window centered on the piece's position
        if self.king:
            window.blit(self.c.PROMOTE, (self.x - self.c.PROMOTE.get_width() // 2, self.y - self.c.PROMOTE.get_height() // 2))

    def move_piece(self, row, col, window=None):
        """
        Move the piece to the given row and column.
        The window parameter is the pygame window in which the piece will be drawn.

        :param row: the new row in which to place the piece
        :type row: int
        :param col: the new column in which to place the piece
        :type col: int
        :param window: the pygame window in which the piece will be drawn
        :type window: pygame.Surface
        """
        # Update the piece's row and column attributes
        self.row = row
        self.col = col
        # Calculate the pixel coordinates of the piece's center
        self.find_pos()
    
    def promote_king(self):
        """
        Promote the piece to a king by setting its 'king' attribute to True.
        """ 
        self.king = True

    
