from data import *

background = pygame.image.load('data/landshaft/BG1.png')
background = pygame.transform.scale(background, (1920, 1080))

background2 = pygame.image.load('data/landshaft/BG2.png')
background2 = pygame.transform.scale(background2, (1920, 1080))

background3 = pygame.image.load('data/landshaft/BG3.png')
background3 = pygame.transform.scale(background3, (1920, 1080))

un_background = pygame.image.load('data/landshaft/space.png')

bg = pygame.Surface((1920, 1080))

bg.blit(background, (0, 0))
bg.blit(background2, (0, 0))
bg.blit(background3, (0, 0))


class Platform(pygame.sprite.Sprite):
    def __init__(self, pos, image, land_sprites):
        super().__init__(land_sprites)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = pos


class Button(pygame.sprite.Sprite):
    def __init__(self, center_x, center_y, text, button_sprites):
        super().__init__(button_sprites)
        self.status = 'idle'
        self.text = text
        if button_statuses.index(self.status) != 0:
            print(button_statuses.index(self.status))
        self.image = button_images[buttons.index(text)][button_statuses.index(self.status)]
        self.rect = self.image.get_rect()
        self.rect.center = center_x, center_y

    def update(self) -> None:
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if not pygame.mouse.get_pressed()[0]:
                self.status = 'aim'
            else:
                self.status = 'pressed'
        else:
            self.status = 'idle'
        self.image = button_images[buttons.index(self.text)][button_statuses.index(self.status)]


def TxT(text, font, color, x, y):
    render = font.render(text, True, pygame.Color(color))
    rect = render.get_rect()
    rect.center = x, y
    return render, rect

#
