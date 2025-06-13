from pygame import RESIZABLE

from classes.interface import display_current_player, display_timer
from utils.functions import *
from classes.game import Game



pygame.init()




screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT),RESIZABLE)
run = True
game = Game(screen)
display_current_player(game)
bord = draw_bord(screen)
clock = pygame.time.Clock()
selected_square = None
game.game_start_sound.play()
game.set_time(TEN_MIN)
while run:
    dt = clock.tick(30)/1000

    display_timer(game)
    game.decrement_time(game.turn,dt)


    for i in range(len(game.bord)):
        for piece in game.bord[i]:
            if piece is not None:
                screen.blit(piece.image,piece.rect)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONUP:
            if selected_square is None:
                selected_square = is_select(game, event)
            else:
                start_x,start_y = selected_square[0],selected_square[1]
                if xy_to_chess(event.pos) is not None:
                    end_x,end_y = xy_to_chess(event.pos)
                    movement = move(game, start_x, start_y, end_x, end_y)
                   # if movement is not None:
                       # print(movement)

                selected_square = None
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

    pygame.display.flip()


pygame.quit()
