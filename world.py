import pygame

import mobs
from mobs import *

background = pygame.image.load('data/landshaft/BG1.png')
background = pygame.transform.scale(background, (1920, 1080))

platform = pygame.image.load('data/landshaft/Platform_combo_1.png')


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, land_sprites):
        super().__init__(land_sprites)
        self.image = pygame.image.load('data/landshaft/Platform_combo_1.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = x, y




