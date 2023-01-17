import pygame
import world
import sys
import pygame_gui
from data import zastavkaImg
import mobs
from underground import Underground

pygame.init()

pygame.display.set_caption('Quick Start')

window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

manager = pygame_gui.UIManager(window.get_size())

under = Underground()

x_w, y_w = window.get_size()
x_w = x_w / 20
y_w = y_w / 20

coords_enemies = [(x_w * 5, y_w * 19, 'skeleton')]

bg = world.bg

mob_sprites = pygame.sprite.Group()
land_sprites = pygame.sprite.Group()
button_sprites = pygame.sprite.Group()
invisible_sprites = pygame.sprite.Group()

begining = True
menu_bool = False
settings_bool = False

enemies = []

hero = mobs.Hero(x_w * 0, y_w * 19, 'adventurer', mob_sprites, land_sprites, under.fight)

play_butt = world.Button(200, 150, 'play', button_sprites)
settings_butt = world.Button(200, 240, 'settings', button_sprites)
exit_butt = world.Button(200, 330, 'exit', button_sprites)
titles_butt = world.Button(200, 420, 'titles', button_sprites)
# new_game_butt = world.Button(200, 430, 'newgame', button_sprites)

for i in coords_enemies:
    pos = (i[0], i[1])
    name = i[2]
    mob = mobs.Enemies(*pos, name, mob_sprites, land_sprites)
    enemies.append(mob)


class Settings:
    def __init__(self, manager):
        self.manager = manager
        self.x, self.y = window.get_size()[0] // 2 - 200, window.get_size()[1] // 2 - 200
        self.window_sett = pygame_gui.elements.UIWindow(
            pygame.Rect(self.x, self.y, 400, 400),
            manager=self.manager)

        self.lst_window_size = ['на весь экран', 'оконный режим']
        self.lst_window_ratio = ['4:3', '16:9', '16:10']

        self.volume_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((10, 20), (100, 50)),
                                                        text='громкость',
                                                        manager=self.manager, container=self.window_sett)
        self.volume_slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((10, 70), (350, 20)),
                                                                    start_value=50,
                                                                    value_range=(0, 100),
                                                                    manager=self.manager, container=self.window_sett)
        self.value_volume = self.volume_slider.get_current_value()
        self.volume_value_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((280, 20), (100, 50)),
                                                              text=str(self.value_volume) + '%',
                                                              manager=self.manager, container=self.window_sett)

        self.resolution_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((10, 130), (140, 50)),
                                                            text='режим отображения',
                                                            manager=self.manager, container=self.window_sett)
        self.resolution = pygame_gui.elements.UIDropDownMenu(relative_rect=pygame.Rect((170, 140), (150, 30)),
                                                             options_list=self.lst_window_size,
                                                             starting_option='на весь экран',
                                                             manager=self.manager, container=self.window_sett)
        self.value_resolution = self.volume_slider.get_current_value()

        self.ratio_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((10, 170), (150, 50)),
                                                       text='соотношение сторон',
                                                       manager=self.manager, container=self.window_sett)
        self.ratio = pygame_gui.elements.UIDropDownMenu(relative_rect=pygame.Rect((170, 180), (150, 30)),
                                                        options_list=self.lst_window_ratio, starting_option='16:9',
                                                        manager=self.manager, container=self.window_sett)
        self.value_ratio = self.volume_slider.get_current_value()

        self.ok_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((50, 280), (100, 40)), text='применить',
                                                      manager=self.manager, container=self.window_sett)

        self.cancel_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((220, 280), (100, 40)),
                                                          text='отменить',
                                                          manager=self.manager, container=self.window_sett)

    def update(self, event, settings_bool):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.cancel_button:
                settings_bool = False
            elif event.ui_element == self.ok_button:
                pygame.mixer.music.set_volume(self.value_volume / 100 / 2)
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
            settings.window_sett.set_position((settings.x, settings.y))
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


def zastavka():
    global begining, settings_bool, menu_bool
    fon = pygame.transform.scale(zastavkaImg, window.get_size())
    window.blit(fon, (0, 0))
    font = pygame.font.Font(None, 70)
    title = world.TxT("The last letter", font, (255, 77, 213), 200, 70)
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
        enemies[i].rect.bottomleft = coords_enemies[i][0], coords_enemies[i][1] + 2
    under.fight = False
    hero.is_fight = False
    mob.is_fight = False
    hero.rect.bottomleft = x_w * 0, y_w * 19
