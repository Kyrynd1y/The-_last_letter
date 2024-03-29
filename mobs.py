import os
import sys

import pygame
from data import mobs_images, statuses, names
from world import Platform
from underground import *

fps = 60


class Mob(pygame.sprite.Sprite):
    def __init__(self, x, y, name, mob_sprites, land_sprites):
        super().__init__(mob_sprites, land_sprites)
        self.ticks = 0
        self.status = "idle"
        self.coef = 0
        self.name = name
        self.direction = True
        self.prev_status = self.status
        self.image = mobs_images[names.index(self.name)][0][0]
        self.image = pygame.transform.scale(self.image, (1.041666 * x_w, 1.851851 * y_w))
        self.rect = self.image.get_rect()
        self.rect.bottomleft = x, y
        self.is_fight = False
        self.bottomleft = self.rect.bottomleft

    def move(self):
        pass

    def update_image(self):
        self.coef += 1
        if self.coef > len(mobs_images[names.index(self.name)][statuses.index(self.status)]) - 1:
            self.coef = 0
        image = mobs_images[names.index(self.name)][statuses.index(self.status)][self.coef]
        if not self.direction:
            image = pygame.transform.flip(image, True, False)
        self.image = pygame.transform.scale(image, (1.041666 * x_w, 1.851851 * y_w))

    def correct_pos(self, x_w, y_w):
        self.rect.bottomleft = x_w, y_w


class Hero(Mob):
    def __init__(self, x, y, name, mob_sprites, land_sprites, is_fight):
        super().__init__(x, y, name, mob_sprites, land_sprites)
        self.land_sprites = land_sprites
        self.jump_coords = self.rect.y
        self.jump_opportunity = True
        self.radius = 1.041666 * x_w
        self.hp = 3
        self.is_fight = is_fight
        self.gravity_speed = 1

    def update(self) -> None:
        keys = pygame.key.get_pressed()
        if not self.is_fight:
            self.move(keys)
            self.bottomleft = self.rect.bottomleft
        if self.status != self.prev_status:
            self.ticks = 0
            self.prev_status = self.status
        if self.ticks / fps >= 0.3 or self.ticks / fps == 0:
            self.update_image()
            self.ticks = 0
        self.ticks += 1

    def move(self, keys):
        collide_sprites = pygame.sprite.spritecollide(self, self.land_sprites, False)
        is_ground = False
        lst_platforms = []
        for i in collide_sprites:
            if i.__class__ == Platform:
                lst_platforms.append(i)
        for i in lst_platforms:
            if i.rect.top + 0.0185185 * y_w <= self.rect.bottom <= i.rect.top + 0.185185 * y_w:
                is_ground = True
                self.jump_opportunity = True
        if is_ground:
            self.status = 'idle'
        if (keys[pygame.K_UP] or keys[pygame.K_w] or keys[pygame.K_SPACE]) and self.jump_opportunity:
            self.jump_coords = self.rect.y - 3.703703 * y_w
            self.jump_opportunity = False
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            for i in lst_platforms:
                if (
                        self.rect.bottom >= i.rect.top + 0.0555555 * y_w >= self.rect.y or self.rect.bottom >= i.rect.bottom >= self.rect.y) \
                        and self.rect.x + 0.0208333 * x_w == i.rect.right:
                    break
            else:
                self.rect.x -= 0.0208333 * x_w
                self.direction = False
                self.status = "run"
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            pass
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            for i in lst_platforms:
                if (
                        self.rect.bottom >= i.rect.top + 3 >= self.rect.y or self.rect.bottom >= i.rect.bottom >= self.rect.y) \
                        and self.rect.right - 0.0208333 * x_w == i.rect.x:
                    break
            else:
                self.rect.x += 2
                self.direction = True
                self.status = "run"
        else:
            self.status = "idle"
        if self.jump_coords < self.rect.y:
            for i in lst_platforms:
                if self.rect.center[1] >= i.rect.bottom >= self.rect.y:
                    break
            else:
                self.rect.y -= 4
                self.status = "jump"
        if (self.jump_coords >= self.rect.y or self.status != "jump" or
            self.prev_status == "fall") and not is_ground:
            self.jump_opportunity = False
            self.gravity_speed += 1
            self.rect.y += 2 * self.gravity_speed // 20
            self.jump_coords = self.rect.y
            self.status = "fall"
        elif self.prev_status != 'jump':
            self.jump_opportunity = True
        if self.status != 'fall':
            for i in lst_platforms:
                if i.rect.top + 1 < self.rect.bottom <= i.rect.top + 2 * self.gravity_speed // 20:
                    self.rect.bottom = i.rect.top + 1
            self.gravity_speed = 0

    # def update_image(self):
    #     self.coef += 1
    #     if self.coef > len(mobs_images[names.index(self.name)][statuses.index(self.status)]) - 1:
    #         self.coef = 0
    #     image = mobs_images[names.index(self.name)][statuses.index(self.status)][self.coef]
    #     if not self.direction:
    #         image = pygame.transform.flip(image, True, False)
    #     self.image = pygame.transform.scale(image, (50, 80))

    def draw_radius(self, surface):
        screen = surface.convert_alpha()
        screen.fill([0, 0, 0, 0])
        pygame.draw.circle(screen, (255, 0, 0, 128), self.rect.center, 100)
        self.hero_x = self.rect[0]
        self.hero_y = self.rect[1]

    def can_move(self):
        pass


class Enemies(Mob):
    def __init__(self, x, y, name, mob_sprites, land_sprites):
        super().__init__(x, y, name, mob_sprites, land_sprites)
        self.land_sprites = land_sprites
        self.direction = False
        self.rect.bottomleft = x, y + 2
        self.radius = 100
        self.allowance = 0
        self.live = True

    def update(self) -> None:
        if not self.is_fight:
            self.move()
            self.bottomleft = self.rect.bottomleft
        if self.status != self.prev_status:
            self.ticks = 0
            self.prev_status = self.status
        if self.ticks / fps >= 0.2 or self.ticks / fps == 0:
            self.update_image()
            self.ticks = 0
        self.ticks += 1

    def move(self):
        collide_sprites = pygame.sprite.spritecollide(self, self.land_sprites, False)
        lst_platforms = []
        for i in collide_sprites:
            if i.__class__ == Platform:
                lst_platforms.append(i)
        if self.direction:
            if not any(i.rect.collidepoint(self.rect.bottomright) for i in lst_platforms):
                self.direction = not self.direction
            self.rect.x += 1
            self.status = "run"
        else:
            if not any(i.rect.collidepoint(self.rect.bottomleft) for i in lst_platforms):
                self.direction = not self.direction
            self.rect.x -= 1
            self.status = "run"

    def draw_radius(self, surface):
        screen = surface.convert_alpha()
        screen.fill([0, 0, 0, 0])
        pygame.draw.circle(screen, (255, 0, 0, 128), self.rect.center, 100)
        self.mob_x = self.rect[0]
        self.mob_y = self.rect[1]
