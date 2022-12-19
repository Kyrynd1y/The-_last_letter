import sys
import pygame
import os

import data
import mobs
import world
from world import *
from data import *

pygame.init()

window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
mob_sprites = pygame.sprite.Group()
land_sprites = pygame.sprite.Group()
data.load_images()

hero = mobs.Hero(100, 200, 'adventurer', mob_sprites, land_sprites)
clock = pygame.time.Clock()
zombie = mobs.Enemies(500, 201, 'skeleton', mob_sprites, land_sprites)
for i in data.coords_platform:
    pos = (i[0], i[1])
    image = i[2]
    world.Platform(pos, data.platform_images[image], land_sprites)
for i in data.landshaft_images:
    world.Platform((0, 0), i, land_sprites, window.get_rect())

fps = 60
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()

    window.fill((0, 0, 0))
    # window.blit(platform, (100, 100))
    land_sprites.update()
    mob_sprites.update()
    land_sprites.draw(window)
    mob_sprites.draw(window)
    pygame.display.flip()
    clock.tick(fps)
