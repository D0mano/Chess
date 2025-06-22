import pygame.font
from pygame import K_ESCAPE, MOUSEBUTTONUP

from utils.functions import *

def display_current_player(game):
    pygame.init()
    font = pygame.font.SysFont("arial" ,50)
    if game.turn == WHITE:
        text = font.render("White to play !", True, TEXT_COLOR)
        rect = text.get_rect(center=(OFFSET_PLATEAU_X / 2, (GAME_WINDOW_HEIGHT - OFFSET_PLATEAU_Y) / 2))
        pygame.draw.rect(game.screen, BACKGROUND_COLOR, rect)
        game.screen.blit(text, rect)
    else:
        text = font.render("Black to play !", True, TEXT_COLOR)
        rect = text.get_rect(center=(OFFSET_PLATEAU_X / 2, (GAME_WINDOW_HEIGHT - OFFSET_PLATEAU_Y) / 2))
        pygame.draw.rect(game.screen, BACKGROUND_COLOR, rect)
        game.screen.blit(text, rect)

def display_timer(game):
    font = pygame.font.SysFont("Arial", 40)
    minute = game.white_time // 60
    sec = game.white_time % 60

    minute_2 = game.black_time // 60
    sec_2 = game.black_time % 60

    padding_x1 = 20
    padding_y1 = 10

    if game.turn == WHITE:
        text_1 = font.render(f"White:{int(minute)}:{int(sec)}", True, TEXT_COLOR)
        rect_1 = text_1.get_rect(
            center=((OFFSET_PLATEAU_X + BORD_WIDTH) + OFFSET_PLATEAU_X / 2,(GAME_WINDOW_HEIGHT * (3 / 4))))
        surface_rect_1 = pygame.Rect(
            rect_1.left - padding_x1,
            rect_1.top - padding_y1,
            rect_1.width + 2 * padding_x1,
            rect_1.height + 2 * padding_y1)

        text_2 = font.render(f"Black:{int(minute_2)}:{int(sec_2)}", True, GRAY_TEXT_COLOR)
        rect_2 = text_2.get_rect(
            center=((OFFSET_PLATEAU_X + BORD_WIDTH) + OFFSET_PLATEAU_X / 2,(GAME_WINDOW_HEIGHT * (1 / 4))))

        surface_rect_2 = pygame.Rect(
            rect_2.left - padding_x1,
            rect_2.top - padding_y1,
            rect_2.width + 2 * padding_x1,
            rect_2.height + 2 * padding_y1)
        pygame.draw.rect(game.screen, BACKGROUND_COLOR, surface_rect_1)
        game.screen.blit(text_1, rect_1)

        pygame.draw.rect(game.screen, BACKGROUND_COLOR, surface_rect_2)
        game.screen.blit(text_2, rect_2)
    else:
        text_1 = font.render(f"White:{int(minute)}:{int(sec)}", True, GRAY_TEXT_COLOR)
        rect_1 = text_1.get_rect(
            center=((OFFSET_PLATEAU_X + BORD_WIDTH) + OFFSET_PLATEAU_X / 2, (GAME_WINDOW_HEIGHT * (3 / 4))))
        surface_rect_1 = pygame.Rect(
            rect_1.left - padding_x1,
            rect_1.top - padding_y1,
            rect_1.width + 2 * padding_x1,
            rect_1.height + 2 * padding_y1)

        text_2 = font.render(f"Black:{int(minute_2)}:{int(sec_2)}", True, TEXT_COLOR)
        rect_2 = text_2.get_rect(
            center=((OFFSET_PLATEAU_X + BORD_WIDTH) + OFFSET_PLATEAU_X / 2, (GAME_WINDOW_HEIGHT * (1 / 4))))
        surface_rect_2 = pygame.Rect(
            rect_2.left - padding_x1,
            rect_2.top - padding_y1,
            rect_2.width + 2 * padding_x1,
            rect_2.height + 2 * padding_y1)
        pygame.draw.rect(game.screen, BACKGROUND_COLOR, surface_rect_1)
        game.screen.blit(text_1, rect_1)

        pygame.draw.rect(game.screen, BACKGROUND_COLOR, surface_rect_2)
        game.screen.blit(text_2, rect_2)

