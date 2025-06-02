import pygame
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

def draw_bord(screen):
    """
    Draw the chess bord with the specific dimension
    :param screen: Represent the surface where we draw the bord
    """

    pygame.draw.rect(screen, COLOR_CLEAR_CASE_2, (OFFSET_PLATEAU_X,OFFSET_PLATEAU_Y,BORD_WIDTH,BORD_HEIGHT))
    for row in range(8):
        for col in range(8):
            if (row + col) % 2 != 0:
                pygame.draw.rect(screen, COLOR_DARK_CASE_2, (OFFSET_PLATEAU_Y + row * CASE_SIZE, OFFSET_PLATEAU_X + col * CASE_SIZE, CASE_SIZE, CASE_SIZE))
    return pygame.Surface((BORD_WIDTH,BORD_HEIGHT))

def is_select(game,event):
    """
    Color in the select_color the case who is selected by the player
     and in the background color the previous selected case
    :param game: The game instance
    :param event: The event used to recover the coordinates
    :return: The position of the selected case
    """
    pos = chess_to_xy(xy_to_chess(event.pos))
    top_left_x = pos[0] - CASE_SIZE // 2
    top_left_y = pos[1] - CASE_SIZE // 2
    for y in range(8):
        for x in range(8):
            if selected_case[y][x]:
                selected_case[y][x] = False
                draw_bord(game.screen)
                """

                if (x+y)%2 != 0:
                    pygame.draw.rect(game.screen, COLOR_DARK_CASE,
                                     (OFFSET_PLATEAU_X + x * CASE_SIZE, OFFSET_PLATEAU_Y + y * CASE_SIZE, CASE_SIZE, CASE_SIZE))
                    print(f"case noir colore en pos {x},{y} ")

                else:
                    pygame.draw.rect(game.screen, COLOR_CLEAR_CASE,
                                     (OFFSET_PLATEAU_X + x * CASE_SIZE, OFFSET_PLATEAU_Y + y * CASE_SIZE, CASE_SIZE,
                                      CASE_SIZE))
                    print(f"case blanche colore en pos {x},{y} ")
                """

    for y in range(len(game.bord)):
        for x in range(len(game.bord[y])):

            if game.bord[y][x] is not None:
                if game.bord[y][x].rect.collidepoint(event.pos):
                    pygame.draw.rect(game.screen,SELECTION_COLOR,(top_left_x,top_left_y,CASE_SIZE,CASE_SIZE))
                    #print(f"Case selected en {x},{y}")
                    selected_case[y][x]= True
                    des_x = x
                    des_y = y
                    show_possible_move(game,(des_x,des_y))
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
        draw_bord(game.screen)
        return
    piece = game.bord[original_y][original_x]
    game.bord[des_y][des_x] = piece
    game.bord[original_y][original_x] = None
    draw_bord(game.screen)

    """

    if (original_x + original_y) % 2 != 0:
        pygame.draw.rect(game.screen, COLOR_DARK_CASE,
                         (OFFSET_PLATEAU_X + original_x * CASE_SIZE, OFFSET_PLATEAU_Y + original_y * CASE_SIZE, CASE_SIZE, CASE_SIZE))

    else:
        pygame.draw.rect(game.screen, COLOR_CLEAR_CASE,
                         (OFFSET_PLATEAU_X + original_x * CASE_SIZE, OFFSET_PLATEAU_Y + original_y * CASE_SIZE, CASE_SIZE,
                          CASE_SIZE))
    """
    game.switch_turn()
    return COLUMNS[des_x]+ROWS[des_y]

def is_collinear(v1,v2):
    """
    Verify if two vector are collinear
    :param v1: Vector 1
    :param v2: Vector 2
    :return: Whether the vector are collinear
    """
    # v1 = (dx,dy) , v2 = (dx,dy)
    return v1[0]*v2[1]-v1[1]*v2[0] == 0

def is_legal_move(game, original_x, original_y, des_x, des_y):
    """
    Verify is the validity of a movement
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


    if original.color != game.turn: # We  verify if it is his turn to play
        return False

    valid_direction =  False

    if original.movement_type == SLIDING: # We verify if this is a valid move
        # To be a valid move the directional vector need to be collinear to the move vector
        for direct in original.movement:
            if is_collinear((d_x,d_y),direct):
                valid_direction = True
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

def show_possible_move(game,pos):
    x = pos[0]
    y = pos[1]
    piece = game.bord[y][x]

    for (d_x,d_y) in piece.movement:
        if piece.movement_type == SLIDING:
            for i in range(8):
                des_x = x + d_x*i
                des_y = y + d_y*i
                if 0 <= des_x <= 7 and 0 <= des_y <= 7:

                    pos_2 = chess_to_xy((des_x,des_y))
                    if game.bord[des_y][des_x] is None:
                        pygame.draw.circle(game.screen,SELECTION_COLOR,pos_2,15)
        else:
            des_x = x + d_x
            des_y = y + d_y
            # des_case = game.bord[des_y][des_x]
            if 0 <= des_x <= 7 and 0 <= des_y <= 7:
                pos_2 = chess_to_xy((des_x, des_y))
                pygame.draw.circle(game.screen, SELECTION_COLOR, pos_2, 15)






