import pytest
import pygame
from checkers.board import Board
from checkers.constants import Constants
from checkers.piece import Piece
from checkers.checkers import Checkers


class Testing:

    @pytest.mark.run
    def test_move(self):
        b = Board()
        assert b.grey_left == 12

    def test_find_pos(self):
        # Create a new Piece object with row=3, col=4, and color=(255, 0, 0)
        piece = Piece(4, 4, (255,0,0))

        # Call the find_pos method
        piece.find_pos()

        # Check that the Piece object has the correct x and y coordinates
        assert piece.x == 337
        assert piece.y == 337
    def test_piece_promote_king():
        # Test that a Piece instance can be promoted to a king
        piece = Piece(0, 0, 'white')
        piece.promote_king()
        assert piece.king == True
    def test_piece_move():
        # Test that a Piece instance can be moved to a new position
        piece = Piece(0, 0, 'white')
        piece.move_piece(1, 1)
        assert piece.row == 1
        assert piece.col == 1
    def test_piece_draw_piece():
    # Test that the draw_piece method correctly draws the piece on the given window
        window = pygame.Surface((80, 80))
        piece = Piece(1, 2, (255, 0, 0), window=window)
        piece.draw_piece(window)
        # Check that a circle was drawn on the window at the correct coordinates
        # and with the correct color
        assert window.get_at((40, 40)) == (255, 0, 0, 255)
    def test_choose():
        # Test selecting a piece that can be selected
        game = Checkers(pygame.display.set_mode((600,600)))
        game.board.add_piece(Piece(3, 4, (255,255,255)))
        assert game.choose(3, 4) == True
        assert game.selected == Piece(3, 4, (255,255,255))
        assert game.valid_moves == {(2, 3): [], (2, 5): []}
        
        # Test selecting a piece that cannot be selected
        game = Checkers(pygame.display.set_mode((600,600)))
        game.board.add_piece(Piece(3, 4, (255,255,255)))
        assert game.choose(3, 5) == False
        assert game.selected == None
        assert game.valid_moves == {}
    def test_can_be_selected():
        # Test selecting a piece that can be selected
        game = Checkers(pygame.display.set_mode((600,600)))
        game.board.add_piece(Piece(3, 4, (255,255,255)))
        assert game.can_be_selected(3, 4) == True
        assert game.selected == Piece(3, 4, (255,255,255))
        assert game.valid_moves == {(2, 3): [], (2, 5): []}
        
        # Test selecting a piece that cannot be selected
        game = Checkers(pygame.display.set_mode((600,600)))
        game.board.add_piece(Piece(3, 4, (255,255,255)))
        assert game.can_be_selected(3, 5) == False
        assert game.selected == None
        assert game.valid_moves == {}
    def test_checkers_move():
        # Test making a valid move
        game = Checkers(pygame.display.set_mode((600,600)))
        game.board.add_piece(Piece(3, 4, (255,255,255)))
        game.selected = Piece(3, 4, (255,255,255))
        game.valid_moves = {(2, 3): [], (2, 5): []}
        assert game.checkers_move(2, 3) == True
        assert game.selected == None
        assert game.board.find_piece(2, 3) == Piece(2, 3, (255,255,255))
        
        # Test making an invalid move
        game = Checkers(pygame.display.set_mode((600,600)))
        game.board.add_piece(Piece(3, 4, (255,255,255)))
        game.selected = Piece(3, 4, (255,255,255))
        game.valid_moves = {(2, 3): [], (2, 5): []}
        assert game.checkers_move(3, 5) == False
        assert game.selected == Piece(3, 4, (255,255,255))
        assert game.board.find_piece(3, 5) == 0

if __name__ == "__main__":
    t = Testing()
    t.test_move()
    t.test_find_pos()
    t.test_piece_promote_king
    t.test_piece_move
    t.test_piece_draw_piece
    t.test_choose
    t.test_can_be_selected
    t.test_checkers_move