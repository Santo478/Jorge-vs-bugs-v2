import pygame
from pygame import mixer
from pygame.locals import (K_ESCAPE, KEYDOWN, QUIT)

mixer.init()

sound = pygame.mixer.Sound('assets/ExitpauseMenu.wav')
sound.set_volume(0.2)

def PauseMenu(screen):


    '''Cambiar musica'''
    pygame.mixer.music.pause()
    '''Botones'''
    
    from funciones.button import Button
    ResumeImg = pygame.image.load('assets/ResumeButton.png').convert_alpha()
    resume_button = Button(500, 300, ResumeImg)

    QuitImg = pygame.image.load('assets/QuitButton.png').convert_alpha()
    quit_button = Button(500, 450, QuitImg)

    run = True

    while run:
        screen.fill((52, 78, 91))

        if resume_button.draw(screen):
            sound.play()
            pygame.time.delay(150)
            break

        if quit_button.draw(screen):
            pygame.quit()

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sound.play()
                    pygame.time.delay(150)
                    return

            elif event.type == QUIT:
                pygame.quit()
        
        pygame.display.update()
    
