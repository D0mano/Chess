from utils.functions import *

def display_current_player(game):
    font = pygame.font.SysFont("Arial" ,50)
    if game.turn == WHITE:
        text = font.render("White to play !", True, TEXT_COLOR)
        rect = text.get_rect(center=(OFFSET_PLATEAU_X/2,(WINDOW_HEIGHT-OFFSET_PLATEAU_Y)/2))
        pygame.draw.rect(game.screen,(0,0,0),rect)
        game.screen.blit(text,rect)
    else:
        text = font.render("Black to play !", True, TEXT_COLOR)
        rect = text.get_rect(center=(OFFSET_PLATEAU_X / 2, (WINDOW_HEIGHT - OFFSET_PLATEAU_Y) / 2))
        pygame.draw.rect(game.screen, (0, 0, 0), rect)
        game.screen.blit(text, rect)

def display_timer(game):
    font = pygame.font.SysFont("Arial", 40)
    minute = game.white_time // 60
    sec = game.white_time % 60

    minute_2 = game.black_time // 60
    sec_2 = game.black_time % 60

    if game.turn == WHITE:
        text_1 = font.render(f"White:{int(minute)}:{int(sec)}", True, TEXT_COLOR)
        rect_1 = text_1.get_rect(
            center=((OFFSET_PLATEAU_X + BORD_WIDTH) + OFFSET_PLATEAU_X / 2,(WINDOW_HEIGHT * (3 / 4))))

        text_2 = font.render(f"Black:{int(minute_2)}:{int(sec_2)}", True, GRAY_TEXT_COLOR)
        rect_2 = text_2.get_rect(
            center=((OFFSET_PLATEAU_X + BORD_WIDTH) + OFFSET_PLATEAU_X / 2,(WINDOW_HEIGHT * (1 / 4))))
        pygame.draw.rect(game.screen,(0,0,0),rect_1)
        game.screen.blit(text_1,rect_1)

        pygame.draw.rect(game.screen, (0, 0, 0), rect_2)
        game.screen.blit(text_2, rect_2)
    else:
        text_1 = font.render(f"White:{int(minute)}:{int(sec)}", True, GRAY_TEXT_COLOR)
        rect_1 = text_1.get_rect(
            center=((OFFSET_PLATEAU_X + BORD_WIDTH) + OFFSET_PLATEAU_X / 2, (WINDOW_HEIGHT * (3 / 4))))

        text_2 = font.render(f"Black:{int(minute_2)}:{int(sec_2)}", True, TEXT_COLOR)
        rect_2 = text_2.get_rect(
            center=((OFFSET_PLATEAU_X + BORD_WIDTH) + OFFSET_PLATEAU_X / 2, (WINDOW_HEIGHT * (1 / 4))))
        pygame.draw.rect(game.screen, (0, 0, 0), rect_1)
        game.screen.blit(text_1, rect_1)

        pygame.draw.rect(game.screen, (0, 0, 0), rect_2)
        game.screen.blit(text_2, rect_2)






