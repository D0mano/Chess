import pygame.font
from pygame import K_ESCAPE, MOUSEBUTTONUP

from utils.functions import *


def display_current_player(game):
    """
    Display the current player's turn on the game screen.

    Args:
        game: Game object containing turn information and screen surface
    """
    pygame.init()
    font = pygame.font.SysFont("arial", 50)
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
    """
    Display the timer for both players on the game screen.
    Highlights the current player's timer and dims the opponent's timer.

    Args:
        game: Game object containing time information for both players
    """
    font = pygame.font.SysFont("Arial", 40)
    # Convert seconds to minutes and seconds for white player
    minute = game.white_time // 60
    sec = game.white_time % 60

    # Convert seconds to minutes and seconds for black player
    minute_2 = game.black_time // 60
    sec_2 = game.black_time % 60

    # Padding for timer display boxes
    padding_x1 = 20
    padding_y1 = 10

    if game.turn == WHITE:
        # Highlight white player's timer (active player)
        text_1 = font.render(f"White:{int(minute)}:{int(sec)}", True, TEXT_COLOR)
        rect_1 = text_1.get_rect(
            center=((OFFSET_PLATEAU_X + BORD_WIDTH) + OFFSET_PLATEAU_X / 2, (GAME_WINDOW_HEIGHT * (3 / 4))))
        surface_rect_1 = pygame.Rect(
            rect_1.left - padding_x1,
            rect_1.top - padding_y1,
            rect_1.width + 2 * padding_x1,
            rect_1.height + 2 * padding_y1)

        # Dim black player's timer (inactive player)
        text_2 = font.render(f"Black:{int(minute_2)}:{int(sec_2)}", True, GRAY_TEXT_COLOR)
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
    else:
        # Dim white player's timer (inactive player)
        text_1 = font.render(f"White:{int(minute)}:{int(sec)}", True, GRAY_TEXT_COLOR)
        rect_1 = text_1.get_rect(
            center=((OFFSET_PLATEAU_X + BORD_WIDTH) + OFFSET_PLATEAU_X / 2, (GAME_WINDOW_HEIGHT * (3 / 4))))
        surface_rect_1 = pygame.Rect(
            rect_1.left - padding_x1,
            rect_1.top - padding_y1,
            rect_1.width + 2 * padding_x1,
            rect_1.height + 2 * padding_y1)

        # Highlight black player's timer (active player)
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
    """
    Display the main menu with PLAY and QUIT buttons.
    Handles user input for menu navigation.

    Args:
        game: Game object to control menu state and game flow
    """
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.NOFRAME)
    font = pygame.font.SysFont("impact", 60)

    # Create PLAY button
    text_play = font.render("PLAY", True, (254, 238, 202))
    text_play_rect = text_play.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT * 2 / 3))
    padding_x1 = 20
    padding_y1 = 10
    play_button_rect = pygame.Rect(
        text_play_rect.left - padding_x1,
        text_play_rect.top - padding_y1,
        text_play_rect.width + 2 * padding_x1,
        text_play_rect.height + 2 * padding_y1
    )

    # Create QUIT button
    text_quit = font.render("QUIT", True, (254, 238, 202))
    text_quit_rect = text_quit.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT * 2.5 / 3))

    quit_button_rect = pygame.Rect(
        text_quit_rect.left - padding_x1,
        text_quit_rect.top - padding_y1,
        text_quit_rect.width + 2 * padding_x1,
        text_quit_rect.height + 2 * padding_y1
    )

    # Initial screen setup
    screen.fill(BACKGROUND_COLOR)
    logo = pygame.image.load("assets/ChessRush.png")
    logo_rect = logo.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 3))
    screen.blit(logo, logo_rect)
    pygame.draw.rect(screen, (33, 32, 31), play_button_rect, border_radius=20)
    pygame.draw.rect(screen, (33, 32, 31), quit_button_rect, border_radius=20)
    screen.blit(text_quit, text_quit_rect)
    screen.blit(text_play, text_play_rect)

    # Main menu loop
    while game.in_menu:
        # Redraw menu elements
        screen.fill(BACKGROUND_COLOR)
        logo = pygame.image.load("assets/ChessRush.png")
        logo_rect = logo.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 3))
        screen.blit(logo, logo_rect)
        pygame.draw.rect(screen, (33, 32, 31), play_button_rect, border_radius=20)
        pygame.draw.rect(screen, (33, 32, 31), quit_button_rect, border_radius=20)
        screen.blit(text_quit, text_quit_rect)
        screen.blit(text_play, text_play_rect)
        pygame.display.flip()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game.in_menu = False
                    game.running = False
            if event.type == pygame.MOUSEBUTTONUP:
                if play_button_rect.collidepoint(event.pos):
                    game.in_menu = False
                    game.in_mode_selection = True
                    mode_selecting(game, screen)
                elif quit_button_rect.collidepoint(event.pos):
                    game.in_menu = False
                    game.running = False


