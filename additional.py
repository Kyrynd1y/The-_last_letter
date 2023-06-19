import pygame

import data
import test
import world
import sys
import pygame_gui
from data import zastavkaImg
import mobs
from underground import Underground
from test import titles

pygame.init()

pygame.display.set_caption('Quick Start')

window = data.window
screen_size = window.get_size()
print(screen_size)

manager = pygame_gui.UIManager(window.get_size())

under = Underground()

x_w, y_w = window.get_size()
x_w = x_w / 20
y_w = y_w / 20

coords_enemies = [(x_w * 2, y_w * 9, 'skeleton'), (x_w * 15, y_w * 9, 'skeleton'), (x_w * 34, y_w * 5, 'skeleton'),
                  (x_w * 23, y_w * 6, 'skeleton'),
                  (x_w * 33.5, y_w * 12.7, 'skeleton')]

bg = world.bg

mob_sprites = pygame.sprite.Group()
decor_sprites = pygame.sprite.Group()
land_sprites = pygame.sprite.Group()
button_sprites = pygame.sprite.Group()

begining = True
menu_bool = False
settings_bool = False

enemies = []

hero = mobs.Hero(x_w * 0, y_w * 19, 'adventurer', mob_sprites, land_sprites, under.fight)
# 0, 19
play_butt = world.Button(2.0833 * x_w, 2.7777 * y_w, 'play', button_sprites)
settings_butt = world.Button(2.0833 * x_w, 4.444444 * y_w, 'settings', button_sprites)
exit_butt = world.Button(2.0833 * x_w, 6.11111 * y_w, 'exit', button_sprites)
new_game_butt = world.Button(0, 0, 'newgame', button_sprites)
titles_butt = world.Button(2.0833 * x_w, 7.777777 * y_w, 'titles', button_sprites)

for i in coords_enemies:
    pos = (i[0], i[1])
    name = i[2]
    mob = mobs.Enemies(*pos, name, mob_sprites, land_sprites)
    enemies.append(mob)


class Settings:
    def __init__(self, manager):
        self.manager = manager
        self.x, self.y = window.get_size()[0] // 2 - (2.0833 * x_w), window.get_size()[1] // 2 - (2.0833 * x_w)
        self.window_sett = pygame_gui.elements.UIWindow(
            pygame.Rect(self.x, self.y, 4.166666 * x_w, 7.407407 * y_w),
            manager=self.manager)

        self.lst_window_size = ['на весь экран', '4:3', '16:9', '16:10']

        self.volume_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0.104166 * x_w, 0.370370 * y_w), (1.041666 * x_w, 0.925925 * y_w)),
                                                        text='громкость',
                                                        manager=self.manager, container=self.window_sett)
        self.volume_slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((0.104166 * x_w, 1.296296 * y_w), (3.645833 * x_w, 0.370370 * y_w)),
                                                                    start_value=50,
                                                                    value_range=(0, 100),
                                                                    manager=self.manager, container=self.window_sett)
        self.value_volume = self.volume_slider.get_current_value()
        self.volume_value_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((2.91666 * x_w, 0.370370 * y_w), (1.041666 * x_w, 0.926926 * y_w)),
                                                              text=str(self.value_volume) + '%',
                                                              manager=self.manager, container=self.window_sett)

        self.resolution_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0.104166 * x_w, 2.407407 * y_w), (1.458333 * x_w, 0.926926 * y_w)),
                                                            text='режим отображения',
                                                            manager=self.manager, container=self.window_sett)
        self.resolution = pygame_gui.elements.UIDropDownMenu(relative_rect=pygame.Rect((1.7708333 * x_w, 2.5925925 * y_w), (1.5625 * x_w, 0.555555 * y_w)),
                                                             options_list=self.lst_window_size,
                                                             starting_option='на весь экран',
                                                             manager=self.manager, container=self.window_sett)
        self.value_resolution = self.volume_slider.get_current_value()

        self.value_ratio = self.resolution

        self.ok_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0.5208333 * x_w, 5.185185 * y_w), (1.041666 * x_w, 0.740740 * y_w)), text='применить',
                                                      manager=self.manager, container=self.window_sett)

        self.cancel_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((2.291666 * x_w, 5.185185 * y_w), (1.041666 * x_w, 0.740740 * y_w)),
                                                          text='отменить',
                                                          manager=self.manager, container=self.window_sett)
        self.comit_screen_size = screen_size

    def update(self, event, settings_bool):
        global window
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.cancel_button:
                settings_bool = False
            elif event.ui_element == self.ok_button:
                pygame.mixer.music.set_volume(self.value_volume / 100 / 2)
                window = pygame.display.set_mode(self.comit_screen_size, pygame.RESIZABLE)
                settings_bool = False
        if event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
            if event.ui_element == self.resolution:
                size = event.text
                if size == '4:3':
                    for i in range(len(data.lst_window_sized_3_4)):
                        if data.lst_window_sized_3_4[i] > screen_size:
                            if i == 0:
                                i = 1
                            size = data.lst_window_sized_3_4[i - 1]
                            self.comit_screen_size = size
                            break
                elif size == '16:9':
                    for i in range(len(data.lst_window_sized_16_9)):
                        print(data.lst_window_sized_16_9[i], screen_size)
                        if data.lst_window_sized_16_9[i] > screen_size:
                            if i == 0:
                                i = 1
                            size = data.lst_window_sized_16_9[i - 1]
                            self.comit_screen_size = size
                            break
                elif size == '16:10':
                    for i in range(len(data.lst_window_sized_16_10)):
                        if data.lst_window_sized_16_10[i] > screen_size:
                            if i == 0:
                                i = 1
                            size = data.lst_window_sized_16_10[i - 1]
                            self.comit_screen_size = size
                            break
                elif size == 'на весь экран':
                    self.comit_screen_size = screen_size
        if event.type == pygame_gui.UI_WINDOW_CLOSE:
            if event.ui_element == window:
                settings_bool = False
        return settings_bool

    def draw(self):
        self.value_volume = self.volume_slider.get_current_value()
        self.volume_value_label.set_text(str(self.value_volume) + '%')
        manager.draw_ui(window)


