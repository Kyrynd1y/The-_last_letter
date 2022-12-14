import pygame

import mobs
from mobs import *


class World:
    def __init__(self):
        self.hero = mobs.Hero(100, 100)

    def render(self):
        all_sprites = pygame.sprite.Group()
        hero = self.hero(all_sprites)
        all_sprites.update()
