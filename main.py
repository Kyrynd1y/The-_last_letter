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
    if additional.begining:
        additional.zastavka()
    elif additional.menu_bool:
        additional.menu()
    elif not additional.settings_bool:
        hero.draw_radius(window)
        mob.draw_radius(window)
        land_sprites.update()
        mob_sprites.update()
    if additional.settings_bool:
        additional.settings()
    pygame.display.flip()
    clock.tick(fps)
