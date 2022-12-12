import pygame
from checkers.game import Game
from checkers.board import Board


class Checkers(Game):
    def __init__(self, window):
        """Initialize a new Checkers game.

        Args:
            window (Surface): The Pygame surface on which to draw the game.
        """
        super().__init__(window)
        self.selected = None

    def reset(self):
        """Reset the game state. This is called at the start of a new game.
        """
        self.initialize()

    def choose(self, r, c):
        """Select the piece at the given position.

        Args:
            r (int): The row of the piece to select.
            c (int): The column of the piece to select.

        Returns:
            bool: True if the selection was successful, False otherwise.
        """
        if self.selected:
        # If a piece is already selected, try to make a move with it
            result = self.checkers_move(r, c)
            if not result:
                # If the move is invalid, deselect the piece and try to select again
                self.selected = None
                self.choose(r, c)
        else:
            # If no piece is selected, check if the selected position can be selected
            self.can_be_selected(r, c)

    def can_be_selected(self,r,c):
        """Determine if the piece at the given position can be selected.

        Args:
            r (int): The row of the piece to select.
            c (int): The column of the piece to select.

        Returns:
            bool: True if the piece can be selected, False otherwise.
        """
        # Find the piece at the given position on the game board
        piece = self.board.find_piece(r, c)

        # Check if the piece exists and if it is the same color as the current turn
        if piece != 0 and piece.color == self.turn:
            # If the conditions are met, set the selected piece and get the valid moves for it
            self.selected = piece
            self.valid_moves = self.board.possible_moves(piece)
            return True

        return False

    def checkers_move(self, r, c):
        """Move the selected piece to the given position.

        Args:
            r (int): The row to move the piece to.
            c (int): The column to move the piece to.

        Returns:
            bool: True if the move was successful, False otherwise.
        """
        piece = self.board.find_piece(r, c)
        # Check if there is a selected piece and the chosen position is a valid move
        if self.selected and piece == 0 and (r, c) in self.valid_moves:
            self.choice_action(r, c)
            # Return True if move is successful
            return True
        # Return False if move is not successful
        return False


    def choice_action(self, r, c):
        """Perform the action associated with a move on the game board.

        Args:
            r (int): The row to move the piece to.
            c (int): The column to move the piece to.
        """
        # Move the selected piece to the specified position
        self.board.move(self.selected, r, c, self.window)

        # If there are any pieces to be skipped, remove them from the board
        skipped = self.valid_moves[(r, c)]
        if skipped:
            self.board.remove_piece(skipped)

        # Switch the turn to the other player
        self.switch_turn()



    def switch_turn(self):
        """Change the current player's turn.
        """
        self.valid_moves = {}
        # Switch the turn to the other player
        if self.turn == self.c.GREY:
            self.turn = self.c.WHITE
        else:
            self.turn = self.c.GREY
    

    
    