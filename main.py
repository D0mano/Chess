from classes.interface import *
from utils.functions import *
from classes.game import Game



pygame.init()
game = Game()


while game.running:
    if game.is_playing:
        game_screen = pygame.display.set_mode((GAME_WINDOW_WIDTH, GAME_WINDOW_HEIGHT),pygame.FULLSCREEN)
        game.set_screen(game_screen)
        game.set_bord(PLATEAU_INITIAL)
        game.star_game()
    else:
        main_menu(game)


pygame.quit()
