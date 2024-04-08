"""
Hola este es modulo Bug,
este modulo manejara la creacion y acciones de los Bugs
"""
import pygame
import random
import math
from pygame.locals import (RLEACCEL)

BUGpng = pygame.image.load('assets/skins/bugs/bug.png').convert_alpha()
BUGpng_scaled = pygame.transform.scale(BUGpng, (64,64))


class Enemy(pygame.sprite.Sprite):

    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, speed_level):
        # nos permite invocar métodos o atributos de Sprite
        super(Enemy, self).__init__()
        self.scale_factor = random.uniform(0.5, 1)
        self.size = 100 * self.scale_factor
        self.surf = pygame.transform.scale(BUGpng_scaled, (100 * self.scale_factor, 100 * self.scale_factor))
        self.mask = pygame.mask.from_surface(self.surf)
        self.surf.set_colorkey((0,0,0), RLEACCEL)
        self.rect = self.surf.get_rect(
            center = (
                SCREEN_WIDTH + 100,
                random.randint(0, SCREEN_HEIGHT),
            )
        )

        self.speed = random.randint(math.floor(5 * speed_level**0.5),math.floor(7 ** speed_level**0.5))



    def update(self):
        self.rect.move_ip(-self.speed,0)
        if self.rect.right < 0:
            self.kill()
            return 100
        return 0
