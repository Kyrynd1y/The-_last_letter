import pygame

import mobs
from mobs import *

background = pygame.image.load('data/landshaft/BG1.png')
background = pygame.transform.scale(background, (1920, 1080))

platform = pygame.image.load('data/landshaft/Platform_combo_1.png')


class World:
    def __init__(self):
        self.hero = mobs.Hero(100, 100)

    def render(self):
        all_sprites = pygame.sprite.Group()
        hero = self.hero(all_sprites)
        all_sprites.update()

