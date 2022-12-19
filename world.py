import pygame

import mobs
from mobs import *


class Platform(pygame.sprite.Sprite):
    def __init__(self, pos, image, land_sprites, *args):
        super().__init__(land_sprites)
        self.image = image
        if args:
            print(args[0])
            self.image = pygame.transform.scale(self.image, args[0])
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
