import inspect

import pygame as pygame

import data
import mobs
import underground
import world
from world import *
from underground import *
import additional

window = additional.window

selectef_word = ''
fight_mob = None

pygame.mixer.music.load("data/music/C418_-_Haggstrom_30921643.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(additional.settings.value_volume / 100 / 2)

land_sprites = additional.land_sprites
decor_sprites = additional.decor_sprites
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

coords_platform = [(x_w * 0, y_w * 19, 0), (x_w * 1, y_w * 19, 0), (x_w * 2, y_w * 19, 0), (x_w * 3, y_w * 19, 0),
                   (x_w * 4, y_w * 19, 0), (x_w * 5, y_w * 19, 0), (x_w * 6, y_w * 19, 0), (x_w * 7.5, y_w * 15, 0),
                   (x_w * 8.5, y_w * 15, 0), (x_w * 9.5, y_w * 15, 0), (x_w * 10.5, y_w * 15, 0),
                   (x_w * 11.5, y_w * 15, 0), (x_w * 12.5, y_w * 15, 0), (x_w * 13.5, y_w * 15, 0),
                   (x_w * 14.5, y_w * 15, 0), (x_w * 15.5, y_w * 15, 0), (x_w * 16.5, y_w * 15, 0),
                   (x_w * 17.5, y_w * 15, 0), (x_w * 18.5, y_w * 15, 0), (x_w * 19.5, y_w * 15, 0),
                   (x_w * 6, y_w * 17, 0),
#21
                   (x_w * 0, y_w * 9, 0), (x_w * 1, y_w * 9, 0), (x_w * 2, y_w * 9, 0), (x_w * 3, y_w * 11, 0),
                   (x_w * 4, y_w * 13, 0),

                   (x_w * 13, y_w * 9, 0), (x_w * 14, y_w * 9, 0), (x_w * 9, y_w * 6.5, 0),

                   (x_w * 21, y_w * 12.5, 0), (x_w * 19, y_w * 9, 0), (x_w * 22.5, y_w * 6, 0),
                   (x_w * 23.5, y_w * 6, 0), (x_w * 24.5, y_w * 6, 0), (x_w * 25.5, y_w * 6, 0),
#35
                   (x_w * 31, y_w * 15, 0), (x_w * 27, y_w * 16, 0), (x_w * 28, y_w * 16, 0), (x_w * 29, y_w * 16, 0),
                   (x_w * 30, y_w * 16, 0), (x_w * 31, y_w * 16, 0), (x_w * 32, y_w * 16, 0),
                   (x_w * 33, y_w * 16, 0), (x_w * 35, y_w * 16, 0), (x_w * 36, y_w * 16, 0),
                   (x_w * 37, y_w * 16, 0), (x_w * 38, y_w * 16, 0), (x_w * 39, y_w * 16, 0),
                   (x_w * 40, y_w * 16, 0), (x_w * 41, y_w * 16, 0), (x_w * 42, y_w * 16, 0),

                   (x_w * 29, y_w * 9, 0), (x_w * 33, y_w * 12.7, 0), (x_w * 36, y_w * 9.5, 0),
                   (x_w * 38.5, y_w * 12, 0), (x_w * 42, y_w * 8.3, 0), (x_w * 39, y_w * 5, 0),
                   (x_w * 38, y_w * 5, 0), (x_w * 37, y_w * 5, 0), (x_w * 36, y_w * 5, 0),
                   (x_w * 35, y_w * 5, 0), (x_w * 34, y_w * 5, 0), (x_w * 33, y_w * 5, 0),

                   (x_w * 34, y_w * 16, 0), (x_w * 9, y_w * 11.5, 0)]

coords_earth_sides = [(x_w * 6.2, y_w * 17), (x_w * 7.7, y_w * 17), (x_w * 7.7, y_w * 15), (x_w * 7.7, y_w * 19),
                      (x_w * 21.2, y_w * 13), (x_w * 22.7, y_w * 10.5), (x_w * 22.7, y_w * 8.5),
                      (x_w * 22.7, y_w * 6.5)]

coords_earth_sides_rev = [(x_w * 26.8, y_w * 6.5), (x_w * 26.8, y_w * 8.5), (x_w * 26.8, y_w * 10.5),
                          (x_w * 26.8, y_w * 12.5), (x_w * 26.8, y_w * 14.5)]

coords_earth = [(x_w * 6.5, y_w * 17)]

coords_platform_2 = [(x_w * 3, y_w * 15, 1), (x_w * 12, y_w * 15, 1)]

coords_trees = [(x_w * 3, y_w * 11.6), (x_w * 17, y_w * 7.6), (x_w * 31, y_w * 7.6), (x_w * 23, y_w * -1.4)]

coords_bushes = [(x_w * 5, y_w * 17.9), (x_w * 2, y_w * 8), (x_w * 3, y_w * 8.4), (x_w * 10, y_w * 14),
                 (x_w * 16.5, y_w * 14), (x_w * 14.5, y_w * 14), (x_w * 30, y_w * 15), (x_w * 33, y_w * 15),
                 (x_w * 32.7, y_w * 14.9), (x_w * 34, y_w * 3.9), (x_w * 37, y_w * 3.9)]

coords_broken_stones = [(x_w * 2.6, y_w * 8), (x_w * 17, y_w * 14), (x_w * 31.2, y_w * 14), (x_w * 35, y_w * 4),
                        (x_w * 39.4, y_w * 11)]

coords_big_earth = [(x_w * 7.8, y_w * 16), (x_w * 15, y_w * 16), (x_w * 22, y_w * 16), (x_w * 29, y_w * 16),
                    (x_w * 36.2, y_w * 16)]

coords_column = [(x_w * 15, y_w * 10)]

landscape = []

coords_landscape = coords_column + coords_broken_stones + coords_big_earth + coords_earth + coords_earth_sides + \
                coords_earth_sides_rev + coords_trees + coords_bushes + [(x_w * 21, y_w * 7.15)] + coords_platform

for i in coords_column:
    pos = (i[0], i[1])
    image = data.column
    image = pygame.transform.scale(image, (150, 300))
    landscape.append(world.Decoration(pos, image, decor_sprites))

for i in coords_broken_stones:
    pos = (i[0], i[1])
    image = data.broken_stone
    image = pygame.transform.scale(image, (65, 55))
    landscape.append(world.Decoration(pos, image, decor_sprites))

for i in coords_big_earth:
    pos = (i[0], i[1])
    image = data.big_earth
    image = pygame.transform.scale(image, (697, 240))
    landscape.append(world.Platform(pos, image, land_sprites))

for i in coords_earth:
    pos = (i[0], i[1])
    image = data.earth
    image = pygame.transform.scale(image, (120, 120))
    landscape.append(world.Platform(pos, image, land_sprites))

for i in coords_earth_sides:
    pos = (i[0], i[1])
    image = data.earth_side
    image = pygame.transform.scale(image, (40, 120))
    landscape.append(world.Platform(pos, image, land_sprites))

for i in coords_earth_sides_rev:
    pos = (i[0], i[1])
    image = data.earth_side_rev
    image = pygame.transform.scale(image, (40, 120))
    landscape.append(world.Platform(pos, image, land_sprites))

for i in coords_trees:
    pos = (i[0], i[1])
    image = data.tree
    image = pygame.transform.scale(image, (230, 400))
    landscape.append(world.Decoration(pos, image, decor_sprites))

for i in coords_bushes:
    pos = (i[0], i[1])
    image = data.bush
    image = pygame.transform.scale(image, (90, 60))
    landscape.append(world.Decoration(pos, image, decor_sprites))

for i in coords_platform_2:
    pos = (i[0], i[1])
    image = i[2]
    image = data.platform_images[image]
    image = pygame.transform.scale(image, (360, 66))
    world.Platform(pos, image, land_sprites_2_vozvrashenie)

image = data.s_p_o_earth
image = pygame.transform.scale(image, (570, 480))
landscape.append(world.Platform((x_w * 21, y_w * 7.15), image, decor_sprites))

for i in coords_platform:
    pos = (i[0], i[1])
    image = i[2]
    image = data.platform_images[image]
    image = pygame.transform.scale(image, (180, 66))
    landscape.append(world.Platform(pos, image, land_sprites))

fps = 60

counter, text = 10, '10'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 100)
timesup = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and not additional.begining:
            additional.menu_bool = not additional.menu_bool
        if event.type == pygame.USEREVENT and under.fight:
            counter -= 1
            text = str(counter).rjust(3) if counter > 0 else "Time's up"
            if text == "Time's up":
                timesup = True
            print(timesup)
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
                fight_mob.add(fight_mobs_sprites)
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
        if pygame.mouse.get_pressed()[0] or timesup:
            press_coord = pygame.mouse.get_pos()
            if play_selected.rect.collidepoint(press_coord) or timesup:
                underground.ltrs.sort()

                for ltr in underground.ltrs:
                    if ltr.selected:
                        selectef_word += ltr.letter

                counter, text = 10, '10'.rjust(3)
                pygame.time.set_timer(pygame.USEREVENT, 1000)
                font = pygame.font.SysFont('comicsans', 100)
                timesup = False

                hero.is_fight = False
                hero.rect.bottomleft = hero.bottomleft
                hero.remove(fight_mobs_sprites)
                under.fight = False
                fight_mob.rect.bottomleft = fight_mob.bottomleft
                fight_mob.is_fight = False
                fight_mob.remove(fight_mobs_sprites)
                for i in underground.ltrs:
                    i.kill()
                underground.ltrs = []
                with open('data/singular_and_plural.txt', encoding='utf8') as f:
                    lines = [line.rstrip('\n') for line in f]
                    for word in lines:
                        if selectef_word == ''.join(word):
                            selectef_word = ''
                            fight_mob.live = False
                            fight_mob.kill()
                            break
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
        fight_mobs_sprites.draw(window)
        land_sprites_2_vozvrashenie.draw(window)
        # text_rect = text.get_rect(center=(x_w * 10, 300))
        window.blit(font.render(text, True, 'red'), (x_w * 10, 300))
    else:
        window.blit(bg, (0, 0))
        decor_sprites.draw(window)
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
        decor_sprites.update()
        mob_sprites.update()
        if hero.rect.x != x_w * 10 and landscape[-2].rect.left > hero.rect.center[0] > landscape[-1].rect.right \
                and not under.fight:
            difference = hero.rect.x - x_w * 10
            for obj in landscape:
                print(obj.rect.center, difference)
                obj.rect.x -= difference
            for mob in enemies:
                mob.rect.x -= difference
            hero.rect.x = x_w * 10
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
                for i in range(len(landscape)):
                    land = landscape[i]
                    coord = coords_landscape[i]
                    land.rect.x, land.rect.y = coord[0], coord[1]
                additional.new_game_func()

        additional.play_butt.kill()
        additional.titles_butt.kill()
        additional.settings_butt.kill()

        additional.button_sprites.draw(window)
    if len(mob_sprites) == 1:
        pass
    pygame.display.flip()
    clock.tick(fps)
