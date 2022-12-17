import os

import pygame

statuses = ["die", "fall", "hurt", "idle", "jump", "run", "stand"]
names = ['adventurer']
lst_images = []
coef = 0
for j in range(len(names)):
    lst_images.append([])
    for i in range(len(statuses)):
        lst_images[j].append([])
        while True:
            name_picture = "-".join((names[j], statuses[i], "0" + str(coef))) + ".png"
            fullname = os.path.join('data', statuses[i], name_picture)
            coef += 1
            if not os.path.isfile(fullname):
                coef = 0
                break
            image = pygame.image.load(fullname)
            lst_images[j][i].append(image)
print(lst_images)
