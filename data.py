import os

import pygame

statuses = ["run", "die", "fall", "hurt", "idle", "jump", "stand"]
names = ['adventurer', 'skeleton']
buttons = ['settings', 'play', 'exit', 'newgame', 'titles']
button_statuses = ['idle', 'aim', 'pressed']
platform_images = []
mobs_images = []
button_images = []


zastavkaImg = pygame.image.load('data/zastavka.jpg')
zastavkaImg = pygame.transform.flip(zastavkaImg, True, False)
coords_enemies = [(180, 825, 'skeleton')]

hp_full = pygame.transform.scale(pygame.image.load('data/hp_full.png'), (52, 50))
hp_empty = pygame.transform.scale(pygame.image.load('data/hp_empty.png'), (52, 50))

lst_window_sized_3_4 = [(320, 240), (640, 480), (1024, 768), (1152, 864), (1400, 1050), (1440, 1080), (2048, 1536)]
lst_window_sized_16_9 = [(640, 360), (1280, 720), (1920, 1080), (2048, 1152)]
lst_window_sized_16_10 = [(1440, 900), (1680, 1050), (1920, 1200), (2048, 1080)]

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
            image = pygame.image.load(fullname)
            mobs_images[j][i].append(image)

while True:
    coef += 1
    fullname = os.path.join('data', 'landshaft', 'Platform_combo_') + str(coef) + '.png'
    if not os.path.isfile(fullname):
        coef = 0
        break
    bckgrd = pygame.image.load(fullname)
    platform_images.append(bckgrd)


for i in range(len(buttons)):
    button_images.append([])
    for j in range(len(button_statuses)):
        fullname = os.path.join('data', 'MenuButtons', buttons[i] + '_' + button_statuses[j]) + '.png'
        if os.path.isfile(fullname):
            image = pygame.image.load(fullname)
            image = pygame.transform.scale(image, (200, 70))
            button_images[i].append(image)

