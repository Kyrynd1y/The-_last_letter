import os

import pygame

statuses = ["run", "die", "fall", "hurt", "idle", "jump", "stand"]
names = ['adventurer', 'skeleton']
platform_images = []
mobs_images = []

coords_platform = [(0, 825, 0), (180, 825, 0), (360, 825, 0), (540, 825, 0), (720, 825, 0),
                   (1080, 825, 0), (360, 645, 0), (720, 465, 0),
                   (1080, 465, 0), (1260, 465, 0), (1440, 465, 0)]

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
