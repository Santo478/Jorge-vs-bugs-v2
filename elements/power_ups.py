import pygame
import time
pygame.init()
pygame.mixer.init()

ShieldPNG = pygame.image.load('assets/Extras/Shield.PNG').convert_alpha()
ShieldPNG_scaled = pygame.transform.scale(ShieldPNG,(35,35))
SpeedPNG = pygame.image.load('assets/Extras/PowerSpeed.png').convert_alpha()
SpeedPNG_scaled = pygame.transform.scale(SpeedPNG,(35,35))
SlownessPNG = pygame.image.load('assets/Extras/Snail.PNG').convert_alpha()
SlownessPNG_scaled = pygame.transform.scale(SlownessPNG,(35,35))

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, x, y, powerup_type, image):
        super().__init__()
        self.type = powerup_type
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.rect.move_ip(-2,0)

class SpeedPowerUp(PowerUp):
    def __init__(self, x, y):
        super().__init__(x, y, "speed",SpeedPNG_scaled)
        self.speed_duration = 5

    def apply_effect(self, player):
        original_speed = player.speed
        player.increase_speed(self.speed_duration)
        start_time = time.time()
        while time.time() - start_time < self.speed_duration:
            pass
        player.speed = original_speed

class ShieldPowerUp(PowerUp):
    def __init__(self, x, y):
        super().__init__(x, y, "shield",ShieldPNG_scaled)
        self.shield_duration = 10

    def apply_effect(self, player):
        player.add_shield(self.shield_duration)
        start_time = time.time()
        while time.time() - start_time < self.speed_duration:
            pass
        player.shield = False

class SlownessPowerUp(PowerUp):
    def __init__(self, x, y):
        super().__init__(x, y, "slowness",SlownessPNG_scaled) 
        self.slowness_duration = 10
    
    def apply_effect(self, enemy):
        original_speed = enemy.speed
        enemy.decrease_speed(self.speed_duration)
        start_time = time.time()
        while time.time() - start_time < self.speed_duration:
            pass
        enemy.speed = original_speed