def main_menu(game):

    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT),pygame.NOFRAME)
    font = pygame.font.SysFont("impact",60)
    text_play = font.render("PLAY",True,(254, 238, 202))
    text_play_rect = text_play.get_rect(center =(WINDOW_WIDTH/2,WINDOW_HEIGHT *2/3))
    padding_x1 = 20
    padding_y1 = 10
    play_button_rect = pygame.Rect(
        text_play_rect.left - padding_x1,
        text_play_rect.top - padding_y1,
        text_play_rect.width + 2 * padding_x1,
        text_play_rect.height + 2 * padding_y1
    )
    text_quit = font.render("QUIT",True,(254, 238, 202))
    text_quit_rect = text_quit.get_rect(center = (WINDOW_WIDTH/2,WINDOW_HEIGHT * 2.5/3))

    quit_button_rect = pygame.Rect(
        text_quit_rect.left - padding_x1,
        text_quit_rect.top - padding_y1,
        text_quit_rect.width + 2 * padding_x1,
        text_quit_rect.height + 2 * padding_y1
    )
    screen.fill(BACKGROUND_COLOR)
    logo = pygame.image.load("assets/ChessRush.png")
    logo_rect = logo.get_rect(center=(WINDOW_WIDTH/2,WINDOW_HEIGHT/3))
    menu = True
    screen.blit(logo,logo_rect)
    pygame.draw.rect(screen,(33, 32, 31),play_button_rect,border_radius=20)
    pygame.draw.rect(screen,(33, 32, 31),quit_button_rect,border_radius=20)
    screen.blit(text_quit,text_quit_rect)
    screen.blit(text_play,text_play_rect)
    while menu:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu = False
                    game.running =  False
            if event.type == pygame.MOUSEBUTTONUP:
                if play_button_rect.collidepoint(event.pos):
                    menu = False
                    mode_selecting(game,screen)
                elif quit_button_rect.collidepoint(event.pos):
                    menu = False
                    game.running = False

