import pygame
import sys
import os

import world
from mobs import *
from data import *
from world import *
from copy import copy
import random

un_background = pygame.image.load('data/landshaft/space.png').convert_alpha()
bg_under = pygame.Surface(screen_size)
bg_under.blit(un_background, (0, 0))

letter_group = pygame.sprite.Group()

ltrs = []


class Underground(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.fight = False
        self.bgr = pygame.image.load('data/landshaft/space.png').convert_alpha()

    def load_fight_lvl(self, window):
        window.blit(self.bgr, (0, 0))


class Letters(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.letters = []
        self.start_word = []

    def random_letters(self):
        with open('data/singular_and_plural.txt', encoding='utf8') as f:
            lines = [line.rstrip('\n') for line in f]
            a = random.choice(lines)
            temp = []
            for i in a:
                temp.append(i)
            print(temp)
            self.start_word = copy(temp)
            random.shuffle(temp)
            self.letters = temp


class Letter(pygame.sprite.Sprite):
    def __init__(self, letter, image, letter_group):
        super().__init__(letter_group)
        self.letter = letter
        self.image = image
        self.rect = image.get_rect()
        self.topleft = self.rect.topleft
        self.selected = False
        self.coef = 5
        self.numb_selected = 100

    def move(self, x, y, but_selected):
        if self.selected:
            self.rect.topleft = self.topleft
            self.selected = False
        else:
            self.rect.topleft = x, y
            self.selected = True
            self.numb_selected = but_selected

    def __lt__(self, other):
        return self.numb_selected < other.numb_selected


def creating_letters(word, x_w, y_w):
    coef_start_pos = 4
    for l in word:
        temp = pygame.image.load(f'data/R_Letters/Letter_{l}.png').convert_alpha()
        temp = pygame.transform.scale(temp, (0.625 * x_w, 1.111111 * y_w))
        ltr = Letter(l, temp, letter_group)
        ltr.rect.topleft = x_w * coef_start_pos, y_w
        ltr.topleft = ltr.rect.topleft
        ltr.add(letter_group)
        coef_start_pos += 0.01041666 * x_w
        ltrs.append(ltr)
