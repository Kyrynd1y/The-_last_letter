import os
import sys

import pygame


class Mob(pygame.sprite.Sprite):
    def __init__(self, x, y, *groups):
        super().__init__(*groups)
        self.x = x
        self.y = y
        self.status = "idle"
        self.hp = 100
        self.coef = 0
        self.load_image("adventurer-stand-0.png")
        self.name = "mob"

    def move(self, direction):
        pass

    def attack(self):
        pass

    def load_image(self, name_picture):
        fullname = os.path.join('data', self.status, name_picture)
        print(fullname)
        if not os.path.isfile(fullname):
            self.coef = 0
            self.update_image()
        image = pygame.image.load(fullname)
        image = image.convert_alpha()
        self.image = image

    def update_image(self):
        name_picture = "-".join((self.name, self.status, str(self.coef)))
        self.coef += 1
        self.load_image(name_picture)


class Hero(Mob):
    def __init__(self, x, y, *groups):
        super().__init__(x, y, *groups)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.name = 'adventurer'

    def update(self) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= 10
            self.status = "run"
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= 10
            self.status = "run"
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += 10
            self.status = "run"
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += 10
            self.status = "run"
        else:
            self.status = "idle"
        self.update_image()


class Enemies(Mob):
    def move(self, direction):
        if direction == 'right':  # условие для остановки будет отслеживаться в main
            self.x += 10
        if direction == 'left':
            self.x -= 10
