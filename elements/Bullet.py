import pygame
from pygame.locals import (RLEACCEL)

# Definición de colores

Bulletpng = pygame.image.load('assets/Extras/Bullets.png').convert_alpha()
Bulletpng_scaled = pygame.transform.scale(Bulletpng, (45,27))


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.surf = Bulletpng_scaled

        self.mask = pygame.mask.from_surface(self.surf)

        self.surf.set_colorkey((255,255,255), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.center = (x, y)
        self.speed = 10

    def update(self):
        self.rect.x += self.speed
        if self.rect.right > 1050:
            self.kill()
            return("Charge")