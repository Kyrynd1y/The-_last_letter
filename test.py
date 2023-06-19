import pygame
from pygame.locals import *

import additional
import data

pygame.init()
pygame.display.set_caption('End credits')
screen = pygame.display.set_mode(data.window.get_size())
screen_r = screen.get_rect()
font = pygame.font.SysFont("Arial", 40)
clock = pygame.time.Clock()

bgr = pygame.image.load('data/landshaft/space.png').convert_alpha()


def titles():
    pygame.mixer.music.stop()
    pygame.mixer.music.load("data/music/C418_-_Haggstrom_30921643.mp3")
    pygame.mixer.music.set_volume(additional.settings.value_volume / 100 / 2)
    pygame.mixer.music.play(1)
    # pygame.mixer.music.set_volume(0.02)

    credit_list = ["THE_LAST_LETTER", " ", '', "Программисты:", " ",
                   'Kyrynd1y', " ", 'Ибатуллин Денис', '', 'Geranton_Storm', '', '', 'Музыка:', '',
                   'Даниээль Роозенфельд', '', '', 'Графика и дизайн:', '', 'Kyrynd1y', '', '', 'Бетта тестеры:', '',
                   'Валерий Центнер',
                   '', '', 'Режиссеры:', '', 'Ибатуллин Денис', '', 'Другова Светлана Андреевна']

    texts = []

    for i, line in enumerate(credit_list):
        s = font.render(line, 1, (10, 10, 10))

        r = s.get_rect(centerx=screen_r.centerx, y=screen_r.bottom + i * 45)
        texts.append((r, s))

    while True:
        for e in pygame.event.get():
            if e.type == QUIT or e.type == KEYDOWN and e.key == pygame.K_ESCAPE:
                pygame.mixer.music.stop()
                pygame.mixer.music.load("data/music/C418_-_Haggstrom_30921643.mp3")
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(0.03)
                return

        screen.fill((255, 255, 255))

        for r, s in texts:
            r.move_ip(0, -1)
            screen.blit(s, r)

        if not screen_r.collidelistall([r for (r, _) in texts]):
            return

        pygame.display.flip()

        clock.tick(60)


if __name__ == '__main__':
    titles()
