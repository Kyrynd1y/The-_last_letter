import os

import pygame

statuses = ["run", "die", "fall", "hurt", "idle", "jump", "stand"]
names = ['adventurer', 'skeleton']
platform_images = []
mobs_images = []
zastavkaImg = pygame.image.load('data/zastavka.jpg')
zastavkaImg = pygame.transform.flip(zastavkaImg, True, False)
coords_enemies = [(180, 825, 'skeleton')]

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
