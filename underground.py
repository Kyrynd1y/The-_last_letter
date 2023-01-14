import pygame
import sys
import os

import world
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

    def load_fight_lvl(self, window):
        window.blit(self.bgr, (0, 0))


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


class Letter(pygame.sprite.Sprite):
    def __init__(self, letter, image, letter_group):
        super().__init__(letter_group)
        self.letter = letter
        self.image = image
        self.rect = image.get_rect()

#
