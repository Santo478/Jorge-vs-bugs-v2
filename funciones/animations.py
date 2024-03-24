import pygame



class SpriteSheet():
    def __init__(self, image):
        self.sheet = image

    def get_frame(self, frame, width, height):
        image = pygame.Surface((width, height), pygame.SRCALPHA)
        image.blit(self.sheet, (0,0), (width * frame, 0, width, height))
        
        return image