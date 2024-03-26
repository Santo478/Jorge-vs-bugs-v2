import pygame
pygame.init()
pygame.mixer.init()

sound1 = pygame.mixer.Sound("assets/audio/Sound/ButtonChange.mp3")
sound1.set_volume(0.2)
sound2 = pygame.mixer.Sound("assets/audio/Sound/ButtonPressed.mp3")
sound2.set_volume(0.1)
        
class Button:
    def __init__(self, x, y, image, use):
        self.surf = pygame.Surface((300,100), pygame.SRCALPHA)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.clicked = False
        self.selected = False
        self.use = use

    def play_sound(self, num):
        if num == 1:
            sound1.play()
        if num == 2:
            sound2.play()

    def draw(self, screen):
        self.surf.blit(self.image, (0,0))
        pygame.PixelArray(self.surf).replace((191,191,191), (240,240,240))
        
        # Cambiar el color si el botón está seleccionado
        button = self.surf if self.selected else self.image
        screen.blit(button, (self.rect.x,self.rect.y))

    def activate(self):
        # Realizar la acción del botón
        sound2.play()
        return True