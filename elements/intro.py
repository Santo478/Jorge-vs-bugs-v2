import pygame
import random
from pygame.locals import (RLEACCEL)

Intropng = pygame.image.load('assets/Extras/IntroCoins.png').convert_alpha()
Intropng_scaled = pygame.transform.scale(Intropng, (50,50))


class Coins(pygame.sprite.Sprite):

    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        # nos permite invocar métodos o atributos de Sprite
        super(Coins, self).__init__()
        self.surf = Intropng_scaled

        self.mask = pygame.mask.from_surface(self.surf)

        self.surf.set_colorkey((0,0,0), RLEACCEL)
        self.screen_width = SCREEN_WIDTH
        self.screen_height = SCREEN_HEIGHT
        self.rect = self.surf.get_rect(
            center = (
                random.randint(50,800),
                random.randint(50, 650),
            )
        )