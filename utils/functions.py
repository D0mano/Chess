import pygame
import math
import copy

from utils.constante import *


selected_case = [[False for _ in range(8)] for _ in range(8)]


def chess_to_xy(pos):
    """
    Convert chess coordinate into xy coordinate
    :param pos: The coordinate in the xy-axis
    :return:
    """
    if pos is not None:
        pos_x = pos[0] * CASE_SIZE + OFFSET_PLATEAU_X + CASE_SIZE // 2
        pos_y = pos[1] * CASE_SIZE + OFFSET_PLATEAU_Y + CASE_SIZE // 2
        return pos_x,pos_y
    return


def xy_to_chess(pos):
    """
    Convert the position into the bord scale
    :param pos: The position to be converted
    :return: The coordinate in the chess bord scale
    """
    pos_x = (pos[0]-OFFSET_PLATEAU_X)//CASE_SIZE
    pos_y = (pos[1]-OFFSET_PLATEAU_Y)//CASE_SIZE


    if (0 <= pos_x <= 7) and (0 <= pos_y <= 7):
        return pos_x,pos_y
    return


def draw_bord(screen,game ,miniature = False,offset_x = OFFSET_PLATEAU_X,offset_y = OFFSET_PLATEAU_Y,bord_width = BORD_WIDTH,bord_height = BORD_HEIGHT , case_size = CASE_SIZE):
    """
    Draw the chess bord with the specific dimension
    :param screen: Represent the surface where we draw the bord
    :param game: Represent the game instance
    """
    color = game.bord_color

    if not miniature:
        pygame.draw.rect(screen, TEXT_COLOR,
                         (offset_x - 25, offset_y - 25, bord_width + 50, bord_height + 50))

    pygame.draw.rect(screen, color[0], (offset_x,offset_y,bord_width,bord_height))
    for row in range(8):
        for col in range(8):
            if (row + col) % 2 != 0:
                pygame.draw.rect(screen, color[1], (offset_x + row * case_size, offset_y + col * case_size, case_size, case_size))
    font= pygame.font.Font(None,20)
    if not miniature:
        for i in range(8):
            text_number = font.render(ROWS[i],True,(150,150,150))
            rect_number = text_number.get_rect(center=(offset_x-15,(offset_y+case_size//2)+(i*case_size)))
            screen.blit(text_number,rect_number)
            text_letter = font.render(COLUMNS[i],True,(150,150,150))
            rect_letter = text_letter.get_rect(center=((offset_x+case_size//2)+(i*case_size),(offset_y + 8*case_size) +10))
            screen.blit(text_letter,rect_letter)

    return pygame.Rect(offset_x,offset_y,bord_width,bord_height)


def is_collinear(v1,v2):
    """
    Verify if two vector are collinear
    :param v1: Vector 1
    :param v2: Vector 2
    :return: Whether the vector are collinear
    """
    # v1 = (dx,dy) , v2 = (dx,dy)
    return v1[0]*v2[1]-v1[1]*v2[0] == 0


def is_legal_move(game, original_x, original_y, des_x, des_y,ignore_turn = False):
    """
    Verify is the validity of a movement
    :param ignore_turn: Boolean value to known if we need to consider the turn
    :param game: Game instance
    :param original_x: original x coordinate
    :param original_y: original y coordinate
    :param des_x: x coordinate of the destination
    :param des_y: y coordinate of the destination
    :return: True if the move is valid False either
    """

    original = game.bord[original_y][original_x]
    destination = game.bord[des_y][des_x]
    # Computation of the distance
    d_x = des_x - original_x
    d_y = des_y - original_y

    if not ignore_turn:
        if original.color != game.turn:
            return False

    if (des_x,des_y) in QUEEN_SIDE_CASTLE and original.nb_move == 0:
        if original.type_piece == KING:
            return can_castle_queen_side(game,original.color)
    elif (des_x,des_y) in KING_SIDE_CASTLE and original.nb_move == 0:
        if original.type_piece == KING:
            return can_castle_king_side(game,original.color)

    valid_direction =  False
    if original.type_piece != PAWN:

        if original.movement_type == SLIDING: # We verify if this is a valid move
            # To be a valid move the directional vector need to be collinear to the move vector
            for direct in original.movement:
                if is_collinear((d_x,d_y),direct):
                    valid_direction = True
                    break
            if valid_direction: # We verify that there is not piece in the way
                step_x = (d_x//abs(d_x)) if d_x != 0 else 0
                step_y = (d_y//abs(d_y)) if d_y != 0 else 0
                x,y = original_x + step_x , original_y + step_y
                while (x,y) != (des_x,des_y):
                    if game.bord[y][x] is not None:
                        return False
                    x += step_x
                    y += step_y
        else: # If this isn't a sliding piece the move need to be in the list of movement of the piece

            valid_direction = (d_x,d_y)  in original.movement
        if destination is None:
            if valid_direction:
                return True
            return False

        if original.color == destination.color:
            return False
        elif valid_direction:
            return True
    else:
        return is_legal_move_pawn(game, original_x, original_y, des_x, des_y)


def is_legal_move_simu(bord,o_x,o_y,d_x,d_y):
    case_sta = bord[o_y][o_x]
    case_end = bord[d_y][d_x]
    distance_x = d_x - o_x
    distance_y = d_y - o_y
    valid_direction = False
    if case_sta[0] != PAWN:

        if case_sta[2] == SLIDING:  # We verify if this is a valid move
            # To be a valid move the directional vector need to be collinear to the move vector
            for direct in MOVEMENT[case_sta[0]]:
                if is_collinear((distance_x, distance_y), direct):
                    valid_direction = True
                    break
            if valid_direction:  # We verify that there is not piece in the way
                step_x = (distance_x // abs(distance_x)) if distance_x != 0 else 0
                step_y = (distance_y // abs(distance_y)) if distance_y != 0 else 0
                x, y = o_x + step_x, o_y + step_y
                while (x, y) != (d_x, d_y):
                    if bord[y][x] is not None:
                        return False
                    x += step_x
                    y += step_y
        else:  # If this isn't a sliding piece the move need to be in the list of movement of the piece

            valid_direction = (distance_x, distance_y) in MOVEMENT[case_sta[0]]
        if case_end is None:
            if valid_direction:
                return True
            return False

        if case_sta[1] == case_end[1]:
            return False
        elif valid_direction:
            return True
    else:
        return is_legal_move_pawn_simu(bord, o_x, o_y, d_x, d_y)


def show_possible_move(game,pos):
    orig_x = pos[0]
    orig_y = pos[1]
    piece = game.bord[orig_y][orig_x]


    for y in range(8):
        for x in range(8):
            if is_legal_move(game,orig_x,orig_y,x,y) and is_safe_move(game,orig_x,orig_y,x,y,game.turn):
                pos_2 = chess_to_xy((x, y))
                top_left_x = pos_2[0] - CASE_SIZE // 2
                top_left_y = pos_2[1] - CASE_SIZE // 2
                circle_surf = pygame.Surface((CASE_SIZE,CASE_SIZE),pygame.SRCALPHA)
                pygame.draw.circle(circle_surf, SELECTION_COLOR_3, (CASE_SIZE/2,CASE_SIZE/2), 10)
                game.screen.blit(circle_surf, (top_left_x, top_left_y))


def is_legal_move_pawn(game,orig_x,orig_y,des_x,des_y):
    original = game.bord[orig_y][orig_x]
    destination = game.bord[des_y][des_x]
    # Computation of the distance
    d_x = des_x - orig_x
    d_y = des_y - orig_y
    if destination is not None:
        if (d_x, d_y) in original.movement_2:
            return True
    if original.nb_move == 0:

        valid_direction = (d_x, d_y) in original.movement_1
    else:
        valid_direction = (d_x, d_y) in original.movement

    if valid_direction:  # We verify that there is not piece in the way
        step_x = (d_x // abs(d_x)) if d_x != 0 else 0
        step_y = (d_y // abs(d_y)) if d_y != 0 else 0
        x, y = orig_x + step_x, orig_y + step_y
        while (x, y) != (des_x, des_y):
            if game.bord[y][x] is not None:
                return False
            x += step_x
            y += step_y
    if destination is None:
        if valid_direction:
            return True
        return False


def is_legal_move_pawn_simu(bord,o_x,o_y,d_x,d_y):
    original = bord[o_y][o_x]
    destination = bord[d_y][d_x]
    color = original[1]

    # Computation of the distance
    distance_x = d_x - o_x
    distance_y = d_y - o_y
    if color == WHITE:
        if (distance_x, distance_y) in DIRECTIONS_WHITE_PAWN_2 and destination is not None:
            return True
        if original[3]== 0:

            valid_direction = (distance_x, distance_y) in DIRECTIONS_WHITE_PAWN_1
        else:
            valid_direction = (distance_x, distance_y) in DIRECTIONS_WHITE_PAWN
    else:
        if (distance_x, distance_y) in DIRECTIONS_BLACK_PAWN_2 and destination is not None:
            return True
        if original[3] == 0:

            valid_direction = (distance_x, distance_y) in DIRECTIONS_BLACK_PAWN_1
        else:
            valid_direction = (distance_x, distance_y) in DIRECTIONS_BLACK_PAWN


    if valid_direction:  # We verify that there is not piece in the way
        step_x = (distance_x // abs(distance_x)) if distance_x != 0 else 0
        step_y = (distance_y // abs(distance_y)) if distance_y != 0 else 0
        x, y = o_x + step_x, o_y + step_y
        while (x, y) != (distance_x, distance_y):
            if bord[y][x] is not None:
                return False
            x += step_x
            y += step_y
    if destination is None:
        if valid_direction:
            return True
        return False


def king_pos(bord,color):
    for y in range(8):
        for x in range(8):
            piece = bord[y][x]
            if piece is not None:
                if piece.type_piece == KING and piece.color == color:
                    return x,y


def king_pos_simu(bord,color):
    for y in range(8):
        for x in range(8):
            piece = bord[y][x]
            if piece is not None:
                if piece[0] == KING and piece[1] == color:
                    return x,y



def is_check(game, color):

    pos = king_pos(game.bord,color)
    pos_xy = chess_to_xy(pos)
    top_left_x = pos_xy[0] - CASE_SIZE // 2
    top_left_y = pos_xy[1] - CASE_SIZE // 2
    if pos is None:
        return False
    # Couleur de l'adversaire (celui qui peut mettre en échec)
    adversaire_color = -color
    for y in range(8):
        for x in range(8):
            piece = game.bord[y][x]
            if piece is not None and piece.color == adversaire_color:
                #print(f"We verify the piece {PIECES_NAMES[piece.type_piece]} {piece.color}")
                #print(f"Testing move from ({x},{y}) to king at {pos}")
                if is_legal_move(game, x, y, pos[0], pos[1],True):
                    pygame.draw.rect(game.screen, COLOR_CHECK, (top_left_x, top_left_y, CASE_SIZE, CASE_SIZE))
                    game.update()
                    draw_move_arrow(game.screen, (x, y), pos)
                    #print( f"ÉCHEC ! {PIECES_NAMES[piece.type_piece]} en ({x},{y}) attaque le roi en ({pos[0]},{pos[1]})")
                    return True
    return False


def is_check_simu(bord,color):
    pos = king_pos_simu(bord, color)
    if pos is None:
        return False
        # Couleur de l'adversaire (celui qui peut mettre en échec)
    adversary_color = -color
    for y in range(8):
        for x in range(8):
            piece = bord[y][x]
            if piece is not None and piece[1] == adversary_color:
                # print(f"We verify the piece {PIECES_NAMES[piece.type_piece]} {piece.color}")
                # print(f"Testing move from ({x},{y}) to king at {pos}")
                if is_legal_move_simu(bord, x, y, pos[0], pos[1]):
                    # print( f"ÉCHEC ! {PIECES_NAMES[piece.type_piece]} en ({x},{y}) attaque le roi en ({pos[0]},{pos[1]})")
                    return True
    return False


def draw_arrow_filled(surface, color, start_pos, end_pos, arrow_width=5, arrow_head_size=15):
    """
    Draw a filled arrow with elegant appearance
    :param surface: The surface to draw on
    :param color: Color of the arrow
    :param start_pos: Starting position (x, y)
    :param end_pos: Ending position (x, y)
    :param arrow_width: Width of the arrow body
    :param arrow_head_size: Size of the arrow head
    """
    # Calculate direction vector
    dx = end_pos[0] - start_pos[0]
    dy = end_pos[1] - start_pos[1]

    # Handle edge case: same start and end position
    if dx == 0 and dy == 0:
        return

    # Normalize the direction vector
    length = math.sqrt(dx * dx + dy * dy)
    unit_x = dx / length
    unit_y = dy / length

    # Calculate perpendicular vector for arrow width
    perp_x = -unit_y * arrow_width / 2
    perp_y = unit_x * arrow_width / 2

    # Calculate where the arrow body ends (before the head)
    body_end_x = end_pos[0] - unit_x * arrow_head_size
    body_end_y = end_pos[1] - unit_y * arrow_head_size

    # Draw the arrow body (rectangle)
    body_points = [
        (start_pos[0] + perp_x, start_pos[1] + perp_y),
        (start_pos[0] - perp_x, start_pos[1] - perp_y),
        (body_end_x - perp_x, body_end_y - perp_y),
        (body_end_x + perp_x, body_end_y + perp_y)
    ]
    pygame.draw.polygon(surface, color, body_points)

    # Draw the arrow head (triangle)
    head_width = arrow_width * 2
    head_perp_x = -unit_y * head_width / 2
    head_perp_y = unit_x * head_width / 2

    head_points = [
        end_pos,
        (body_end_x + head_perp_x, body_end_y + head_perp_y),
        (body_end_x - head_perp_x, body_end_y - head_perp_y)
    ]
    pygame.draw.polygon(surface, color, head_points)


def draw_move_arrow(screen, start_pos, end_pos, color=POSSIBLE_MOVE):
    """
    Draw an arrow to show possible move
    :param screen: The surface to draw on
    :param color: Color of the arrow
    :param start_pos: Starting position (x, y)
    :param end_pos: Ending position (x, y)
    """
    start_pixel = chess_to_xy(start_pos)
    end_pixel = chess_to_xy(end_pos)
    draw_arrow_filled(screen, color, start_pixel, end_pixel, arrow_width=4, arrow_head_size=12)


def is_safe_move(game, original_x, original_y, des_x, des_y,color):
    game.bord_copy = game.copy()
    move_simu(game.bord_copy,original_x,original_y,des_x,des_y)
    return not is_check_simu(game.bord_copy,color)


def is_select(game,event):
    """
    Color in the select_color the case who is selected by the player
     and in the background color the previous selected case
    :param game: The game instance
    :param event: The event used to recover the coordinates
    :return: The position of the selected case
    """

    pos = chess_to_xy(xy_to_chess(event.pos))
    if pos is None:
        return
    top_left_x = pos[0] - CASE_SIZE // 2
    top_left_y = pos[1] - CASE_SIZE // 2
    for y in range(8):
        for x in range(8):
            if selected_case[y][x]:
                selected_case[y][x] = False
                draw_bord(game.screen,game)
                game.update()

    for y in range(len(game.bord)):
        for x in range(len(game.bord[y])):

            if game.bord[y][x] is not None:
                if game.bord[y][x].rect.collidepoint(event.pos):
                    highlight = pygame.Surface((CASE_SIZE,CASE_SIZE),pygame.SRCALPHA)
                    highlight.fill(SELECTION_COLOR_4)
                    game.screen.blit(highlight, (top_left_x, top_left_y))
                    selected_case[y][x]= True
                    des_x = x
                    des_y = y
                    show_possible_move(game,(des_x,des_y))
                    game.update()
                    return des_x,des_y


def move(game, original_x, original_y, des_x, des_y):
    """
    Move the piece on the bord
    :param game: The game instance
    :param original_x: x-coordinate of the origin of the piece
    :param original_y: y-coordinate of the origin of the piece
    :param des_x: x-coordinate of the destination of the piece
    :param des_y: y-coordinate of the destination of the piece
    :return: A string describing the move
    """

    if not is_legal_move(game, original_x, original_y, des_x, des_y):
        draw_bord(game.screen,game)
        game.move_illegal_sound.play()
        game.update()
        return

    if not is_safe_move(game,original_x, original_y, des_x, des_y,game.turn):
        draw_bord(game.screen,game)
        game.move_illegal_sound.play()
        game.update()
        return




    capture = False
    if game.bord[des_y][des_x] is not None:
        capture = True


    piece = game.bord[original_y][original_x]
    if (des_x, des_y) in QUEEN_SIDE_CASTLE and piece.type_piece == KING and piece.nb_move == 0:
        piece.nb_move += 1
        movement = execute_castle(game, piece.color, False)
        draw_bord(game.screen,game)
        game.update()
        game.switch_turn()
        game.castle_sound.play()
        return movement
    elif (des_x, des_y) in KING_SIDE_CASTLE and piece.type_piece == KING and piece.nb_move == 0:
        piece.nb_move += 1
        movement = execute_castle(game, piece.color, True)
        draw_bord(game.screen,game)
        game.update()
        game.switch_turn()
        game.castle_sound.play()
        return movement
    piece.nb_move += 1
    game.bord[des_y][des_x] = piece
    game.bord[original_y][original_x] = None
    draw_bord(game.screen,game)
    game.update()
    promotion = game.bord[des_y][des_x].promotion()
    if promotion:
        game.update()
    game.increment(game.turn,game.increment_time)
    game.switch_turn()
    game.check = is_check(game, game.turn)
    game.checkmate = game.is_checkmate(game.turn)
    stalemate = game.is_stalemate(game.turn)



    if game.checkmate:
        game.game_end_sound.play()
    elif game.check:
        game.move_check_sound.play()
    elif capture:
        game.capture_sound.play()
    else:
        game.move_self_sound.play()
    return algebraic_notation(original_x,des_x,des_y,capture,game.check,game.checkmate,piece.type_piece,promotion)


def move_simu(bord,o_x,o_y,d_x,d_y):

    piece = bord[o_y][o_x]
    bord[d_y][d_x] = piece
    bord[o_y][o_x] = None


def algebraic_notation( original_x, des_x, des_y, capture, check, checkmate, type_piece,promotion):
    if capture:
        if promotion:
            notation = COLUMNS[original_x] + "x" + COLUMNS[des_x] + ROWS[des_y] + "=" + PIECE_PGN[type_piece]

        elif type_piece == PAWN:
            notation = COLUMNS[original_x] + "x" + COLUMNS[des_x] + ROWS[des_y]

        else:
            notation = PIECE_PGN[type_piece] + "x" + COLUMNS[des_x] + ROWS[des_y]
        if checkmate:
            notation += "#"
        elif check:
            notation += "+"
        return notation
    else:
        if promotion:
            notation = COLUMNS[des_x] + ROWS[des_y] + "=" + PIECE_PGN[type_piece]
        elif type_piece == PAWN:
            notation = COLUMNS[des_x] + ROWS[des_y]
        else:
            notation = PIECE_PGN[type_piece] + COLUMNS[des_x] + ROWS[des_y]

        if checkmate:
            notation += "#"
        elif check:
            notation += "+"
        return notation


def create_pgn(list_coup,color,game):
    with open("game_save.txt","w") as file:
        result = ""
        if color == WHITE and game.checkmate:
            result = "1-0"
        elif color == BLACK and game.checkmate:
            result = "0-1"
        elif game.stalemate:
            result = "1/2-1/2"
        else:
            result = "*"
        file.write(f'[Event ""]\n'
                   f'[Site ""]\n'
                   f'[Date ""]\n'
                   f'[Round ""]\n'
                   f'[White "Player_1"]\n'
                   f'[Black "Player_2"]\n'
                   f'[Result "{result}"]\n'
                   f'[FEN "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"]\n')
        for i in range(len(list_coup)):
            file.write(f"{i+1}. ")
            for movement in list_coup[i]:
                file.write(f"{movement} ")
        file.write(result)


def can_castle_king_side(game, color):
    """
    Vérify if the king side castle is possible
    """
    king_x, king_row = king_pos(game.bord,color)
    rook_x = 7

    # We verify is the king and the rook didn't move

    king = game.bord[king_row][king_x]
    rook = game.bord[king_row][rook_x]

    if  king.color != color or king.nb_move > 0:
        return False
    if rook is None or rook.type_piece != ROOK or rook.color != color or rook.nb_move > 0:
        return False

    # Check that the squares between the king and the rook are empty
    for x in range(5, 7):
        if game.bord[king_row][x] is not None:
            return False

    # Check that the king is not in check and does not pass through an attacked square.
    if game.check:
        return False

    # Simulate the king's movement square by square
    for x in range(4, 7):
        if not is_safe_move(game, king_x, king_row, x, king_row, color):
            return False

    return True


def can_castle_queen_side(game, color):
    """
    Vérify if the king side castle is possible
    """
    king_x, king_row = king_pos(game.bord,color)
    rook_x =  0

    # We verify if the king and the rook didn't move

    king = game.bord[king_row][king_x]
    rook = game.bord[king_row][rook_x]

    if  king.color != color or king.nb_move > 0:
        return False
    if rook is None or rook.type_piece != ROOK or rook.color != color or rook.nb_move > 0:
        return False

    # Check that the squares between the king and the rook are empty

    for x in range(1, 4):
        if game.bord[king_row][x] is not None:
            return False

    # Check that the king is not in check and does not pass through an attacked square.

    if game.check:
        return False

    # Simulate the king's movement square by square

    for x in range(4, 1, -1):
        if not is_safe_move(game, king_x, king_row, x, king_row, color):
            return False

    return True


def execute_castle(game, color, king_side=True):
    """
    Exécute le roque
    """
    king_row = 7 if color == WHITE else 0

    if king_side:
        # Roque côté roi
        king_new_x, rook_old_x, rook_new_x = 6, 7, 5
    else:
        # Roque côté dame
        king_new_x, rook_old_x, rook_new_x = 2, 0, 3

    # Déplacer le roi
    king = game.bord[king_row][4]
    game.bord[king_row][king_new_x] = king
    game.bord[king_row][4] = None
    king.nb_move += 1

    # Déplacer la tour
    rook = game.bord[king_row][rook_old_x]
    game.bord[king_row][rook_new_x] = rook
    game.bord[king_row][rook_old_x] = None
    rook.nb_move += 1

    return "O-O" if king_side else "O-O-O"























