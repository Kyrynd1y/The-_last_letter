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
pygame.mixer.music.set_volume(0)

window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
mob_sprites = pygame.sprite.Group()
land_sprites = pygame.sprite.Group()
land_sprites_2_vozvrashenie = pygame.sprite.Group()
letter_group = pygame.sprite.Group()

letter = Letters()
under = Underground()

clock = pygame.time.Clock()

x_w, y_w = window.get_size()
x_w = x_w / 20
y_w = y_w / 20

begining = True
menu_bool = False
settings_bool = False

hero = mobs.Hero(x_w * 0, y_w * 19, 'adventurer', mob_sprites, land_sprites, under.fight)

coords_platform = [(x_w * 0, y_w * 19, 0), (x_w * 3, y_w * 19, 0), (x_w * 6, y_w * 19, 0), (x_w * 9, y_w * 19, 0),
                   (x_w * 12, y_w * 19, 0), (x_w * 15, y_w * 19, 0), (x_w * 18, y_w * 19, 0),
                   (x_w * 19, y_w * 19, 0),
                   (x_w * 14, y_w * 5, 0), (x_w * 3, y_w * 15, 0)]

coords_platform_2 = [(x_w * 3, y_w * 15, 0), (x_w * 12, y_w * 15, 0)]

coords_enemies = [(x_w * 5, y_w * 19, 'skeleton')]


for i in coords_platform:
    pos = (i[0], i[1])
    image = i[2]
    image = data.platform_images[image]
    image = pygame.transform.scale(image, (360, 66))
    world.Platform(pos, image, land_sprites)

for i in coords_platform_2:
    pos = (i[0], i[1])
    image = i[2]
    image = data.platform_images[image]
    image = pygame.transform.scale(image, (360, 66))
    world.Platform(pos, image, land_sprites_2_vozvrashenie)

for i in coords_enemies:
    pos = (i[0], i[1])
    name = i[2]
    mob = mobs.Enemies(*pos, name, mob_sprites, land_sprites)


def settings():
    global settings_bool, menu_bool
    Height, Width = 700, 500
    lst_txts = []
    text_color = 'Blue'
    pos = window.get_size()[0] // 2 - Width // 2, window.get_size()[1] // 2 - Height // 2
    rect = pygame.draw.rect(window, "yellow", (*pos, Width, Height))
    font = pygame.font.Font(None, 60)
    text_y = rect.y + 40
    text_x = rect.x + 250
    count_y = rect.height // 5

    title = world.TxT("НАСТРОЙКИ", font, text_color, text_x, text_y)
    lst_txts.append(title)

    volume = world.TxT("громкость", font, text_color, text_x, text_y + count_y)
    lst_txts.append(volume)

    window_size = world.TxT("размер окна", font, text_color, text_x, text_y + count_y * 2)
    lst_txts.append(window_size)

    cancel = world.TxT("отменить", font, text_color, text_x, text_y + count_y * 3)
    lst_txts.append(cancel)

    save_changes = world.TxT("сохранить", font, text_color, text_x, text_y + count_y * 4)
    lst_txts.append(save_changes)

    if event.type == pygame.MOUSEBUTTONUP and event.button == pygame.BUTTON_LEFT:
        klickPos = event.pos
        if volume[1].collidepoint(klickPos):
            pass
        if window_size[1].collidepoint(klickPos):
            pass
        if cancel[1].collidepoint(klickPos):
            settings_bool = False
            menu_bool = True
        if save_changes[1].collidepoint(klickPos):
            settings_bool = False
            menu_bool = True
    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and not begining:
        settings_bool = not settings_bool
    for i in lst_txts:
        window.blit(*i)


def menu():
    global menu_bool, settings_bool
    lst_txts = []
    Height, Width = 500, 500
    pos = window.get_size()[0] // 2 - Width // 2, window.get_size()[1] // 2 - Height // 2
    rect = pygame.draw.rect(window, "darkGray", (*pos, Width, Height))
    font = pygame.font.Font(None, 60)
    text_y = rect.y + 40
    text_x = rect.x + 250
    count_y = rect.height // 5
    title = world.TxT("МЕНЮ", font, (255, 77, 213), text_x, text_y)
    lst_txts.append(title)
    resume = world.TxT("продолжить", font, (255, 77, 213), text_x, text_y + count_y)
    lst_txts.append(resume)
    new_game = world.TxT("новая игра", font, (255, 77, 213), text_x, text_y + count_y * 2)
    lst_txts.append(new_game)
    settings_txt = world.TxT("настройки", font, (255, 77, 213), text_x, text_y + count_y * 3)
    lst_txts.append(settings_txt)
    quit = world.TxT("выйти из игры", font, (255, 77, 213), text_x, text_y + count_y * 4)
    lst_txts.append(quit)
    if event.type == pygame.MOUSEBUTTONUP and event.button == pygame.BUTTON_LEFT:
        klickPos = event.pos
        if resume[1].collidepoint(klickPos):
            menu_bool = False
        if quit[1].collidepoint(klickPos):
            pygame.quit()
            sys.exit()
        if new_game[1].collidepoint(klickPos):
            pass
        if settings_txt[1].collidepoint(klickPos):
            settings_bool = True
            menu_bool = False
    for i in lst_txts:
        window.blit(*i)


def zastavka():
    global begining, settings_bool, menu_bool
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
    settings_txt = world.TxT("настройки", font, (255, 77, 213), 200, 200)
    lst_txts.append(settings_txt)
    quit = world.TxT("выйти из игры", font, (255, 77, 213), 200, 250)
    lst_txts.append(quit)
    if event.type == pygame.MOUSEBUTTONUP and event.button == pygame.BUTTON_LEFT:
        klickPos = event.pos
        if start[1].collidepoint(klickPos):
            begining = False
            settings_bool = False
            menu_bool = False
        if quit[1].collidepoint(klickPos):
            pygame.quit()
            sys.exit()
        if settings_txt[1].collidepoint(klickPos):
            settings_bool = True
    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        settings_bool = False
    for i in lst_txts:
        window.blit(*i)


fps = 60
letter.random_letters()

cfg = 3

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and not begining:
            menu_bool = not menu_bool
        if (hero.hero_x - mob.mob_x) ** 2 + (hero.hero_y - mob.mob_y) ** 2 <= (hero.radius + mob.radius) ** 2 \
                and event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            under.fight = True
            hero.attack()
            mob.attack()
            mob.correct_pos(x_w * 13.5, y_w * 15)
            hero.correct_pos(x_w * 4.5, y_w * 15)
    window.fill((0, 0, 0))
    if under.fight:
        window.blit(bg_under, (0, 0))
        while letter.letters:
            for a in letter.letters:
                temp = pygame.image.load(f'data/R_Letters/Letter_{a}.png')
                temp2 = pygame.transform.scale(temp, (60, 60))
                ltr = Letter(a, temp2, letter_group)
                ltr.rect.topleft = x_w * cfg, y_w
                cfg += 1
                letter.letters.remove(a)
        letter_group.draw(window)
        land_sprites_2_vozvrashenie.draw(window)
    else:
        window.blit(bg, (0, 0))
        land_sprites.draw(window)
    mob_sprites.draw(window)
    if begining:
        zastavka()
    elif menu_bool:
        menu()
    elif not settings_bool:
        hero.draw_radius(window)
        mob.draw_radius(window)
        land_sprites.update()
        mob_sprites.update()
    if settings_bool:
        settings()
    pygame.display.flip()
    clock.tick(fps)

#
