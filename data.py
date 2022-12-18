import os

import pygame

statuses = ["run", "die", "fall", "hurt", "idle", "jump", "stand"]
names = ['adventurer', 'skeleton']
lst_images = []


def load_images():
    coef = 0
    print("here")
    for j in range(len(names)):
        lst_images.append([])
        for i in range(len(statuses)):
            lst_images[j].append([])
            while True:
                name_picture = "-".join((names[j], statuses[i], "0" + str(coef))) + ".png"
                fullname = os.path.join('data', names[j], statuses[i], name_picture)
                coef += 1
                if not os.path.isfile(fullname):
                    coef = 0
                    break
                image = pygame.image.load(fullname)
                lst_images[j][i].append(image)
