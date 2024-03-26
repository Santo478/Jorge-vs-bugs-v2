import pygame



class SpriteSheet():
    def __init__(self, image, num_frames, cooldown):
        self.sheet = image
        self.num_frames = num_frames
        self.cooldown = cooldown
        self.animation_list = []
        self.frame = 0

    def get_frames(self, width, height):
        for i in range(self.num_frames):
            image = pygame.Surface((width, height), pygame.SRCALPHA)
            image.blit(self.sheet, (0,0), (width * i, 0, width, height))
            self.animation_list.append(image)

'''
current_time = pygame.time.get_ticks()
if current_time - last_update >= animation_cooldown:
    frame += 1
    last_update = current_time
    if frame >= len(animation_list):
        frame = 0
'''
'''
num_frames = 3
animation_list = []
last_update = pygame.time.get_ticks()
animation_cooldown = 100
frame = 0

for i in range(num_frames):
    aa = bug_sprite_sheet.get_frame(i, 32, 32)
    
    animation_list.append(aa)
''' 