# constante.py - Configuration du jeu d'échecs

# === DIMENSIONS ET AFFICHAGE ===
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
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

COLOR_CLEAR_CASE_2 = (237, 242, 250)  # #edf2fa
COLOR_DARK_CASE_2 = (111, 163, 213)  # #6fa3d5

# Couleurs d'interface
BACKGROUND_COLOR = (50, 50, 50)  # Fond de la fenêtre
SELECTION_COLOR = (125, 211, 192)  # #7DD3C0 - Case sélectionnée
SELECTION_COLOR_2 = (194, 235, 247)
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
NOMS_PIECES = {
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
TAILLE_POLICE_PIECES = 60
TAILLE_POLICE_INTERFACE = 20

# === TOUCHES CLAVIER ===
# Codes pour les actions spéciales (à utiliser avec pygame)
TOUCHE_NOUVELLE_PARTIE = 'n'
TOUCHE_QUITTER = 'q'

# === ÉTATS DU JEU ===
JEU_EN_COURS = 0
ECHEC_ET_MAT_BLANC = 1
ECHEC_ET_MAT_NOIR = 2
PAT = 3
PARTIE_NULLE = 4

# === DIRECTIONS DE MOUVEMENT ===
# Pour calculer les mouvements des pièces
DIRECTIONS_TOUR = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Horizontal/Vertical
DIRECTIONS_FOU = [(1, 1), (1, -1), (-1, 1), (-1, -1)]  # Diagonales
DIRECTIONS_REINE = DIRECTIONS_TOUR + DIRECTIONS_FOU
DIRECTIONS_ROI = DIRECTIONS_REINE  # Même directions mais 1 case seulement

# Mouvements du cavalier (en L)
MOUVEMENTS_CAVALIER = [
    (2, 1), (2, -1), (-2, 1), (-2, -1),
    (1, 2), (1, -2), (-1, 2), (-1, -2)
]