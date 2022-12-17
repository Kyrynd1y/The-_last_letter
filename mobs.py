import os
import sys

import pygame

fps = 60

for filename in os.listdir('data/idle'):
    a = pygame.image.load(f'data/idle/{filename}')
    pygame.transform.scale(a, (200, 200))


class Mob(pygame.sprite.Sprite):
    def __init__(self, x, y, *groups):
        super().__init__(*groups)
        self.ticks = 0
        self.x = x
        self.y = y
        self.status = "idle"
        self.hp = 100
        self.coef = 0
        self.name = ""
        self.direction = True
        self.prev_status = self.status
        self.load_image("adventurer-idle-00.png")

    def move(self, keys):
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
        if not self.direction:
            image = pygame.transform.flip(image, True, False)
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
        self.jump_coords = self.rect.y
        self.name = 'adventurer'

    def update(self) -> None:
        keys = pygame.key.get_pressed()
        self.move(keys)
        if self.status != self.prev_status:
            self.ticks = 0
            self.prev_status = self.status
        if self.ticks / fps >= 0.2 or self.ticks / fps == 0:
            self.update_image()
            self.ticks = 0
        self.ticks += 1

    def move(self, keys):
        if keys[pygame.K_UP] or keys[pygame.K_w] or keys[pygame.K_SPACE]:
            self.jump_coords = self.rect.y - 30
            self.status = "jump"
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= 1
            self.direction = False
            self.status = "run"
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            pass
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += 1
            self.direction = True
            self.status = "run"
        else:
            self.status = "idle"
        if self.jump_coords < self.rect.y:
            self.rect.y -= 2
            self.status = "jump"
        if self.jump_coords >= self.rect.y or self.prev_status == "fall":
            pass


class Enemies(Mob):
    def move(self, direction):
        if direction == 'right':  # условие для остановки будет отслеживаться в main
            self.x += 10
        if direction == 'left':
            self.x -= 10
