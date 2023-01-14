import pygame
import world
import sys
import pygame_gui
from data import zastavkaImg
import mobs
from underground import Underground

window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

under = Underground()

x_w, y_w = window.get_size()
x_w = x_w / 20
y_w = y_w / 20

coords_enemies = [(x_w * 5, y_w * 19, 'skeleton')]

bg = world.bg

mob_sprites = pygame.sprite.Group()
land_sprites = pygame.sprite.Group()
button_sprites = pygame.sprite.Group()

begining = True
menu_bool = False
settings_bool = False

enemies = []

hero = mobs.Hero(x_w * 0, y_w * 19, 'adventurer', mob_sprites, land_sprites, under.fight)

play_butt = world.Button(200, 150, 'play', button_sprites)
settings_butt = world.Button(200, 240, 'settings', button_sprites)
exit_butt = world.Button(200, 330, 'exit', button_sprites)
#new_game_butt = world.Button(200, 430, 'newgame', button_sprites)

for i in coords_enemies:
    pos = (i[0], i[1])
    name = i[2]
    mob = mobs.Enemies(*pos, name, mob_sprites, land_sprites)
    enemies.append(mob)


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

    play_butt.rect.center = text_x, text_y + count_y
    play_butt.status = 'idle'
    settings_butt.rect.center = text_x, text_y + count_y * 3
    exit_butt.rect.center = text_x, text_y + count_y * 4

    new_game = world.TxT("новая игра", font, (255, 77, 213), text_x, text_y + count_y * 2)
    lst_txts.append(new_game)
    if pygame.mouse.get_pressed()[0]:
        klickPos = pygame.mouse.get_pos()
        if play_butt.rect.collidepoint(klickPos):
            play_butt.status = 'pressed'
            menu_bool = False
        if exit_butt.rect.collidepoint(klickPos):
            exit_butt.status = 'pressed'
            pygame.quit()
            sys.exit()
        if new_game[1].collidepoint(klickPos):
            new_game_func()
        if settings_butt.rect.collidepoint(klickPos):
            settings_butt.status = 'pressed'
            settings_bool = True
            menu_bool = False
    else:
        aimPos = pygame.mouse.get_pos()
        if play_butt.rect.collidepoint(aimPos):
            play_butt.status = 'aim'
        else:
            play_butt.status = 'idle'
        if exit_butt.rect.collidepoint(aimPos):
            exit_butt.status = 'aim'
        else:
            exit_butt.status = 'idle'
        if settings_butt.rect.collidepoint(aimPos):
            settings_butt.status = 'aim'
        else:
            settings_butt.status = 'idle'

    for i in lst_txts:
        window.blit(*i)

def settinks():
    manager = pygame_gui.UIManager((800, 600))

    window = pygame_gui.elements.UIWindow(pygame.Rect(100, 100, 300, 300), manager=manager)

    hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),
                                                text='Say Hello',
                                                manager=manager, container=window)
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
    if pygame.mouse.get_pressed()[0]:
        klickPos = pygame.mouse.get_pos()
        if play_butt.rect.collidepoint(klickPos):
            play_butt.status = 'pressed'
            begining = False
            settings_bool = False
            menu_bool = False
        if exit_butt.rect.collidepoint(klickPos):
            exit_butt.status = 'pressed'
            pygame.quit()
            sys.exit()
        if settings_butt.rect.collidepoint(klickPos):
            settings_butt.status = 'pressed'
            settings_bool = True
    else:
        aimPos = pygame.mouse.get_pos()
        if play_butt.rect.collidepoint(aimPos):
            play_butt.status = 'aim'
        else:
            play_butt.status = 'idle'
        if exit_butt.rect.collidepoint(aimPos):
            exit_butt.status = 'aim'
        else:
            exit_butt.status = 'idle'
        if settings_butt.rect.collidepoint(aimPos):
            settings_butt.status = 'aim'
        else:
            settings_butt.status = 'idle'
    if pygame.key == pygame.K_ESCAPE:
        settings_bool = False
    for i in lst_txts:
        window.blit(*i)


def new_game_func():
    for i in range(len(enemies)):
        enemies[i].rect.bottomleft = coords_enemies[i][0], coords_enemies[i][1] + 2
    under.fight = False
    hero.is_fight = False
    mob.is_fight = False
    hero.rect.bottomleft = x_w * 0, y_w * 19
