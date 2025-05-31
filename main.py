from utils.functions import *
from classes.game import Game



pygame.init()




screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
run = True
game = Game(screen)
bord = draw_bord(screen, OFFSET_PLATEAU_X, OFFSET_PLATEAU_Y)

while run:


    game.update()


    for i in range(len(game.bord)):
        for piece in game.bord[i]:
            if piece is not None:
                screen.blit(piece.image,piece.rect)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONUP:
            selection = is_select(game,event)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

    pygame.display.flip()


pygame.quit()