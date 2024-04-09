import pygame
import time
pygame.init()
pygame.mixer.init()
from pygame.locals import (RLEACCEL)

pickup_sound = pygame.mixer.Sound("assets/audio/Sound/PowerUp.wav")
pickup_sound.set_volume(0.2)

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, x, y, powerup_type, image):
        super(PowerUp, self).__init__()
        self.image = image
        self.type = powerup_type
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.shield_duration = 3000
        self.speed_duration = 5000
        self.slowness_duration = 7000
 
    def update(self):
        self.rect.move_ip(-3,0)
        if self.rect.right < 0:
            self.kill()

    def apply_effect(self, enemy, player):
        if self.type == "speed":
            print("speed")
            original_speed = player.speed
            player.increase_speed()
        
        elif self.type == "shield":
            player.add_shield()
            print("shield")


        elif self.type == "slowness":
            enemy.decrease_speed()
            print("slow")

    def play_pickup(self):
        pickup_sound.play()
