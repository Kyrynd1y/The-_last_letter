import pygame
import sys
import os

from mobs import *
from data import *
from world import *
import random

un_background = pygame.image.load('data/landshaft/space.png')
bg_under = pygame.Surface((1920, 1080))
bg_under.blit(un_background, (0, 0))


class Underground(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.fight = False
        self.bgr = pygame.image.load('data/landshaft/space.png')

    def fight_start(self, hero, mob):
        for event in pygame.event.get():
            if (hero.hero_x - mob.mob_x) ** 2 + (hero.hero_y - mob.mob_y) ** 2 <= (hero.radius + mob.radius) ** 2 \
                    and event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                self.fight = True


class Letters(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.letters = []

    def random_letters(self):
        with open('RUS.txt') as f:
            lines = [line.rstrip('\n') for line in f]
            a = random.choice(lines)
            temp = []
            for i in a:
                temp.append(i)
            random.shuffle(temp)
            self.letters = temp

    def draw_letters(self, screen: pygame.Surface, x, y):
        for elem in self.letters:
            letter = pygame.image.load(f'data/R_Letters/Letter_{elem}.png')
            a = pygame.transform.scale(letter, (60, 60))
            pygame.transform.scale(image, (60, 60))
            screen.blit(a, (x, y))
            x += 80

#
