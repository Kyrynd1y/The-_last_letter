import sys
import pygame
import os

import mobs
import world
from world import *

pygame.init()

window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
mob_sprites = pygame.sprite.Group()
land_sprites = pygame.sprite.Group()

hero = mobs.Hero(100, 200, 'adventurer', mob_sprites, land_sprites)
clock = pygame.time.Clock()
land = world.Platform(100, 200, land_sprites)
land2 = world.Platform(500, 200, land_sprites)
zombie = mobs.Enemies(500, 201, 'skeleton', mob_sprites, land_sprites)


fps = 60
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()

    window.fill((0, 0, 0))
    window.blit(background, (0, 0))
    #window.blit(platform, (100, 100))
    land_sprites.update()
    mob_sprites.update()
    land_sprites.draw(window)
    mob_sprites.draw(window)
    pygame.display.flip()
    clock.tick(fps)
