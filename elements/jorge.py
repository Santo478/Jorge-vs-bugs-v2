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
        self.is_dead = False
        self.dead_countdown = 120
        self.speed = 4
        self.shield = False
        

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0,-self.speed)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,self.speed)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-self.speed*1.5,0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(self.speed,0)
        if not pressed_keys[K_UP] and not pressed_keys[K_DOWN] and not pressed_keys[K_LEFT] and not pressed_keys[K_RIGHT]:
            self.rect.move_ip(-2,0)



        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right > self.screen_width:
            self.rect.right = self.screen_width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > self.screen_height:
            self.rect.bottom = self.screen_height
        
        if self.is_dead:
            self.dead_countdown -= 1
        if self.dead_countdown == 0:
            self.is_dead = False
            self.dead_countdown = 120

    def increase_speed(self):
        self.speed *= 1.5

    def add_shield(self):
        self.shield = True
        
