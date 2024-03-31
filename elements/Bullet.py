import pygame
import random
from pygame.locals import (RLEACCEL)

BUGpng = pygame.image.load('assets/skins/bugs/bug.png').convert_alpha()
BUGpng_scaled = pygame.transform.scale(BUGpng, (64,64))


class Bullet(pygame.sprite.Sprite):

    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        # nos permite invocar métodos o atributos de Sprite
        super(Bullet, self).__init__()
        self.surf = BUGpng_scaled

        self.mask = pygame.mask.from_surface(self.surf)

        self.surf.set_colorkey((0,0,0), RLEACCEL)
        self.screen_width = SCREEN_WIDTH
        self.screen_height = SCREEN_HEIGHT
        self.rect = self.surf.get_rect(
            center = (
                random.randint(150,800),
                random.randint(50, 650),
            )
        )
    def update(self):
        self.rect.move_ip(10,0)
        if self.rect.right > 1000:
            self.kill()
            return 100
        return 0