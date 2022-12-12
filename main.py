
from checkers.constants import Constants
from checkers.checkers import Checkers
import pygame

class Main:
    def __init__(self):
        """Initialize the game window and constants"""
        pygame.init()
        self.c = Constants()
        self.window = pygame.display.set_mode((self.c.W, self.c.H))
        self.refresh = 60
        

    pygame.display.set_caption('Checkers')

    def get_row_col_from_mouse(self, pos):
        """
        Converts the given mouse position to a row and column on the checkerboard.
        This function takes in a mouse position and converts it to a row and column on the game board. 
        This is useful for determining which piece the player has clicked on.
        Args:
        pos (tuple): The (x, y) coordinates of the mouse position.
        Returns:
        tuple: The (row, col) coordinates on the game board corresponding to the given mouse position.
        """
        
        # Unpack the (x, y) coordinates of the mouse position
        x, y = pos
        # Calculate the row and column indices by dividing by the size of each square on the game board
        row = y // self.c.SQUARE
        col = x // self.c.SQUARE
        # Return the row and column as a tuple
        return row, col

    def game_loop(self, run, time, game):
        """
        Executes the game loop until the game is over or the player quits.
        This function manages the game loop, which is the core of the game. 
        It handles user input, updates the game state, and renders the game.

        Args:
        run (bool): A flag indicating whether the game should continue to run.
        time (Clock): The time object used to control the game's frame rate.
        game (Checkers): The main game object, which manages the state of the game.
        """
        
        while run:
        # Control the frame rate of the game
            time.tick(self.refresh)

            # Check if the game is over
            if game.winner() is not None:
                print(game.winner())
                run = False
            for event in pygame.event.get():
                # Check if the player has quit the game
                if event.type == pygame.QUIT:
                    run = False
                # Check if the player has clicked on the game board
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    # Convert the mouse position to row and column on the game board
                    row, col = self.get_row_col_from_mouse(pos)
                    game.choose(row, col)
                
            # Update the game state
            game.update()
    
    def main(self):
        """Run the main game loop"""

        # Set a flag indicating that the game should continue running
        run = True
        # Create a time object for controlling the game's frame rate
        time = pygame.time.Clock()
        # Create a Checkers game object
        game = Checkers(self.window)
        # Run the game loop until the game is over or the player quits
        self.game_loop(run, time, game)

        # Quit Pygame
        pygame.quit()

    

if __name__ == "__main__":
    m = Main()
    m.main() 


