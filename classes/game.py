from utils.constante import *
from classes.pieces import Pieces
from utils.functions import chess_to_xy
from classes.interface import display_current_player


class Game:
    def __init__(self,screen):
        self.is_playing = False
        self.screen = screen
        self.bord = []
        self.bord_copy = []
        for y in range(len(PLATEAU_INITIAL)):
            row = []
            for x in range(len(PLATEAU_INITIAL[y])):
                pieces = PLATEAU_INITIAL[y][x]
                if pieces != EMPTY:
                    obj = Pieces(pieces[0], x, y, pieces[1])
                    row.append(obj)
                else: row.append(None)
            self.bord.append(row)
        self.turn = WHITE
        self.nb_turn = 1
        self.check = None

    def update(self):
        """
        Update the position of the pieces in the bord to their coordinate
        :return:
        """
        for y in range(8):
            for x in range(8):
                if self.bord[y][x] is not None:
                    self.bord[y][x].rect = self.bord[y][x].image.get_rect(center=(chess_to_xy((x,y))))
                    self.bord[y][x].x = x
                    self.bord[y][x].y = y

    def switch_turn(self):
        self.turn = -self.turn
        display_current_player(self)
        if self.turn == WHITE:
            self.nb_turn += 1
        return self.turn

    def copy(self):
        bord = self.bord
        copy = []
        for y in range(8):
            row = []
            for x in range(8):
                piece = bord[y][x]
                if piece is None:
                    row.append(None)
                else:
                    row.append((piece.type_piece,piece.color,piece.movement_type,piece.nb_move))
            copy.append(row)
        return copy



