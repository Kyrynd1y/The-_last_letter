import inspect

import data
import mobs
from world import *
from underground import *
import additional

window = additional.window

pygame.init()

pygame.mixer.music.load("C418_-_Haggstrom_30921643.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0)

land_sprites = additional.land_sprites
mob_sprites = additional.mob_sprites
land_sprites_2_vozvrashenie = pygame.sprite.Group()
letter_group = pygame.sprite.Group()

hero = additional.hero
enemies = additional.enemies
under = additional.under

letter = Letters()

clock = pygame.time.Clock()

x_w, y_w = additional.x_w, additional.y_w

coords_platform = [(x_w * 0, y_w * 19, 0), (x_w * 3, y_w * 19, 0), (x_w * 6, y_w * 19, 0), (x_w * 9, y_w * 19, 0),
                   (x_w * 12, y_w * 19, 0), (x_w * 15, y_w * 19, 0), (x_w * 18, y_w * 19, 0),
                   (x_w * 19, y_w * 19, 0),
                   (x_w * 14, y_w * 5, 0), (x_w * 3, y_w * 15, 0)]

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
letter.random_letters()

cfg = 3

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
                under.fight = True
                hero.is_fight = True
                mob.is_fight = False
                mob.correct_pos(x_w * 13.5, y_w * 15)
                hero.correct_pos(x_w * 4.5, y_w * 15)
    window.fill((0, 0, 0))
    land_sprites.update()
    mob_sprites.update()
    additional.button_sprites.update()
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
    if additional.begining:
        additional.zastavka()
        additional.button_sprites.draw(window)
    elif additional.menu_bool:
        additional.menu()
        additional.button_sprites.draw(window)
    elif not additional.settings_bool:
        hero.draw_radius(window)
        for mob in enemies:
            mob.draw_radius(window)
    if additional.settings_bool:
        additional.settings()
    pygame.display.flip()
    clock.tick(fps)
