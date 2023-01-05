import sys
import pygame
import os

import data
import mobs
import world
from world import *
from data import *
from underground import *

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
menu_bool = False

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

coords_enemies = [(x_w * 5, y_w * 19, 'skeleton')]

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


def settings():
    Height, Width = 500, 500
    pos = window.get_size()[0] // 2 - Width // 2, window.get_size()[1] // 2 - Height // 2
    #pygame.draw.rect(window, "darkGray", (*pos, 500, 500))


def menu():
    global menu
    lst_txts = []
    Height, Width = 250, 250
    pos = window.get_size()[0] // 2, window.get_size()[1] // 2
    #pygame.draw.rect(window, "darkGray", (pos[0] - Width // 2, pos[1] - Height // 2, 500, 500))
    font = pygame.font.Font(None, 70)
    title = world.TxT("Меню", font, (255, 77, 213), pos[0], 70)
    lst_txts.append(title)
    font = pygame.font.Font(None, 60)
    text_y = pos[1] - Height // 2
    resume = world.TxT("продолжить игру", font, (255, 77, 213), pos[0], text_y)
    lst_txts.append(resume)
    new_game = world.TxT("новая игра", font, (255, 77, 213), pos[0], text_y + 50)
    lst_txts.append(new_game)
    settings_txt = world.TxT("настройки", font, (255, 77, 213), pos[0], text_y + 100)
    lst_txts.append(settings_txt)
    quit = world.TxT("выйти из игры", font, (255, 77, 213), pos[0], text_y + 150)
    lst_txts.append(quit)
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
        klickPos = event.pos
        if resume[1].collidepoint(klickPos):
            menu = False
        if quit[1].collidepoint(klickPos):
            pygame.quit()
            sys.exit()
        if new_game[1].collidepoint(klickPos):
            pass
        if settings_txt[1].collidepoint(klickPos):
            settings()


def zastavka():
    global begining
    intro_text = ["The lat letter", "",
                  "начать игру",
                  "настройки",
                  "выйти из игры"]
    lst_txts = []
    fon = pygame.transform.scale(zastavkaImg, window.get_size())
    window.blit(fon, (0, 0))
    font = pygame.font.Font(None, 70)
    title = world.TxT("The lat letter", font, (255, 77, 213), 200, 70)
    lst_txts.append(title)
    font = pygame.font.Font(None, 60)
    start = world.TxT("начать игру", font, (255, 77, 213), 200, 150)
    lst_txts.append(start)
    settings = world.TxT("настройки", font, (255, 77, 213), 200, 200)
    lst_txts.append(settings)
    quit = world.TxT("выйти из игры", font, (255, 77, 213), 200, 250)
    lst_txts.append(quit)
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
        klickPos = event.pos
        if start[1].collidepoint(klickPos):
            begining = False
        if quit[1].collidepoint(klickPos):
            pygame.quit()
            sys.exit()
        if settings[1].collidepoint(klickPos):
            pass
    # text_center = 200
    # for line in intro_text[1:]:
    #    string_rendered = font.render(line, True, pygame.Color(255, 77, 213))
    #    name_rect = string_rendered.get_rect()
    #    text_y += 10
    #    name_rect.top = text_y
    #    name_rect.centerx = text_center
    #    text_y += name_rect.height
    #    window.blit(string_rendered, name_rect)
    #    if klickPos and
    for i in lst_txts:
        window.blit(*i)


fps = 60
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and not begining:
            menu = True
    if begining:
        zastavka()
    else:
        window.fill((0, 0, 0))
        window.blit(bg, (0, 0))
        Letters.draw_letters()
        land_sprites.update()
        mob_sprites.update()
        land_sprites.draw(window)
        mob_sprites.draw(window)
    if menu_bool:
        menu()
    settings()
    pygame.display.flip()
    clock.tick(fps)
