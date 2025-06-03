from utils.functions import *

def display_current_player(game):
    font = pygame.font.Font(None ,50)
    if game.turn == WHITE:
        text = font.render("White to play !",True,COULEUR_TEXTE)
        rect = text.get_rect(center=(OFFSET_PLATEAU_X/2,(WINDOW_HEIGHT-OFFSET_PLATEAU_Y)/2))
        pygame.draw.rect(game.screen,(0,0,0),rect)
        game.screen.blit(text,rect)
    else:
        text = font.render("Black to play !", True, COULEUR_TEXTE)
        rect = text.get_rect(center=(OFFSET_PLATEAU_X / 2, (WINDOW_HEIGHT - OFFSET_PLATEAU_Y) / 2))
        pygame.draw.rect(game.screen, (0, 0, 0), rect)
        game.screen.blit(text, rect)




