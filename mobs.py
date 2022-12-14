import os
import sys

import pygame

fps = 60


class Mob(pygame.sprite.Sprite):
    def __init__(self, x, y, *groups):
        super().__init__(*groups)
        self.ticks = 0
        self.x = x
        self.y = y
        self.status = "idle"
        self.hp = 100
        self.coef = 0
        self.load_image("adventurer-idle-00.png")
        self.name = ""

    def move(self, direction):
        pass

    def attack(self):
        pass

    def load_image(self, name_picture):
        fullname = os.path.join('data', self.status, name_picture)
        if not os.path.isfile(fullname):
            self.coef = 0
            self.update_image()
            return
        image = pygame.image.load(fullname)
        image = image.convert_alpha()
        self.image = image

    def update_image(self):
        name_picture = "-".join((self.name, self.status, "0" + str(self.coef))) + ".png"
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
            self.rect.y -= 1
            self.status = "run"
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= 1
            self.status = "run"
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += 1
            self.status = "run"
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += 1
            self.status = "run"
        else:
            self.status = "idle"
        if self.ticks / fps >= 0.2:
            self.update_image()
            self.ticks = 0
        self.ticks += 1


class Enemies(Mob):
    def move(self, direction):
        if direction == 'right':  # условие для остановки будет отслеживаться в main
            self.x += 10
        if direction == 'left':
            self.x -= 10