def mode_selecting(game,screen):

    # Initialisation
    pygame.init()
    pygame.display.set_caption("Menu de jeu d'échecs")
    clock = pygame.time.Clock()

    # Couleurs
    DARK_BG = BACKGROUND_COLOR
    CARD_BG = (30, 28, 26)
    TEXT_COLOR = (254, 238, 202)

    # Police
    pygame.font.init()
    font_title = pygame.font.SysFont("Impact", 32)
    font_button = pygame.font.SysFont("Impact", 28)

    # Données des colonnes
    columns = [
        {
            "title": "assets/icon-bullet.png",  # Icône bullet
            "modes": ["1 min", "1 | 1", "2 | 1"]
        },
        {
            "title": "assets/icon-lightning-bolt.png",  # Icône blitz
            "modes": ["3 min", "3 | 2", "5 min"]
        },
        {
            "title": "assets/icon-timer.png",  # Icône rapide
            "modes": ["10 min", "15 | 10", "30 min"]
        }
    ]

    def draw_column(x, y, width, height, title, modes):
        # Dessine la carte
        pygame.draw.rect(screen, CARD_BG, (x, y, width, height), border_radius=20)

        # Cercle icône
        pygame.draw.circle(screen, TEXT_COLOR, (x + width // 2, y - 25), 30)
        icon = pygame.image.load(title).convert_alpha()
        icon = pygame.transform.scale(icon,(50,50))
        icon_rect = icon.get_rect(center=(x + width // 2, y - 25))
        screen.blit(icon, icon_rect)

        # Dessine les boutons de texte
        button_height = 60
        spacing = 15
        button_rect = []
        for i, mode in enumerate(modes):
            button_y = y + 20 + i * (button_height + spacing)
            rect = pygame.Rect(x + 10, button_y, width - 20, button_height)
            pygame.draw.rect(screen, DARK_BG, rect, border_radius=15)
            text = font_button.render(mode, True, TEXT_COLOR)
            text_rect = text.get_rect(center=rect.center)
            screen.blit(text, text_rect)
            button_rect.append((rect,mode))
        return button_rect



    screen.fill(DARK_BG)

    margin = WINDOW_WIDTH/13
    col_width = WINDOW_WIDTH/4
    col_height = WINDOW_HEIGHT/2
    spacing = (WINDOW_WIDTH - 3 * col_width - 2 * margin) // 2
    y = 150
    all_button = []
    for i, col in enumerate(columns):
        x = margin + i * (col_width + spacing)
        button_rect = draw_column(x, y, col_width, col_height, col["title"], col["modes"])
        all_button.extend(button_rect)


    running = True
    while running:


        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONUP:
                mode_selected = False
                for (rect,mode) in all_button:
                    if rect.collidepoint(event.pos):
                        if mode == "1 min":
                            game.set_time(ONE_MIN)
                            mode_selected = True
                        elif mode == "1 | 1":
                            game.set_mode(ONE_MIN,1)
                            mode_selected = True
                        elif mode == "2 | 1":
                            game.set_mode(2*ONE_MIN,1)
                            mode_selected = True
                        elif mode == "3 min":
                            game.set_mode(3*ONE_MIN)
                            mode_selected = True
                        elif mode == "3 | 2":
                            game.set_mode(3*ONE_MIN,2)
                            mode_selected = True
                        elif mode == "5 min":
                            game.set_mode(FIVE_MIN)
                            mode_selected = True
                        elif mode == "10 min":
                            game.set_mode(TEN_MIN)
                            mode_selected = True
                        elif mode == "15 | 10":
                            game.set_mode(FIFTEENTH_MIN,10)
                            mode_selected = True
                        elif mode == "30 min":
                            game.set_mode(THIRTY_MIN)
                            mode_selected = True
                if mode_selected:
                    ATH_selecting(game,screen)
                    running = False

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()



def ATH_selecting(game,screen):
    pygame.init()
    font = pygame.font.SysFont("impact",60)
    paths = ["pieces","pieces_2","pieces_3","pieces_4"]
    bord_colors = [CLASSICAL_BORD,GREEN_BORD,CIEL_BORD,GRAY_BORD]

    running = True
    piece_index = 0
    color_index = 0
    piece = pygame.image.load(f"assets/{paths[piece_index]}/white-pawn.png")
    text_play = font.render("PLAY", True, (254, 238, 202))
    text_play_rect = text_play.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT * 4 / 5 ))
    padding_x1 = 20
    padding_y1 = 10
    play_button_rect = pygame.Rect(
        text_play_rect.left - padding_x1,
        text_play_rect.top - padding_y1,
        text_play_rect.width + 2 * padding_x1,
        text_play_rect.height + 2 * padding_y1
    )

    while running:
        piece_rect = piece.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 3))
        screen.fill(BACKGROUND_COLOR)
        piece = pygame.image.load(f"assets/{paths[piece_index]}/white-pawn.png")
        bord_rect = draw_bord(screen, game, True, WINDOW_WIDTH // 2 - 56, WINDOW_HEIGHT // 2, 112, 112, 14)
        screen.blit(piece, piece_rect)
        pygame.draw.rect(screen, (33, 32, 31), play_button_rect, border_radius=20)
        screen.blit(text_play,text_play_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONUP:
                if bord_rect.collidepoint(event.pos):
                    if color_index == len(bord_colors)-1:
                        color_index = 0
                        game.set_bord_color(bord_colors[color_index])
                    else:
                        color_index += 1
                        game.set_bord_color(bord_colors[color_index])
                if piece_rect.collidepoint(event.pos):
                    if piece_index == len(paths)-1:
                        piece_index = 0
                        pygame.draw.rect(screen,BACKGROUND_COLOR,piece_rect)
                        game.set_piece(paths[piece_index])
                    else:
                        piece_index += 1
                        pygame.draw.rect(screen,BACKGROUND_COLOR,piece_rect)
                        game.set_piece(paths[piece_index])
                if play_button_rect.collidepoint(event.pos):
                    running = False
                    game.is_playing = True







        pygame.display.flip()

















