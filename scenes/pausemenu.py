import pygame
from pygame import mixer
from pygame.locals import (K_ESCAPE, KEYDOWN, QUIT)

mixer.init()

sound = pygame.mixer.Sound('assets/audio/Sound/ExitpauseMenu.wav')
sound.set_volume(0.2)

def PauseMenu(screen):
    from .main_menu import MainMenu
    pygame.display.set_caption("Pause Menu")
    '''Cambiar musica'''
    pygame.mixer.music.pause()
    '''Botones'''
    
    from funciones.button import Button
    ResumeImg = pygame.image.load('assets/Buttons/ResumeButton.png').convert_alpha()
    resume_button = Button(500, 300, ResumeImg)

    MainMenuImg = pygame.image.load('assets/Buttons/MainMenuButton.png').convert_alpha()
    main_menu_button = Button(500, 450, MainMenuImg)

    

    run = True

    while run:
        screen.fill((52, 78, 91))

        if resume_button.draw(screen):
            sound.play()
            pygame.time.delay(150)
            return

        if main_menu_button.draw(screen):
            return True
        
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sound.play()
                    pygame.time.delay(150)
                    return

            elif event.type == QUIT:
                pygame.display.quit()
                pygame.quit()
        
        pygame.display.update()
    
