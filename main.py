import sys
import pygame
import os

import data
import mobs
import world
from world import *
from data import *

pygame.init()

pygame.mixer.music.load("C418_-_Haggstrom_30921643.mp3")
pygame.mixer.music.play(-1)

window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
mob_sprites = pygame.sprite.Group()
land_sprites = pygame.sprite.Group()

clock = pygame.time.Clock()

x_w, y_w = window.get_size()
x_w = x_w / 20
y_w = y_w / 20
begining = True

hero = mobs.Hero(x_w * 0, y_w * 19, 'adventurer', mob_sprites, land_sprites)

coords_platform = [(x_w * 0, y_w * 19, 0), (x_w * 1, y_w * 19, 0), (x_w * 2, y_w * 19, 0),
                   (x_w * 3, y_w * 19, 0), (x_w * 4, y_w * 19, 0), (x_w * 5, y_w * 19, 0),
                   (x_w * 6, y_w * 19, 0), (x_w * 7, y_w * 19, 0), (x_w * 8, y_w * 19, 0),
                   (x_w * 7, y_w * 19, 0), (x_w * 8, y_w * 19, 0), (x_w * 9, y_w * 19, 0),
                   (x_w * 8, y_w * 19, 0), (x_w * 9, y_w * 19, 0), (x_w * 10, y_w * 19, 0),
                   (x_w * 11, y_w * 19, 0), (x_w * 12, y_w * 19, 0), (x_w * 13, y_w * 19, 0),
                   (x_w * 14, y_w * 19, 0), (x_w * 15, y_w * 19, 0), (x_w * 16, y_w * 19, 0),
                   (x_w * 17, y_w * 19, 0), (x_w * 18, y_w * 19, 0), (x_w * 19, y_w * 19, 0),
                   (x_w * 14, y_w * 5, 0), (x_w * 3, y_w * 15, 0)]

coords_enemies = [(x_w * 14, y_w * 5, 'skeleton')]

for i in coords_platform:
    pos = (i[0], i[1])
    image = i[2]
    image = data.platform_images[image]
    image = pygame.transform.scale(image, (360, 66))
    world.Platform(pos, image, land_sprites)

for i in coords_enemies:
    pos = (i[0], i[1])
    name = i[2]
    mobs.Enemies(*pos, name, mob_sprites, land_sprites)


def zastavka():
    intro_text = ["The lat letter", "",
                  "начать игру",
                  "настройки",
                  "выйти из игры"]

    fon = pygame.transform.scale(zastavkaImg, window.get_size())
    window.blit(fon, (0, 0))
    font = pygame.font.Font(None, 70)
    text_y = 50
    text_x = 70
    name_game = font.render(intro_text[0], True, pygame.Color(255, 77, 213))
    name_rect = name_game.get_rect()
    name_rect.top = text_y
    name_rect.x = 50
    text_y += name_rect.height
    window.blit(name_game, name_rect)

    font = pygame.font.Font(None, 60)
    text_center = 200
    for line in intro_text[1:]:
        string_rendered = font.render(line, True, pygame.Color(255, 77, 213))
        name_rect = string_rendered.get_rect()
        text_y += 10
        name_rect.top = text_y
        name_rect.centerx = text_center
        text_y += name_rect.height
        window.blit(string_rendered, name_rect)


fps = 60
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
            print("here")
            klickPos = event.pos
            begining = False
            print(begining)
    if begining:
        zastavka()
    else:
        window.fill((0, 0, 0))
        window.blit(bg, (0, 0))
        hero.draw_radius(window)
        land_sprites.update()
        mob_sprites.update()
        land_sprites.draw(window)
        mob_sprites.draw(window)
    pygame.display.flip()
    clock.tick(fps)
