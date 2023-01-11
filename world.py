import pygame

from mobs import *

background = pygame.image.load('data/landshaft/BG1.png')
background = pygame.transform.scale(background, (1920, 1080))

background2 = pygame.image.load('data/landshaft/BG2.png')
background2 = pygame.transform.scale(background2, (1920, 1080))

background3 = pygame.image.load('data/landshaft/BG3.png')
background3 = pygame.transform.scale(background3, (1920, 1080))

un_background = pygame.image.load('data/landshaft/space.png')

bg = pygame.Surface((1920, 1080))

bg.blit(background, (0, 0))
bg.blit(background2, (0, 0))
bg.blit(background3, (0, 0))


class Platform(pygame.sprite.Sprite):
    def __init__(self, pos, image, land_sprites):
        super().__init__(land_sprites)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = pos


def TxT(text, font, color, x, y):
    render = font.render(text, True, pygame.Color(color))
    rect = render.get_rect()
    rect.center = x, y
    return render, rect

#