settings = Settings(manager)


def menu():
    global menu_bool, settings_bool
    lst_txts = []
    Height, Width = 5.208333 * x_w, 9.259259 * y_w
    pos = window.get_size()[0] // 2 - Width // 2, window.get_size()[1] // 2 - Height // 2
    rect = pygame.draw.rect(window, "darkGreen", (*pos, Width, Height))
    font = pygame.font.Font(None, 60)
    text_y = rect.y + 0.740740 * y_w
    text_x = rect.x + 2.6041666 * x_w
    count_y = rect.height // 5
    #    window.blit(data.menu_fon, pos)
    #    window.blit(data.menu_title, (text_x - 150, text_y - 80))
    title = world.TxT("МЕНЮ", font, (255, 77, 213), text_x, text_y)
    lst_txts.append(title)

    play_butt.rect.center = text_x, text_y + count_y
    play_butt.status = 'idle'
    settings_butt.rect.center = text_x, text_y + count_y * 3
    exit_butt.rect.center = text_x, text_y + count_y * 4
    new_game_butt.rect.center = text_x, text_y + count_y * 2
    new_game_butt.add(button_sprites)
    play_butt.add(button_sprites)
    settings_butt.add((button_sprites))
    titles_butt.kill()

    if pygame.mouse.get_pressed()[0]:
        klickPos = pygame.mouse.get_pos()
        if play_butt.rect.collidepoint(klickPos):
            menu_bool = False
        if exit_butt.rect.collidepoint(klickPos):
            pygame.quit()
            sys.exit()
        if new_game_butt.rect.collidepoint(klickPos):
            new_game_func()
        if settings_butt.rect.collidepoint(klickPos):
            settings_bool = True
            settings.window_sett.set_position((settings.x, settings.y))
            menu_bool = False
        if titles_butt.rect.collidepoint(klickPos):
            test.titles()

    for i in lst_txts:
        window.blit(*i)


def zastavka():
    global begining, settings_bool, menu_bool
    fon = pygame.transform.scale(zastavkaImg, window.get_size())
    window.blit(fon, (0, 0))
    font = pygame.font.Font(None, 70)
    title = world.TxT("The last letter", font, (255, 77, 213), 2.08333 * x_w, 1.296296 * y_w)
    play_butt.rect.center = 2.08333 * x_w, 2.777777 * y_w
    settings_butt.rect.center = 2.08333 * x_w, 4.444444 * y_w
    exit_butt.rect.center = 2.08333 * x_w, 6.111111 * y_w
    new_game_butt.kill()

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
            settings.window_sett.set_position((settings.x, settings.y))
        if titles_butt.rect.collidepoint(klickPos):
            test.titles()
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
    window.blit(*title)


def new_game_func():
    for i in range(len(enemies)):
        enemies[i].rect.bottomleft = coords_enemies[i][0], coords_enemies[i][1] + 0.0208333 * x_w
        enemies[i].live = True
        enemies[i].add(mob_sprites, land_sprites)
    under.fight = False
    hero.is_fight = False
    mob.is_fight = False
    hero.rect.bottomleft = x_w * 0, y_w * 19.05
    hero.jump_coords = hero.rect.y
    hero.hp = 3
