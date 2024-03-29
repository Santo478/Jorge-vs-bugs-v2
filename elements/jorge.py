"""
Hola este es modulo Jorge,
este modulo manejara la creacion y movimiento de Jorge
"""
import pygame
from pygame.locals import (
    K_UP, K_DOWN, K_LEFT, K_RIGHT, RLEACCEL)


JorgePNG = pygame.image.load('assets/skins/jorge/JorgeVJ.png').convert_alpha()
JorgePNG_scaled = pygame.transform.scale(JorgePNG, (64,64))

class Player(pygame.sprite.Sprite):
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        # nos permite invocar métodos o atributos de Sprite
        super(Player, self).__init__()
        self.surf = JorgePNG_scaled

        self.mask = pygame.mask.from_surface(self.surf)

        self.surf.set_colorkey((0,0,0), RLEACCEL)
        self.rect = self.surf.get_rect(midleft=(30, 350))
        self.screen_width = SCREEN_WIDTH
        self.screen_height = SCREEN_HEIGHT
        self.lives = 3
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()
        

    def update(self, pressed_keys):
        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1000:
            self.hidden = False
            if self.rect.left < 0:
                self.rect.midleft = (30, 350)
        if pressed_keys[K_UP]:
            self.rect.move_ip(0,-4)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,4)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-6,0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(4,0)
        if not pressed_keys[K_UP] and not pressed_keys[K_DOWN] and not pressed_keys[K_LEFT] and not pressed_keys[K_RIGHT]:
            self.rect.move_ip(-2,0)


        if self.hidden == False and self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right > self.screen_width:
            self.rect.right = self.screen_width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > self.screen_height:
            self.rect.bottom = self.screen_height

    def hide(self,pressed_keys):
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (-80, 350)
        self.rect.move_ip(0,0)

    
