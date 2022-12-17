import os
import sys

import pygame
from data import lst_images, statuses, names

# from main import land_sprites

fps = 60

for filename in os.listdir('data/idle'):
    a = pygame.image.load(f'data/idle/{filename}')
    pygame.transform.scale(a, (200, 200))


class Mob(pygame.sprite.Sprite):
    def __init__(self, x, y, *groups):
        super().__init__(*groups)
        self.ticks = 0
        self.status = "idle"
        self.hp = 100
        self.coef = 0
        self.name = ""
        self.direction = True
        self.prev_status = self.status
        self.image = lst_images[0][0][0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move(self, keys):
        pass

    def attack(self):
        pass

    def update_image(self):
        self.coef += 1
        if self.coef > len(lst_images[names.index(self.name)][statuses.index(self.status)]) - 1:
            self.coef = 0
        image = lst_images[names.index(self.name)][statuses.index(self.status)][self.coef]
        if not self.direction:
            image = pygame.transform.flip(image, True, False)
        self.image = image


class Hero(Mob):
    def __init__(self, x, y, mob_sprites, land_sprites):
        super().__init__(x, y, mob_sprites, land_sprites)
        self.land_sprites = land_sprites
        self.jump_coords = self.rect.y
        self.name = 'adventurer'
        self.jumo_opportunity = True

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
        if (keys[pygame.K_UP] or keys[pygame.K_w] or keys[pygame.K_SPACE]) and self.jumo_opportunity:
            self.jump_coords = self.rect.y - 30
            self.jumo_opportunity = False
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
            self.rect.y -= 1
            self.status = "jump"
        if self.jump_coords >= self.rect.y and self.prev_status == "jump" or self.status != "jump" and len(
                pygame.sprite.spritecollide(self, self.land_sprites, False)) == 1:
            self.rect.y += 1
            self.jump_coords = self.rect.y
            self.status = "fall"
        elif self.prev_status != 'jump':
            self.jumo_opportunity = True


class Enemies(Mob):
    def move(self, direction):
        if direction == 'right':  # условие для остановки будет отслеживаться в main
            self.x += 10
        if direction == 'left':
            self.x -= 10
