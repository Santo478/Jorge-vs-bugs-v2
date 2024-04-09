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
        self.shield_duration = 4000
        self.speed_duration = 5000
        self.slowness_duration = 7000
 
    def update(self):
        self.rect.move_ip(-3,0)
        if self.rect.right < 0:
            self.kill()

    def apply_effect(self, enemy, player):
        if self.type == "speed":
            original_speed = player.speed
            player.increase_speed()
            start_time = time.time()
            while time.time() - start_time < self.speed_duration:
                pass
            enemy.speed = original_speed
        
        elif self.type == "shield":
            player.add_shield()
            start_time = time.time()
            while time.time() - start_time < self.shield_duration:
                pass
            player.shield = False

        elif self.type == "slowness":
            for item in enemy:
                original_speed = item.speed
            item.decrease_speed()
            start_time = time.time()
            while time.time() - start_time < self.slowness_duration:
                pass
            item.speed = original_speed

    def play_pickup(self):
        pickup_sound.play()
