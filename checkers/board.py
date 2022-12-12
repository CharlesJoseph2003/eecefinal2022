import pygame
from checkers.constants import Constants
from checkers.piece import Piece
from checkers.angry_piece import AngryPiece

class Board:
    def __init__(self):
        """Initialize a new game board.
        """
        self.c = Constants()
        self.board = []
        self.grey_left = self.white_left = 12
        self.grey_kings = self.white_kings = 0
        self.build_board()

    def make_squares(self, window):
        """Draw the squares on the game board.

        Args:
            window (Surface): The Pygame surface on which to draw the game board.
        """
         # Fill the window with the color BLACK
        window.fill(self.c.BLACK)

        # Loop through all rows and columns of the game board
        for r in range(self.c.ROWS):
            for c in range(r % 2, self.c.COLS, 2):
                # Draw a square at the current row and column
                self.square(window, r, c)
    def square(self, window, r, c):
        """Draw a single square on the game board.

    Args:
        window (Surface): The Pygame surface on which to draw the game board.
        r (int): The row of the square to draw.
        c (int): The column of the square to draw.
    """
        #draws square
        pygame.draw.rect(window, self.c.GREY, (r * self.c.SQUARE, c * self.c.SQUARE,
                                                   self.c.SQUARE, self.c.SQUARE))

    def move(self, piece, r, c, window=None):
        """Move a piece on the game board.

    Args:
        piece (Piece): The piece to move.
        r (int): The row to move the piece to.
        c (int): The column to move the piece to.
        window (Surface, optional): The Pygame surface on which to draw the move.
            Defaults to None.
    """
        # Swap the piece at the current position with the piece at the new position
        self.board[piece.row][piece.col], self.board[r][c] = self.board[r][c], self.board[piece.row][piece.col]
        # Move the piece to the new position on the game board
        piece.move_piece(r, c, window)
        # If the moved piece reaches the opposite side of the board, make it a king
        self.make_king(piece, r)

    def make_king(self, piece, r):
        """Make a piece a king if it reaches the opposite end of the board.

    Args:
        piece (Piece): The piece to potentially promote.
        row (int): The row that the piece moved to.
    """
        # Check if the piece reached the top or bottom row of the board
        if r == self.c.ROWS - 1 or r == 0:
            # Promote the piece to a king
            piece.promote_king()

            # Increment the number of kings for the piece's color
            if piece.color == self.c.WHITE:
                self.white_kings += 1
            else:
                self.grey_kings += 1

    def find_piece(self, r, c):
        """Get the piece at the given position on the game board.

    Args:
        r (int): The row of the piece to get.
        c (int): The column of the piece to get.

    Returns:
        Piece: The piece at the given position, or 0 if there is no piece.
    """
        # Return the piece at the given position on the board
        return self.board[r][c]

    def build_board(self):
        """Create the initial state of the game board.
    """
        # Loop through all rows and columns of the game board
        for r in range(self.c.ROWS):
            # Append an empty list to represent the current row of the board
            self.board.append([])

            # Loop through all columns of the current row
            for c in range(self.c.COLS):
                # Create a piece at the current position on the board
                self.create_piece(r,c)

    def create_piece(self, r, c):
        """Create a piece at the given position on the game board.

    Args:
        r (int): The row of the piece to create.
        c (int): The column of the piece to create.
    """
         # Check if the current position should contain a piece
        if c % 2 == ((r + 1) % 2):
            # If the row is in the top three rows, create a white piece
            if r < 3:
                self.board[r].append(AngryPiece(r, c, self.c.WHITE))
            # If the row is in the bottom three rows, create a grey piece
            elif r > 4:
                self.board[r].append(AngryPiece(r, c, self.c.GREY))
            # Otherwise, append 0 to represent an empty position
            else:
                self.board[r].append(0)
        # If the current position should not contain a piece, append 0 to represent an empty position
        else:
            self.board[r].append(0)
        

    def draw_board(self, window):
        """Draw the game board and all of the pieces on it.

    Args:
        window (Surface): The Pygame surface on which to draw the game board.
    """
         # Draw the squares on the game board
        self.make_squares(window)

        # Loop through all rows and columns of the game board
        for r in range(self.c.ROWS):
            for c in range(self.c.COLS):
                # Get the piece at the current position on the board
                piece = self.board[r][c]

                # If there is a piece at the current position, draw it on the window
                if piece != 0:
                    piece.draw_piece(window)

    def remove_piece(self, pieces):
        """Remove a list of pieces from the game board.

    Args:
        pieces (list): A list of pieces to remove.
    """
        # Loop through all pieces in the list
        for piece in pieces:
            # Set the position of the piece on the board to 0 to represent an empty position
            self.board[piece.row][piece.col] = 0

            # If the piece is not 0 (i.e. it is a valid piece)
            if piece != 0:
                # Decrement the number of pieces for the piece's color
                if piece.color == self.c.GREY:
                    self.grey_left -= 1
                else:
                    self.white_left -= 1

    def winner(self):
        """Determine the winner of the game.

    Returns:
        str: The color of the winning player, or None if the game is not over.
    """
        # If there are no more grey pieces, white wins
        if self.grey_left <= 0:
            return self.c.WHITE
        # If there are no more white pieces, grey wins
        elif self.white_left <= 0:
            return self.c.GREY

        # If there are still pieces of both colors, the game is not over
        return None

    def possible_moves(self, piece):
        """Get a dictionary of valid moves for a given piece.

    Args:
        piece (Piece): The piece to get valid moves for.

    Returns:
        dict: A dictionary of valid moves, where the keys are tuples representing
            positions on the game board, and the values are the pieces that will
            be skipped if the move is made.
    """
        # Initialize an empty dictionary to store valid moves
        posible_moves = {}

        # Get the left and right columns relative to the current piece's position
        left_col = piece.col - 1
        right = piece.col + 1

        # Get the current piece's row
        r = piece.row

        # If the current piece is a grey piece or a king,
        # check for possible moves in the upward direction
        if piece.color == self.c.GREY or piece.king:
            # Update the dictionary of valid moves with the moves that are found
            posible_moves.update(self.move_left(r - 1, max(r - 3, -1), -1, piece.color, left_col))
            posible_moves.update(self.move_right(r - 1, max(r - 3, -1), -1, piece.color, right))

        # If the current piece is a white piece or a king,
        # check for possible moves in the downward direction
        if piece.color == self.c.WHITE or piece.king:
            # Update the dictionary of valid moves with the moves that are found
            posible_moves.update(self.move_left(r + 1, min(r + 3, self.c.ROWS), 1, piece.color, left_col))
            posible_moves.update(self.move_right(r + 1, min(r + 3, self.c.ROWS), 1, piece.color, right))
        # Return the dictionary of valid moves
        return posible_moves

    def move_left(self, start, stop, step, color, left, passed=[]):
        """
        Given the current board state, determine the possible moves that can be made by moving a piece
        left from the given start position.
        Args:
        - self: the Board instance to operate on
        - start: the starting position (a tuple of the form (row, col))
        - stop: the stopping position (a tuple of the form (row, col))
        - step: the number of rows to move for each step (1 for forward, -1 for backward)
        - color: the color of the piece to move (1 for white, 2 for black)
        - left: the number of columns to move left for each step
        - passed: a list of pieces that were jumped over (optional, default is [])
        Returns:
        A dictionary mapping from destination positions (tuples of the form (row, col)) to a list of
        pieces that were jumped over to reach that position.
        """
        posible_moves = {}
        removed = []
 
        # Calculate the possible moves.
        r = start
        while r != stop:
            # Stop if the current position is outside the board.
            if left < 0:
                break

            current = self.board[r][left]

            # If the current position is empty, it is a possible move.
            if current == 0:
                if passed and not removed:
                    # Stop if we have already jumped over a piece and no pieces were removed.
                    break
                elif passed:
                    posible_moves[(r, left)] = removed + passed
                else:
                    posible_moves[(r, left)] = removed

                # Recursively explore moves in other directions if any pieces were removed.
                if removed:
                    if step == -1:
                        r = max(r - 3, 0)
                    else:
                        r = min(r + 3, self.c.ROWS)
                    posible_moves.update(self.move_left(r + step, r, step, color, left - 1, passed=removed))
                    posible_moves.update(self.move_right(r + step, r, step, color, left + 1, passed=removed))
                break
            # Stop if we encounter a piece of the same color.
            elif current.color == color:
                break
            # Otherwise, remove the piece.
            
            else:              
                removed = [current]

            left -= 1

        return posible_moves

    #same as move_left function but in right direction
    def move_right(self, start, stop, step, color, right, passed=[]):
        """
        This function moves the checker piece to the right and calculates
        the possible moves for the piece.

        Args:
            start: The starting row of the checker piece.
            stop: The ending row of the checker piece.
            step: The step size of the checker piece, can be 1 or -1.
            color: The color of the checker piece.
            right: The starting column of the checker piece.
            passed: The list of checker pieces that have been jumped over.
        Returns:
            posible_moves: A dictionary containing the possible moves for the checker piece.
        """
        posible_moves = {}
        removed = []
        r = start
        
        while start != stop:
            # If the checker piece has reached the end of the board, break the loop
            if right >= self.c.COLS:
                break

            current = self.board[r][right]

            if current == 0:
                # If the checker piece has jumped over any other checker pieces, 
                # add them to the list of possible moves
                if passed and not removed:
                    break
                elif passed:
                    posible_moves[(r, right)] = removed + passed
                else:
                    posible_moves[(r, right)] = removed

                # If the checker piece has removed any checker pieces, 
                # calculate the possible moves in the left and right direction
                if removed:
                    if step == -1:
                        r = max(r - 3, 0)
                    else:
                        r = min(r + 3, self.c.ROWS)
                    posible_moves.update(self.move_left(r + step, r, step, color, right - 1, passed=removed))
                    posible_moves.update(self.move_right(r + step, r, step, color, right + 1, passed=removed))
                break
            elif current.color == color:
                # If the checker piece has reached another checker piece of the same color, break the loop
                break
            else:
                # If the checker piece has reached another checker piece of a different color, 
                # add it to the list of removed pieces
                removed = [current]

            right += 1

        return posible_moves