def mode_selecting(game, screen):
    """
    Display the game mode selection screen with different time controls.
    Organized in three columns: Bullet, Blitz, and Rapid games.

    Args:
        game: Game object to store selected time control
        screen: Pygame screen surface for rendering
    """
    # Initialization
    pygame.init()
    pygame.display.set_caption("Menu de jeu d'échecs")
    clock = pygame.time.Clock()

    # Color definitions
    DARK_BG = BACKGROUND_COLOR
    CARD_BG = (30, 28, 26)
    TEXT_COLOR = (254, 238, 202)

    # Font initialization
    pygame.font.init()
    font_title = pygame.font.SysFont("Impact", 32)
    font_button = pygame.font.SysFont("Impact", 28)

    # Column data with icons and time controls
    columns = [
        {
            "title": "assets/icon-bullet.png",  # Bullet chess icon
            "modes": ["1 min", "1 | 1", "2 | 1"]
        },
        {
            "title": "assets/icon-lightning-bolt.png",  # Blitz chess icon
            "modes": ["3 min", "3 | 2", "5 min"]
        },
        {
            "title": "assets/icon-timer.png",  # Rapid chess icon
            "modes": ["10 min", "15 | 10", "30 min"]
        }
    ]

    def draw_column(x, y, width, height, title, modes):
        """
        Draw a single column with icon and time control buttons.

        Args:
            x, y: Position coordinates
            width, height: Column dimensions
            title: Path to icon image
            modes: List of time control strings

        Returns:
            List of (rect, mode) tuples for button collision detection
        """
        # Draw the card background
        pygame.draw.rect(screen, CARD_BG, (x, y, width, height), border_radius=20)

        # Draw icon circle and load icon
        pygame.draw.circle(screen, TEXT_COLOR, (x + width // 2, y - 25), 30)
        icon = pygame.image.load(title).convert_alpha()
        icon = pygame.transform.scale(icon, (50, 50))
        icon_rect = icon.get_rect(center=(x + width // 2, y - 25))
        screen.blit(icon, icon_rect)

        # Draw time control buttons
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
            button_rect.append((rect, mode))
        return button_rect

    # Initial screen setup
    screen.fill(DARK_BG)

    # Calculate column positions
    margin = WINDOW_WIDTH / 13
    col_width = WINDOW_WIDTH / 4
    col_height = WINDOW_HEIGHT / 2
    spacing = (WINDOW_WIDTH - 3 * col_width - 2 * margin) // 2
    y = 150
    all_button = []

    # Draw all columns and collect button rectangles
    for i, col in enumerate(columns):
        x = margin + i * (col_width + spacing)
        button_rect = draw_column(x, y, col_width, col_height, col["title"], col["modes"])
        all_button.extend(button_rect)

    # Mode selection loop
    while game.in_mode_selection:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.in_mode_selection = False
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    game.in_mode_selection = False
                    game.in_menu = True
            if event.type == pygame.MOUSEBUTTONUP:
                mode_selected = False
                # Check which time control button was clicked
                for (rect, mode) in all_button:
                    if rect.collidepoint(event.pos):
                        # Set time control based on selected mode
                        if mode == "1 min":
                            game.set_time(ONE_MIN)
                            mode_selected = True
                        elif mode == "1 | 1":
                            game.set_mode(ONE_MIN, 1)
                            mode_selected = True
                        elif mode == "2 | 1":
                            game.set_mode(2 * ONE_MIN, 1)
                            mode_selected = True
                        elif mode == "3 min":
                            game.set_mode(3 * ONE_MIN)
                            mode_selected = True
                        elif mode == "3 | 2":
                            game.set_mode(3 * ONE_MIN, 2)
                            mode_selected = True
                        elif mode == "5 min":
                            game.set_mode(FIVE_MIN)
                            mode_selected = True
                        elif mode == "10 min":
                            game.set_mode(TEN_MIN)
                            mode_selected = True
                        elif mode == "15 | 10":
                            game.set_mode(FIFTEENTH_MIN, 10)
                            mode_selected = True
                        elif mode == "30 min":
                            game.set_mode(THIRTY_MIN)
                            mode_selected = True

                # Proceed to appearance selection if mode was selected
                if mode_selected:
                    game.in_mode_selection = False
                    ATH_selecting(game, screen)
                    # Redraw columns after returning from appearance selection
                    screen.fill(DARK_BG)
                    for i, col in enumerate(columns):
                        x = margin + i * (col_width + spacing)
                        button_rect = draw_column(x, y, col_width, col_height, col["title"], col["modes"])
                        all_button.extend(button_rect)
        pygame.display.flip()
        clock.tick(60)


def ATH_selecting(game, screen):
    """
    Display the appearance/theme selection screen.
    Allows players to choose piece sets and board colors.

    Args:
        game: Game object to store appearance preferences
        screen: Pygame screen surface for rendering
    """
    pygame.init()
    font = pygame.font.SysFont("impact", 60)

    # Available piece sets and board colors
    paths = ["pieces", "pieces_2", "pieces_3", "pieces_4"]
    bord_colors = [CLASSICAL_BORD, GREEN_BORD, CIEL_BORD, GRAY_BORD,PINK_BORD   ]

    running = True
    piece_index = 0
    color_index = 0

    # Load initial piece for preview
    piece = pygame.image.load(f"assets/{paths[piece_index]}/white-pawn.png")

    # Create PLAY button
    text_play = font.render("PLAY", True, (254, 238, 202))
    text_play_rect = text_play.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT * 4 / 5))
    padding_x1 = 20
    padding_y1 = 10
    play_button_rect = pygame.Rect(
        text_play_rect.left - padding_x1,
        text_play_rect.top - padding_y1,
        text_play_rect.width + 2 * padding_x1,
        text_play_rect.height + 2 * padding_y1
    )

    # Appearance selection loop
    while running:
        piece_rect = piece.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 3))
        screen.fill(BACKGROUND_COLOR)

        # Load and display current piece set
        piece = pygame.image.load(f"assets/{game.path}/white-pawn.png")

        # Draw board preview with current color scheme
        bord_rect = draw_bord(screen, game, True, WINDOW_WIDTH // 2 - 56, WINDOW_HEIGHT // 2, 112, 112, 14)
        screen.blit(piece, piece_rect)

        # Draw PLAY button
        pygame.draw.rect(screen, (33, 32, 31), play_button_rect, border_radius=20)
        screen.blit(text_play, text_play_rect)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                    game.in_mode_selection = True
            if event.type == MOUSEBUTTONUP:
                # Cycle through board colors when board is clicked
                if bord_rect.collidepoint(event.pos):
                    if color_index == len(bord_colors) - 1:
                        color_index = 0
                        game.set_bord_color(bord_colors[color_index])
                    else:
                        color_index += 1
                        game.set_bord_color(bord_colors[color_index])

                # Cycle through piece sets when piece is clicked
                if piece_rect.collidepoint(event.pos):
                    if piece_index == len(paths) - 1:
                        piece_index = 0
                        pygame.draw.rect(screen, BACKGROUND_COLOR, piece_rect)
                        game.set_piece(paths[piece_index])
                    else:
                        piece_index += 1
                        pygame.draw.rect(screen, BACKGROUND_COLOR, piece_rect)
                        game.set_piece(paths[piece_index])

                # Start game when PLAY button is clicked
                if play_button_rect.collidepoint(event.pos):
                    running = False
                    game.is_playing = True

        pygame.display.flip()


def End_banner(game, screen):
    """
    Display the end game banner showing results and options.
    Shows winner, final score, and buttons for rematch or quit.

    Args:
        game: Game object containing game state and results
        screen: Pygame screen surface for rendering
    """
    # Color definitions
    white = (255, 255, 255)
    LIGHT_GRAY = (235, 234, 232)
    DARK_GRAY = (90, 90, 90)
    black = (0, 0, 0)

    # Font definitions
    font_title = pygame.font.SysFont("Arial", 36, bold=True)
    font_score = pygame.font.SysFont("Arial", 22, bold=True)
    font_button = pygame.font.SysFont("Arial", 24)

    # Banner positioning
    banner_width = 300
    banner_height = 320
    banner_x = (GAME_WINDOW_WIDTH - banner_width) // 2
    banner_y = (GAME_WINDOW_HEIGHT - banner_height) // 2

    def draw_rounded_rect(surface, color, rect, radius=10):
        """
        Draw a rectangle with rounded corners.

        Args:
            surface: Pygame surface to draw on
            color: Color tuple for the rectangle
            rect: Rectangle coordinates (x, y, width, height)
            radius: Corner radius for rounding
        """
        pygame.draw.rect(surface, color, rect, border_radius=radius)

    def draw_banner():
        """
        Draw the complete end game banner with all elements.

        Returns:
            Tuple of (rematch_button_rect, quit_button_rect) for event handling
        """
        # Draw main background
        draw_rounded_rect(screen, white, (banner_x, banner_y, banner_width, banner_height), radius=10)

        # Draw title section and determine winner
        title_rect = (banner_x + 20, banner_y - 40, banner_width - 40, 50)
        draw_rounded_rect(screen, DARK_GRAY, title_rect, radius=10)

        # Determine game result and display appropriate message
        if (game.turn == BLACK and game.checkmate) or game.black_time < 1:
            title_surf = font_title.render("White Won", True, white)
            score_text = font_score.render("1-0", True, black)
        elif (game.turn == WHITE and game.checkmate) or game.white_time < 1:
            title_surf = font_title.render("Black Won", True, white)
            score_text = font_score.render("0-1", True, black)
        else:
            title_surf = font_title.render("Stalemate", True, white)
            score_text = font_score.render("1/2-1/2", True, black)

        # Center and draw title text
        screen.blit(title_surf, (title_rect[0] + (title_rect[2] - title_surf.get_width()) // 2,
                                 title_rect[1] + (title_rect[3] - title_surf.get_height()) // 2))

        # Draw player avatars
        avatar_size = 80
        avatar_y = banner_y + 50

        # Load and scale avatars
        white_avatar = pygame.image.load("assets/white-avatar.png")
        white_avatar = pygame.transform.scale(white_avatar, (avatar_size, avatar_size))

        black_avatar = pygame.image.load("assets/black-avatar.png")
        black_avatar = pygame.transform.scale(black_avatar, (avatar_size, avatar_size))

        # Position avatars
        screen.blit(white_avatar, (banner_x + 40, avatar_y))
        screen.blit(black_avatar, (banner_x + banner_width - avatar_size - 40, avatar_y))

        # Draw score text between avatars
        screen.blit(score_text, (banner_x + (banner_width - score_text.get_width()) // 2,
                                 avatar_y + (avatar_size - score_text.get_height()) // 2))

        # Draw action buttons
        button_width = 180
        button_height = 50
        button_spacing = 20
        button_y_start = avatar_y + avatar_size + 40

        # Create button rectangles
        rematch_rect = pygame.Rect(banner_x + (banner_width - button_width) // 2, button_y_start, button_width,
                                   button_height)
        quit_rect = pygame.Rect(banner_x + (banner_width - button_width) // 2,
                                button_y_start + button_height + button_spacing, button_width, button_height)

        # Draw button backgrounds
        draw_rounded_rect(screen, LIGHT_GRAY, rematch_rect, radius=10)
        draw_rounded_rect(screen, LIGHT_GRAY, quit_rect, radius=10)

        # Create and draw button text
        rematch_text = font_button.render("REMATCH", True, DARK_GRAY)
        quit_text = font_button.render("QUIT", True, DARK_GRAY)

        # Center button text
        screen.blit(rematch_text, (rematch_rect.x + (rematch_rect.width - rematch_text.get_width()) // 2,
                                   rematch_rect.y + (rematch_rect.height - rematch_text.get_height()) // 2))
        screen.blit(quit_text, (quit_rect.x + (quit_rect.width - quit_text.get_width()) // 2,
                                quit_rect.y + (quit_rect.height - quit_text.get_height()) // 2))

        return rematch_rect, quit_rect

    # Brief delay before showing banner
    pygame.time.delay(1500)

    # Main banner loop
    running = True
    rematch_button, quit_button = None, None
    while running:
        # Draw banner and get button rectangles
        rematch_button, quit_button = draw_banner()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Handle rematch button click
                if rematch_button.collidepoint(event.pos):
                    print("Rematch !")
                    running = False
                    game.reinitialise_game()
                    game.is_playing = True

                # Handle quit button click
                elif quit_button.collidepoint(event.pos):
                    running = False
                    game.reinitialise_game()
                    game.is_playing = False
                    game.in_menu = True

        pygame.display.flip()