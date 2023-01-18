import inspect

import pygame as pygame

import data
import mobs
import underground
from world import *
from underground import *
import additional

window = additional.window

selectef_word = ''
fight_mob = None

pygame.mixer.music.load("C418_-_Haggstrom_30921643.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(additional.settings.value_volume / 100 / 2)

land_sprites = additional.land_sprites
mob_sprites = additional.mob_sprites
fight_mobs_sprites = pygame.sprite.Group()
land_sprites_2_vozvrashenie = pygame.sprite.Group()

hero = additional.hero
enemies = additional.enemies
under = additional.under

letter = Letters()

clock = pygame.time.Clock()

x_w, y_w = additional.x_w, additional.y_w

play_selected = world.Button(x_w * 9 + 50, y_w * 12, 'play', underground.letter_group)

coords_platform = [(x_w * 0, y_w * 19, 0), (x_w * 3, y_w * 19, 0), (x_w * 6, y_w * 19, 0), (x_w * 9, y_w * 19, 0),
                   (x_w * 12, y_w * 19, 0), (x_w * 15, y_w * 19, 0), (x_w * 18, y_w * 19, 0),
                   (x_w * 14, y_w * 5, 0), (x_w * 3, y_w * 15, 0), (x_w * 9, y_w * 11, 0)]

coords_platform_2 = [(x_w * 3, y_w * 15, 0), (x_w * 12, y_w * 15, 0)]

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

fps = 60

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and not additional.begining:
            additional.menu_bool = not additional.menu_bool
        for mob in enemies:
            if (hero.rect.x - mob.rect.x) ** 2 + (hero.rect.y - mob.rect.y) ** 2 <= (hero.radius + mob.radius) ** 2 \
                    and event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                fight_mob = mob
                under.fight = True
                hero.is_fight = True
                mob.is_fight = True
                mob.correct_pos(x_w * 13.5, y_w * 15)
                mob.direction = False
                hero.correct_pos(x_w * 4.5, y_w * 15)
                hero.status = 'idle'
                hero.direction = True
                mob.add(fight_mobs_sprites)
                hero.add(fight_mobs_sprites)
                break

        if additional.settings_bool:
            additional.manager.process_events(event)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                additional.settings_bool = False
            additional.settings_bool = additional.settings.update(event, additional.settings_bool)
    window.fill((0, 0, 0))
    additional.button_sprites.update()

    if under.fight:
        window.blit(bg_under, (0, 0))
        if not underground.ltrs:
            letter.random_letters()
            underground.creating_letters(letter.letters, x_w, y_w)
        coef_selected_pos = 5
        if pygame.mouse.get_pressed()[0]:
            press_coord = pygame.mouse.get_pos()
            if play_selected.rect.collidepoint(press_coord):
                for ltr in underground.ltrs:
                    if ltr.selected:
                        selectef_word += ltr.letter
                hero.is_fight = False
                hero.rect.bottomleft = hero.bottomleft
                under.fight = False
                fight_mob.rect.bottomleft = fight_mob.bottomleft
                fight_mob.is_fight = False
                for i in underground.ltrs:
                    i.kill()
                underground.ltrs = []
                with open('singular_and_plural.txt', encoding='utf8') as f:
                    lines = [line.rstrip('\n') for line in f]
                    for word in lines:
                        if selectef_word == ''.join(word):
                            selectef_word = ''
                            fight_mob.live = False
                            fight_mob.kill()
                    else:
                        hero.hp -= 1
            for ltr in underground.ltrs:
                if ltr.selected:
                    coef_selected_pos += 1
            for ltr in underground.ltrs:
                if ltr.rect.collidepoint(press_coord):
                    ltr.move(x_w * coef_selected_pos, y_w * 6, coef_selected_pos)
        play_selected.update()
        letter_group.draw(window)
        land_sprites_2_vozvrashenie.draw(window)
    else:
        window.blit(bg, (0, 0))
        land_sprites.draw(window)
    mob_sprites.draw(window)
    if additional.begining:
        additional.zastavka()
        additional.button_sprites.draw(window)
    elif additional.menu_bool:
        additional.menu()
        additional.button_sprites.draw(window)
    elif not additional.settings_bool:
        land_sprites.update()
        mob_sprites.update()
        hero.draw_radius(window)
        for mob in enemies:
            mob.draw_radius(window)
    if additional.settings_bool:
        additional.settings.draw()
        additional.manager.update(fps / 1000.0)
    if not additional.begining:
        for i in range(hero.hp):
            window.blit(hp_full, (x_w * i + 20, y_w))
        for i in range(3 - hero.hp):
            window.blit(hp_empty, (x_w * (hero.hp + i) + 20, y_w))
    if hero.hp == 0 or len(mob_sprites) == 1:
        if hero.hp == 0:
            death_img = pygame.transform.scale(death_img, window.get_size())
            window.blit(death_img, (0, 0))
        else:
            win_fon = pygame.transform.scale(win_fon, window.get_size())
            winner = pygame.transform.scale(winner, (400, 300))
            window.blit(win_fon, (0, 0))
            window.blit(winner, (x_w * 1, y_w * 1))
        additional.new_game_butt.add(additional.button_sprites)
        additional.new_game_butt.rect.center = (x_w * 7, y_w * 17)

        additional.exit_butt.rect.center = (x_w * 13, y_w * 17)

        if pygame.mouse.get_pressed()[0]:
            klickPos = pygame.mouse.get_pos()
            if additional.exit_butt.rect.collidepoint(klickPos):
                pygame.quit()
                sys.exit()
            if additional.new_game_butt.rect.collidepoint(klickPos):
                additional.new_game_func()

        additional.play_butt.kill()
        additional.titles_butt.kill()
        additional.settings_butt.kill()

        additional.button_sprites.draw(window)
    if len(mob_sprites) == 1:
        pass
    pygame.display.flip()
    clock.tick(fps)
