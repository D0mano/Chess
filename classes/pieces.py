from utils.functions import *


class Pieces:
    def __new__(cls, color = int, x = int, y = int, type_piece = int):
        if type_piece == PAWN:
            return super().__new__(Pawn)
        elif type_piece == KNIGHT:
            return super().__new__(Knight)
        elif type_piece == BISHOP:
            return super().__new__(Bishop)
        elif type_piece == ROOK:
            return super().__new__(Rook)
        elif type_piece == KING:
            return super().__new__(King)
        elif type_piece == QUEEN:
            return super().__new__(Queen)
    def __init__(self,color,x,y,type_piece):
        self.color = color
        self.type_piece = type_piece
        self.nb_move = 0


class Pawn(Pieces):
    def __init__(self,color,x,y,type_piece):
        super().__init__(color,x,y,type_piece)
        if self.color == WHITE :
            self.image = pygame.image.load(f"assets/pieces/white-pawn.png")
            self.movement = DIRECTIONS_WHITE_PAWN
            self.movement_1 = DIRECTIONS_WHITE_PAWN_1
            self.movement_2 = DIRECTIONS_WHITE_PAWN_2
        else:
            self.image = pygame.image.load(f"assets/pieces/black-pawn.png")
            self.movement = DIRECTIONS_BLACK_PAWN
            self.movement_1 = DIRECTIONS_BLACK_PAWN_1
            self.movement_2 = DIRECTIONS_BLACK_PAWN_2

        self.image = pygame.transform.scale(self.image,(SIZE_PIECES,SIZE_PIECES))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect = self.image.get_rect(center=(chess_to_xy((self.rect.x,self.rect.y))))
        self.movement_type = JUMPING


class Knight(Pieces):
    def __init__(self,color,x,y,type_piece):
        super().__init__(color,x,y,type_piece)
        if self.color == 1 :self.image = pygame.image.load(f"assets/pieces/white-knight.png")
        else: self.image = pygame.image.load(f"assets/pieces/black-knight.png")

        self.image = pygame.transform.scale(self.image,(SIZE_PIECES,SIZE_PIECES))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect = self.image.get_rect(center=(chess_to_xy((self.rect.x, self.rect.y))))
        self.movement = KNIGHT_DIRECTION
        self.movement_type = JUMPING

class Bishop(Pieces):
    def __init__(self,color,x,y,type_piece):
        super().__init__(color,x,y,type_piece)
        if self.color == 1 :self.image = pygame.image.load(f"assets/pieces/white-bishop.png")
        else: self.image = pygame.image.load(f"assets/pieces/black-bishop.png")

        self.image = pygame.transform.scale(self.image,(SIZE_PIECES,SIZE_PIECES))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect = self.image.get_rect(center=(chess_to_xy((self.rect.x, self.rect.y))))
        self.movement = BISHOP_DIRECTION
        self.movement_type = SLIDING

class Rook(Pieces):
    def __init__(self,color,x,y,type_piece):
        super().__init__(color,x,y,type_piece)
        if self.color == 1 :self.image = pygame.image.load(f"assets/pieces/white-rook.png")
        else: self.image = pygame.image.load(f"assets/pieces/black-rook.png")

        self.image = pygame.transform.scale(self.image,(SIZE_PIECES,SIZE_PIECES))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect = self.image.get_rect(center=(chess_to_xy((self.rect.x, self.rect.y))))
        self.movement = ROOK_DIRECTION
        self.movement_type = SLIDING

class Queen(Pieces):
    def __init__(self,color,x,y,type_piece):
        super().__init__(color,x,y,type_piece)
        if self.color == 1 :self.image = pygame.image.load(f"assets/pieces/white-queen.png")
        else: self.image = pygame.image.load(f"assets/pieces/black-queen.png")

        self.image = pygame.transform.scale(self.image,(SIZE_PIECES,SIZE_PIECES))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect = self.image.get_rect(center=(chess_to_xy((self.rect.x, self.rect.y))))
        self.movement = QUEEN_DIRECTION
        self.movement_type = SLIDING

class King(Pieces):
    def __init__(self,color,x,y,type_piece):
        super().__init__(color,x,y,type_piece)
        if self.color == 1 :self.image = pygame.image.load(f"assets/pieces/white-king.png")
        else: self.image = pygame.image.load(f"assets/pieces/black-king.png")

        self.image = pygame.transform.scale(self.image,(SIZE_PIECES,SIZE_PIECES))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect = self.image.get_rect(center=(chess_to_xy((self.rect.x, self.rect.y))))
        self.movement = KING_DIRECTION
        self.movement_type = JUMPING
