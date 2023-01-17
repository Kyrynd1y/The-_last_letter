import pygame
import sys
import os

import world
from mobs import *
from data import *
from world import *
from copy import copy
import random

un_background = pygame.image.load('data/landshaft/space.png')
bg_under = pygame.Surface((1920, 1080))
bg_under.blit(un_background, (0, 0))

letter_group = pygame.sprite.Group()

# alphabet = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о",
#            "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]

ltrs = []


class Underground(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.fight = False
        self.bgr = pygame.image.load('data/landshaft/space.png')

    def load_fight_lvl(self, window):
        window.blit(self.bgr, (0, 0))


class Letters(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.letters = []
        self.start_word = []

    def random_letters(self):
        with open('russian.txt') as f:
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

    def move(self, x, y):
        if self.selected:
            self.rect.topleft = self.topleft
            self.selected = False
        else:
            self.rect.topleft = x, y
            self.selected = True


def creating_letters(word, x_w, y_w):
    coef_start_pos = 3
    for l in word:
        temp = pygame.image.load(f'data/R_Letters/Letter_{l}.png')
        temp = pygame.transform.scale(temp, (60, 60))
        ltr = Letter(l, temp, letter_group)
        ltr.rect.topleft = x_w * coef_start_pos, y_w
        ltr.topleft = ltr.rect.topleft
        ltr.add(letter_group)
        coef_start_pos += 1
        ltrs.append(ltr)
