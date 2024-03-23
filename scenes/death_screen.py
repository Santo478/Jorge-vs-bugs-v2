import pygame
from pygame import mixer
from funciones.button import Button
from .game import StartScene
from .main_menu import MainMenu
from pygame.locals import (K_ESCAPE, KEYDOWN, QUIT)

mixer.init()

#sound = pygame.mixer.Sound()
#sound.set_volume(0.2)

def DeathScreen(screen):

    pygame.display.set_caption("You Died")
    '''Cambiar musica'''
    pygame.mixer.music.pause()

    RetryImg = pygame.image.load('assets/Buttons/RetryButton.png').convert_alpha()
    retry_button = Button(500, 300, RetryImg)

    MainMenuImg = pygame.image.load('assets/Buttons/MainMenuButton.png').convert_alpha()
    main_menu_button = Button(500, 450, MainMenuImg)

    run = True

    while run:
        screen.fill((52, 78, 91))

        if retry_button.draw(screen):
            return True
        if main_menu_button.draw(screen):
            return False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()
                return pygame.quit()
        
        pygame.display.update()