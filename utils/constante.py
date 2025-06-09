# constante.py - Configuration du jeu d'échecs

# === DIMENSIONS ET AFFICHAGE ===
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
CASE_SIZE = 80
BORD_WIDTH = CASE_SIZE * 8  # 560px
BORD_HEIGHT = CASE_SIZE * 8  # 560px

# Position du plateau sur l'écran (centré)
OFFSET_PLATEAU_X = (WINDOW_WIDTH - BORD_WIDTH) // 2
OFFSET_PLATEAU_Y = (WINDOW_HEIGHT - BORD_HEIGHT) // 2

# === COULEURS (format RGB) ===
# Couleurs de l'échiquier
COLOR_CLEAR_CASE = (240, 217, 181)  # #F0D9B5
COLOR_DARK_CASE = (181, 136, 99)  # #B58863
CLASSICAL_BORD = [COLOR_CLEAR_CASE,COLOR_DARK_CASE]


COLOR_CLEAR_CASE_2 = (237, 242, 250)  # #edf2fa
COLOR_DARK_CASE_2 = (111, 163, 213)  # #6fa3d5
CIEL_BORD = [COLOR_CLEAR_CASE_2,COLOR_DARK_CASE_2]


COLOR_CLEAR_CASE_3 = (235, 236, 208) # #ebecd0
COLOR_DARK_CASE_3 = (115, 149, 82)  # #739552
GREEN_BORD = [COLOR_CLEAR_CASE_3,COLOR_DARK_CASE_3]


# Couleurs d'interface
BACKGROUND_COLOR = (50, 50, 50)  # Fond de la fenêtre
SELECTION_COLOR = (125, 211, 192,100)  # #7DD3C0 - Case sélectionnée
SELECTION_COLOR_2 = (194, 235, 247,180)
SELECTION_COLOR_3 = (150,150,150,150)
SELECTION_COLOR_4 = (215,224,98,180)

COLOR_CHECK = (255, 107, 107)  # #FF6B6B - Roi en échec
POSSIBLE_MOUV = (100, 200, 100, 100)  # Vert transparent

# Couleurs du texte
COULEUR_TEXTE = (255, 255, 255)  # Blanc
COULEUR_TEXTE_NOIR = (0, 0, 0)  # Noir

# === TYPES DE PIÈCES ===
# Constantes pour identifier les pièces
EMPTY = 0
PAWN = 1
ROOK = 2
KNIGHT = 3
BISHOP = 4
QUEEN = 5
KING = 6

# Couleurs des joueurs
WHITE = 1
BLACK = -1

SIZE_PIECES = 60
# === CARACTÈRES UNICODE DES PIÈCES ===
PIECES_UNICODE = {
    (WHITE, KING): '♔',
    (WHITE, QUEEN): '♕',
    (WHITE, ROOK): '♖',
    (WHITE, BISHOP): '♗',
    (WHITE, KNIGHT): '♘',
    (WHITE, PAWN): '♙',
    (BLACK, KING): '♚',
    (BLACK, QUEEN): '♛',
    (BLACK, ROOK): '♜',
    (BLACK, BISHOP): '♝',
    (BLACK, KNIGHT): '♞',
    (BLACK, PAWN): '♟'
}

# === NOMS DES PIÈCES (pour affichage/debug) ===
PIECES_NAMES = {
    EMPTY: "Vide",
    PAWN: "Pawn",
    ROOK: "Rook",
    KNIGHT: "Knight",
    BISHOP: "Bishop",
    QUEEN: "Queen",
    KING: "King"
}

# === POSITION INITIALE DE L'ÉCHIQUIER ===
# Chaque case contient (couleur, type_piece)
# VIDE représente une case vide
PLATEAU_INITIAL = [
    # Ligne 8 (index 0) - Pièces noires
    [(BLACK, ROOK), (BLACK, KNIGHT), (BLACK, BISHOP), (BLACK, QUEEN),
     (BLACK, KING), (BLACK, BISHOP), (BLACK, KNIGHT), (BLACK, ROOK)],

    # Ligne 7 (index 1) - Pions noirs
    [(BLACK, PAWN), (BLACK, PAWN), (BLACK, PAWN), (BLACK, PAWN),
     (BLACK, PAWN), (BLACK, PAWN), (BLACK, PAWN), (BLACK, PAWN)],

    # Lignes 6 à 3 (indices 2 à 5) - Cases vides
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],

    # Ligne 2 (index 6) - Pions blancs
    [(WHITE, PAWN), (WHITE, PAWN), (WHITE, PAWN), (WHITE, PAWN),
     (WHITE, PAWN), (WHITE, PAWN), (WHITE, PAWN), (WHITE, PAWN)],

    # Ligne 1 (index 7) - Pièces blanches
    [(WHITE, ROOK), (WHITE, KNIGHT), (WHITE, BISHOP), (WHITE, QUEEN),
     (WHITE, KING), (WHITE, BISHOP), (WHITE, KNIGHT), (WHITE, ROOK)]
]

# === COORDONNÉES D'ÉCHIQUIER ===
# Conversion entre indices de tableau et notation échiquéenne
COLUMNS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
ROWS = ['8', '7', '6', '5', '4', '3', '2', '1']

# === CONFIGURATIONS DE JEU ===
FPS = 60  # Images par seconde

# Police pour l'affichage du texte
SIZE_PIECE_POLICE = 60
SIZE_INTERFACE_POLICE = 20

# === TOUCHES CLAVIER ===
# Codes pour les actions spéciales (à utiliser avec pygame)
NEW_GAME_KEY = 'n'
QUIT_KEY = 'q'

# === ÉTATS DU JEU ===
GAME_IN_PROGRESS = 0
WHITE_CHECKMATE = 1
BLACK_CHECKMATE = 2
PAT = 3
PARTIE_NULLE = 4

# === DIRECTIONS DE MOUVEMENT ===
# Pour calculer les mouvements des pièces
DIRECTIONS_WHITE_PAWN = [(0, -1)]
DIRECTIONS_WHITE_PAWN_1 = DIRECTIONS_WHITE_PAWN+[(0, -2)]
DIRECTIONS_WHITE_PAWN_2 = [(-1,-1),(1,-1)]

DIRECTIONS_BLACK_PAWN = [(0, 1)]
DIRECTIONS_BLACK_PAWN_1 = DIRECTIONS_BLACK_PAWN + [(0, 2)]
DIRECTIONS_BLACK_PAWN_2 = [(-1,1),(1,1)]

ROOK_DIRECTION = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Horizontal/Vertical
BISHOP_DIRECTION = [(1, 1), (1, -1), (-1, 1), (-1, -1)]  # Diagonales
QUEEN_DIRECTION = ROOK_DIRECTION + BISHOP_DIRECTION
KING_DIRECTION = QUEEN_DIRECTION  # Même directions mais 1 case seulement

# Mouvements du cavalier (en L)
KNIGHT_DIRECTION = [
    (2, 1), (2, -1), (-2, 1), (-2, -1),
    (1, 2), (1, -2), (-1, 2), (-1, -2)
]

MOVEMENT = {
             ROOK : ROOK_DIRECTION,
             BISHOP : BISHOP_DIRECTION,
             KNIGHT : KNIGHT_DIRECTION,
             KING : KING_DIRECTION,
             QUEEN : QUEEN_DIRECTION
            }
#====== Piece type ========#
JUMPING = 1
SLIDING = 0