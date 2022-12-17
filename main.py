import sys
import pygame
import os

import mobs
from mobs import *
from world import *

pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)

# animation_set = [pygame.image.load(f"r{i}.png") for i in range(1, 4)]

window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
all_sprites = pygame.sprite.Group()
hero = mobs.Hero(100, 100, all_sprites)
clock = pygame.time.Clock()

fps = 60
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()

    window.fill((0, 0, 0))
    window.blit(background, (0, 0))
    window.blit(platform, (100, 100))
    window.blit(platform, (150, 100))
    window.blit(platform, (200, 100))
    window.blit(platform, (50, 100))
    window.blit(platform, (0, 100))
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(fps)
