import pygame
from utils.constante import *

list_case = [[False for _ in range(8)] for _ in range(8)]
selected_case = []

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

def draw_bord(screen,x,y):
    """
    Draw the chess bord with the specific dimension
    :param screen: Represent the surface where we draw the bord
    :param x: The x-coordinate
    :param y: The y-coordinate
    """

    pygame.draw.rect(screen, COLOR_CLEAR_CASE, (x,y,BORD_WIDTH,BORD_HEIGHT))
    for row in range(8):
        for col in range(8):
            if (row + col) % 2 != 0:
                pygame.draw.rect(screen, COLOR_DARK_CASE, (y + row * CASE_SIZE, x + col * CASE_SIZE, CASE_SIZE, CASE_SIZE))
    return pygame.Surface((BORD_WIDTH,BORD_HEIGHT))

def is_select(game,event):
    """
    Color in the select_color the case who is selected by the player
     and in the background color the previous selected case
    :param game: The game instance
    :param event: The event used to claim the position
    :return:
    """
    pos = chess_to_xy(xy_to_chess(event.pos))
    top_left_x = pos[0] - CASE_SIZE // 2
    top_left_y = pos[1] - CASE_SIZE // 2
    for y in range(8):
        for x in range(8):
            if list_case[y][x]:
                original_x = x
                original_y = y
                list_case[y][x] = False

                if (x+y)%2 != 0:
                    pygame.draw.rect(game.screen, COLOR_DARK_CASE,
                                     (OFFSET_PLATEAU_X + x * CASE_SIZE, OFFSET_PLATEAU_Y + y * CASE_SIZE, CASE_SIZE, CASE_SIZE))
                    print(f"case noir colore en pos {x},{y} ")

                else:
                    pygame.draw.rect(game.screen, COLOR_CLEAR_CASE,
                                     (OFFSET_PLATEAU_X + x * CASE_SIZE, OFFSET_PLATEAU_Y + y * CASE_SIZE, CASE_SIZE,
                                      CASE_SIZE))
                    print(f"case blanche colore en pos {x},{y} ")

    for y in range(len(game.bord)):
        for x in range(len(game.bord[y])):

            if game.bord[y][x] is not None:
                if game.bord[y][x].rect.collidepoint(event.pos):
                    pygame.draw.rect(game.screen,SELECTION_COLOR,(top_left_x,top_left_y,CASE_SIZE,CASE_SIZE))
                    print(f"Case selectionner en {x},{y}")
                    list_case[y][x]= True
                    des_x = x
                    des_y = y
                    return des_x,des_y


def mouv(game,original_x,original_y,des_x,des_y):
    if original_y is None or des_y is None:
        return
    piece = game.bord[original_y][original_x]
    game.bord[des_y][des_x] = piece
    game.bord[original_y][original_x] = None

    if (original_x + original_y) % 2 != 0:
        pygame.draw.rect(game.screen, COLOR_DARK_CASE,
                         (OFFSET_PLATEAU_X + original_x * CASE_SIZE, OFFSET_PLATEAU_Y + original_y * CASE_SIZE, CASE_SIZE, CASE_SIZE))

    else:
        pygame.draw.rect(game.screen, COLOR_CLEAR_CASE,
                         (OFFSET_PLATEAU_X + original_x * CASE_SIZE, OFFSET_PLATEAU_Y + original_y * CASE_SIZE, CASE_SIZE,
                          CASE_SIZE))



