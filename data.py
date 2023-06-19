import os

import pygame

window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
x_w = window.get_size()[0] / 20
y_w = window.get_size()[1] / 20
print(x_w, y_w)

statuses = ["run", "die", "fall", "hurt", "idle", "jump", "stand"]
names = ['adventurer', 'skeleton']
buttons = ['settings', 'play', 'exit', 'newgame', 'titles']
button_statuses = ['idle', 'aim', 'pressed']
platform_images = []
mobs_images = []
button_images = []

zastavkaImg = pygame.image.load('data/backgrounds/zastavka.jpg').convert()
zastavkaImg = pygame.transform.flip(zastavkaImg, True, False)
death_img = pygame.image.load('data/backgrounds/death_2.png').convert_alpha()
win_fon = pygame.image.load('data/backgrounds/win_fon.jpg').convert()
winner = pygame.image.load('data/backgrounds/winner.png').convert_alpha()
tree = pygame.image.load('data/landshaft/tree.png').convert_alpha()
bush = pygame.image.load('data/landshaft/bush.png').convert_alpha()
earth = pygame.image.load('data/landshaft/earth.png').convert_alpha()
big_earth = pygame.image.load('data/landshaft/big_earth.png').convert_alpha()
earth_side = pygame.image.load('data/landshaft/earth_side.png').convert_alpha()
s_p_o_earth = pygame.image.load('data/landshaft/special_part_of_earth.png').convert_alpha()
broken_stone = pygame.image.load('data/landshaft/broken_stone.png').convert_alpha()
column = pygame.image.load('data/landshaft/column.png').convert_alpha()
earth_side_rev = pygame.transform.flip(earth_side, True, False)

# coords_enemies = [(180, 825, 'skeleton')]

hp_full = pygame.transform.scale(pygame.image.load('data/backgrounds/hp_full.png'), (0.54 * x_w, 0.926 * y_w)).convert_alpha()
hp_empty = pygame.transform.scale(pygame.image.load('data/backgrounds/hp_empty.png'), (0.54 * x_w, 0.926 * y_w)).convert_alpha()
# menu_title = pygame.transform.scale(pygame.image.load('data/MenuButtons/menu.png'), (300, 100))
# menu_fon = pygame.transform.scale(pygame.image.load('data/MenuButtons/menu_fon.png'), (500, 500))


# lst_window_sized_3_4 = [(320, 240), (640, 480), (1024, 768), (1152, 864), (1400, 1050), (1440, 1080), (2048, 1536)]
# lst_window_sized_16_9 = [(640, 360), (1280, 720), (1920, 1080), (2048, 1152)]
# lst_window_sized_16_10 = [(1440, 900), (1680, 1050), (1920, 1200), (2048, 1080)]

coef = 0
for j in range(len(names)):
    mobs_images.append([])
    for i in range(len(statuses)):
        mobs_images[j].append([])
        while True:
            name_picture = "-".join((names[j], statuses[i], "0" + str(coef))) + ".png"
            fullname = os.path.join('data', names[j], statuses[i], name_picture)
            coef += 1
            if not os.path.isfile(fullname):
                coef = 0
                break
            image = pygame.image.load(fullname).convert_alpha()
            mobs_images[j][i].append(image)

while True:
    fullname = os.path.join('data', 'landshaft', 'Platform_combo_') + str(coef) + '.png'
    coef += 1
    if not os.path.isfile(fullname):
        coef = 0
        break
    bckgrd = pygame.image.load(fullname).convert_alpha()
    platform_images.append(bckgrd)

for i in range(len(buttons)):
    button_images.append([])
    for j in range(len(button_statuses)):
        fullname = os.path.join('data', 'MenuButtons', buttons[i] + '_' + button_statuses[j]) + '.png'
        if os.path.isfile(fullname):
            image = pygame.image.load(fullname).convert_alpha()
            image = pygame.transform.scale(image, (2.0833 * x_w, 1.2963 * y_w))
            button_images[i].append(image)
