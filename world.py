import pygame

import mobs
from mobs import *

background = pygame.image.load('data/landshaft/BG1.png')
background = pygame.transform.scale(background, (1920, 1080))

background2 = pygame.image.load('data/landshaft/BG2.png')
background2 = pygame.transform.scale(background2, (1920, 1080))

background3 = pygame.image.load('data/landshaft/BG3.png')
background3 = pygame.transform.scale(background3, (1920, 1080))

bg = pygame.Surface((1920, 1080))

bg.blit(background, (0, 0))
bg.blit(background2, (0, 0))
bg.blit(background3, (0, 0))

platform = pygame.image.load('data/landshaft/Platform_combo_1.png')


class Platform(pygame.sprite.Sprite):
    def __init__(self, pos, image, land_sprites, *args):
        super().__init__(land_sprites)
        self.image = image
        if args:
            print(args[0])
            self.image = pygame.transform.scale(self.image, args[0])
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.image = pygame.image.load('data/landshaft/Platform_combo_1.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = x, y
