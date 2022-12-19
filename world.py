import pygame

import mobs
from mobs import *


class Platform(pygame.sprite.Sprite):
    def __init__(self, pos, image, land_sprites, *args):
        super().__init__(land_sprites)
        self.image = image
        self.rect = self.image.get_rect()
        if args:
            self.rect = args[0]
        self.rect.topleft = pos
        print(self.rect)
