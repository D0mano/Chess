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
    screen.blit(logo,logo_rect)
    pygame.draw.rect(screen,(33, 32, 31),play_button_rect,border_radius=20)
    pygame.draw.rect(screen,(33, 32, 31),quit_button_rect,border_radius=20)
    screen.blit(text_quit,text_quit_rect)
    screen.blit(text_play,text_play_rect)
    while game.in_menu:
        screen.fill(BACKGROUND_COLOR)
        logo = pygame.image.load("assets/ChessRush.png")
        logo_rect = logo.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 3))
        screen.blit(logo, logo_rect)
        pygame.draw.rect(screen, (33, 32, 31), play_button_rect, border_radius=20)
        pygame.draw.rect(screen, (33, 32, 31), quit_button_rect, border_radius=20)
        screen.blit(text_quit, text_quit_rect)
        screen.blit(text_play, text_play_rect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game.in_menu = False
                    game.running =  False
            if event.type == pygame.MOUSEBUTTONUP:
                if play_button_rect.collidepoint(event.pos):
                    game.in_menu = False
                    game.in_mode_selection = True
                    mode_selecting(game,screen)
                elif quit_button_rect.collidepoint(event.pos):
                    game.in_menu = False
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


    while game.in_mode_selection:


        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.in_mode_selection = False
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    game.in_mode_selection = False
                    game.in_menu = True
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
                    game.in_mode_selection = False
                    ATH_selecting(game,screen)
                    screen.fill(DARK_BG)
                    for i, col in enumerate(columns):
                        x = margin + i * (col_width + spacing)
                        button_rect = draw_column(x, y, col_width, col_height, col["title"], col["modes"])
                        all_button.extend(button_rect)
        pygame.display.flip()
        clock.tick(60)




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
        piece = pygame.image.load(f"assets/{game.path}/white-pawn.png")
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
                    game.in_mode_selection = True
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



def End_banner(game,screen):
    # Couleurs
    white = (255, 255, 255)
    LIGHT_GRAY = (235, 234, 232)
    DARK_GRAY = (90, 90, 90)
    black = (0, 0, 0)

    # Police
    font_title = pygame.font.SysFont("Arial", 36, bold=True)
    font_score = pygame.font.SysFont("Arial", 28, bold=True)
    font_button = pygame.font.SysFont("Arial", 24)

    # Centrage
    banner_width = 300
    banner_height = 320
    banner_x = (GAME_WINDOW_WIDTH - banner_width) // 2
    banner_y = (GAME_WINDOW_HEIGHT - banner_height) // 2

    # Fonctions
    def draw_rounded_rect(surface, color, rect, radius=10):
        pygame.draw.rect(surface, color, rect, border_radius=radius)

    def draw_banner():
        # Fond principal
        draw_rounded_rect(screen, white, (banner_x, banner_y, banner_width, banner_height), radius=10)

        # Titre (ex. "White Won")
        title_rect = (banner_x + 20, banner_y - 40, banner_width - 40, 50)
        draw_rounded_rect(screen, DARK_GRAY, title_rect, radius=10)
        if (game.turn == BLACK and game.checkmate) or game.black_time < 1 :
            title_surf = font_title.render("White Won", True, white)
            score_text = font_score.render("1-0", True, black)

        elif (game.turn == WHITE and game.checkmate) or game.white_time < 1:
            title_surf = font_title.render("Black Won", True, white)
            score_text = font_score.render("0-1", True, black)

        else:
            title_surf = font_title.render("Stalemate", True, white)
            score_text = font_score.render("1/2-1/2", True, black)

        screen.blit(title_surf, (title_rect[0] + (title_rect[2] - title_surf.get_width()) // 2,
                                 title_rect[1] + (title_rect[3] - title_surf.get_height()) // 2))

        # Avatars
        avatar_size = 80
        avatar_y = banner_y + 50

        white_avatar = pygame.image.load("assets/white-avatar.png")
        white_avatar = pygame.transform.scale(white_avatar,(avatar_size, avatar_size))

        black_avatar = pygame.image.load("assets/black-avatar.png")
        black_avatar = pygame.transform.scale(black_avatar, (avatar_size, avatar_size))

        screen.blit(white_avatar,(banner_x + 40, avatar_y))
        screen.blit(black_avatar,(banner_x + banner_width - avatar_size - 40, avatar_y))


        screen.blit(score_text, (banner_x + (banner_width - score_text.get_width()) // 2,
                                 avatar_y + (avatar_size - score_text.get_height()) // 2))

        # Boutons
        button_width = 180
        button_height = 50
        button_spacing = 20
        button_y_start = avatar_y + avatar_size + 40

        rematch_rect = pygame.Rect(banner_x + (banner_width - button_width) // 2, button_y_start, button_width,
                                   button_height)
        quit_rect = pygame.Rect(banner_x + (banner_width - button_width) // 2,
                                button_y_start + button_height + button_spacing, button_width, button_height)

        draw_rounded_rect(screen, LIGHT_GRAY, rematch_rect, radius=10)
        draw_rounded_rect(screen, LIGHT_GRAY, quit_rect, radius=10)

        rematch_text = font_button.render("REMATCH", True, DARK_GRAY)
        quit_text = font_button.render("QUIT", True, DARK_GRAY)

        screen.blit(rematch_text, (rematch_rect.x + (rematch_rect.width - rematch_text.get_width()) // 2,
                                   rematch_rect.y + (rematch_rect.height - rematch_text.get_height()) // 2))
        screen.blit(quit_text, (quit_rect.x + (quit_rect.width - quit_text.get_width()) // 2,
                                quit_rect.y + (quit_rect.height - quit_text.get_height()) // 2))

        return rematch_rect, quit_rect

    pygame.time.delay(1500)

    # Boucle principale
    running = True
    rematch_button, quit_button = None, None
    while running:
        rematch_button, quit_button = draw_banner()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if rematch_button.collidepoint(event.pos):
                    print("Rematch !")
                    running = False
                    game.reinitialise_game()
                    game.set_bord(PLATEAU_INITIAL)
                    game.set_mode(game.time,game.increment_time)
                    game.star_game()

                elif quit_button.collidepoint(event.pos):
                    running = False
                    game.reinitialise_game()
                    game.is_playing = False
                    game.in_menu = True

        pygame.display.flip()

