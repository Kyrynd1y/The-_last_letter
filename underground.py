import pygame
import sys
import os

from mobs import *
from world import *
from data import *
import random

with open('RUS.txt') as f:
    lines = [line.rstrip('\n') for line in f]
    a = random.choice(lines)
    temp = []
    for i in a:
        temp.append(i)
    random.shuffle(temp)
    print(a)
    print(temp)


class Underground(pygame.sprite.Sprite):
    pass


class Letters(pygame.sprite.Sprite):
    pass
