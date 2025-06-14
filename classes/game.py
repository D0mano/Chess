from utils.constante import *
import pygame
from classes.pieces import Pieces
from utils.functions import chess_to_xy
from classes.interface import display_current_player


class Game:
    def __init__(self,screen):
        self.is_playing = False
        self.screen = screen
        self.bord = []
        self.bord_copy = []
        self.white_time = None
        self.black_time = None
        for y in range(len(PLATEAU_INITIAL)):
            row = []
            for x in range(len(PLATEAU_INITIAL[y])):
                pieces = PLATEAU_INITIAL[y][x]
                if pieces != EMPTY:
                    obj = Pieces(self,pieces[0], x, y, pieces[1])
                    row.append(obj)
                else: row.append(None)
            self.bord.append(row)
        self.turn = WHITE
        self.nb_turn = 1
        self.check = None
        self.checkmate = None
        self.stalemate = None
        self.white_roque = True
        self.black_roque = True
        self.game_start_sound = pygame.mixer.Sound(f"assets/sounds/game-start.mp3")
        self.game_end_sound = pygame.mixer.Sound(f"assets/sounds/game-end.mp3")
        self.move_self_sound = pygame.mixer.Sound(f"assets/sounds/move-self.mp3")
        self.move_check_sound = pygame.mixer.Sound("assets/sounds/move-check.mp3")
        self.move_illegal_sound = pygame.mixer.Sound("assets/sounds/illegal.mp3")
        self.capture_sound = pygame.mixer.Sound("assets/sounds/capture.mp3")



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

    def is_checkmate(self,color):
        if not self.check:
            return False
        for y in range(8):
            for x in range(8):
                piece = self.bord[y][x]
                if piece is not None and piece.color == color:
                    if piece.count_possible_move() != 0:
                        return False
        print("Checkmate !!")
        return True

    def is_stalemate(self, color):
        if  self.check:
            return False
        for y in range(8):
            for x in range(8):
                piece = self.bord[y][x]
                if piece is not None and piece.color == color:
                    if piece.count_possible_move() != 0:
                        return False
        print("Stalemate !!")
        return True

    def set_time(self,time):
        self.white_time = time
        self.black_time = time

    def decrement_time(self,color,dt):
        if color == WHITE:
            self.white_time -= dt
        else:
            self.black_time -= dt







