import pygame
import world
import sys
import pygame_gui
from data import zastavkaImg

window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

begining = True
menu_bool = False
settings_bool = False


def settings():
    global settings_bool, menu_bool
    Height, Width = 700, 500
    lst_txts = []
    text_color = 'Blue'
    pos = window.get_size()[0] // 2 - Width // 2, window.get_size()[1] // 2 - Height // 2
    rect = pygame.draw.rect(window, "yellow", (*pos, Width, Height))
    font = pygame.font.Font(None, 60)
    text_y = rect.y + 40
    text_x = rect.x + 250
    count_y = rect.height // 5

    title = world.TxT("НАСТРОЙКИ", font, text_color, text_x, text_y)
    lst_txts.append(title)

    volume = world.TxT("громкость", font, text_color, text_x, text_y + count_y)
    lst_txts.append(volume)

    window_size = world.TxT("размер окна", font, text_color, text_x, text_y + count_y * 2)
    lst_txts.append(window_size)

    cancel = world.TxT("отменить", font, text_color, text_x, text_y + count_y * 3)
    lst_txts.append(cancel)

    save_changes = world.TxT("сохранить", font, text_color, text_x, text_y + count_y * 4)
    lst_txts.append(save_changes)
    if pygame.mouse.get_pressed()[0]:
        klickPos = pygame.mouse.get_pos()
        if volume[1].collidepoint(klickPos):
            pass
        if window_size[1].collidepoint(klickPos):
            pass
        if cancel[1].collidepoint(klickPos):
            settings_bool = False
            menu_bool = True
        if save_changes[1].collidepoint(klickPos):
            settings_bool = False
            menu_bool = True
    if pygame.key == pygame.K_ESCAPE and not begining:
        settings_bool = not settings_bool
    for i in lst_txts:
        window.blit(*i)


def menu():
    global menu_bool, settings_bool
    lst_txts = []
    Height, Width = 500, 500
    pos = window.get_size()[0] // 2 - Width // 2, window.get_size()[1] // 2 - Height // 2
    rect = pygame.draw.rect(window, "darkGray", (*pos, Width, Height))
    font = pygame.font.Font(None, 60)
    text_y = rect.y + 40
    text_x = rect.x + 250
    count_y = rect.height // 5
    title = world.TxT("МЕНЮ", font, (255, 77, 213), text_x, text_y)
    lst_txts.append(title)
    resume = world.TxT("продолжить", font, (255, 77, 213), text_x, text_y + count_y)
    lst_txts.append(resume)
    new_game = world.TxT("новая игра", font, (255, 77, 213), text_x, text_y + count_y * 2)
    lst_txts.append(new_game)
    settings_txt = world.TxT("настройки", font, (255, 77, 213), text_x, text_y + count_y * 3)
    lst_txts.append(settings_txt)
    quit = world.TxT("выйти из игры", font, (255, 77, 213), text_x, text_y + count_y * 4)
    lst_txts.append(quit)
    if pygame.mouse.get_pressed()[0]:
        klickPos = pygame.mouse.get_pos()
        if resume[1].collidepoint(klickPos):
            print(resume[1])
            menu_bool = False
        if quit[1].collidepoint(klickPos):
            pygame.quit()
            sys.exit()
        if new_game[1].collidepoint(klickPos):
            pass
        if settings_txt[1].collidepoint(klickPos):
            settings_bool = True
            menu_bool = False
    for i in lst_txts:
        window.blit(*i)


def zastavka():
    global begining, settings_bool, menu_bool
    intro_text = ["The lat letter", "",
                  "начать игру",
                  "настройки",
                  "выйти из игры"]
    lst_txts = []
    fon = pygame.transform.scale(zastavkaImg, window.get_size())
    window.blit(fon, (0, 0))
    font = pygame.font.Font(None, 70)
    title = world.TxT("The lat letter", font, (255, 77, 213), 200, 70)
    lst_txts.append(title)
    font = pygame.font.Font(None, 60)
    start = world.TxT("начать игру", font, (255, 77, 213), 200, 150)
    lst_txts.append(start)
    settings_txt = world.TxT("настройки", font, (255, 77, 213), 200, 200)
    lst_txts.append(settings_txt)
    quit = world.TxT("выйти из игры", font, (255, 77, 213), 200, 250)
    lst_txts.append(quit)
    if pygame.mouse.get_pressed()[0]:
        klickPos = pygame.mouse.get_pos()
        if start[1].collidepoint(klickPos):
            begining = False
            settings_bool = False
            menu_bool = False
        if quit[1].collidepoint(klickPos):
            pygame.quit()
            sys.exit()
        if settings_txt[1].collidepoint(klickPos):
            settings_bool = True
    if pygame.key == pygame.K_ESCAPE:
        settings_bool = False
    for i in lst_txts:
        window.blit(*i)
