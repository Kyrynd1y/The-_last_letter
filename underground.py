import pygame
import sys
import os

from mobs import *
from world import *
from data import *
import random


class Underground(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)


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
            pygame.transform.scale(letter, (60, 60))
            screen.blit(letter, (x, y))
            x += 60

#