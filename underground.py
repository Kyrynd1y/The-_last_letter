import pygame
import sys
import os

from mobs import *
from world import *
from data import *
import requests

response = requests.get('https://raw.githubusercontent.com/danakt/russian-words/master/russian.txt')

text = response.content.decode('cp1251')

with open('russian.txt', 'wb') as ru:
    ru.write(text.encode('utf-8'))

response = requests.get('https://raw.githubusercontent.com/danakt/russian-words/master/russian_surnames.txt')

text = response.content.decode('cp1251')

with open('russian_surnames.txt', 'wb') as ru:
    ru.write(text.encode('utf-8'))


class Underground(pygame.sprite.Sprite):
    pass


class Letters(pygame.sprite.Sprite):
    pass

