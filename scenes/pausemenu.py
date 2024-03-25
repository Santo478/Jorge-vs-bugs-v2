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
    MainMenuImg = pygame.image.load('assets/Buttons/MainMenuButton.png').convert_alpha()
    
    buttons = [Button(500, 300, ResumeImg, "Resume"),
               Button(500, 450, MainMenuImg, "Main")]
    selected_index = 0
    buttons[selected_index].selected = True


    run = True

    while run:
        screen.fill((61, 105, 132))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()
                return pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    sound.play()
                    pygame.time.delay(150)
                    return
                elif event.key == pygame.K_UP:
                    buttons[selected_index].play_sound(1)
                    buttons[selected_index].selected = False
                    selected_index = (selected_index - 1) % len(buttons)
                    buttons[selected_index].selected = True
                elif event.key == pygame.K_DOWN:
                    buttons[selected_index].play_sound(1)
                    buttons[selected_index].selected = False
                    selected_index = (selected_index + 1) % len(buttons)
                    buttons[selected_index].selected = True
                elif event.key == pygame.K_RETURN:
                    if buttons[selected_index].use == "Resume":
                        buttons[selected_index].play_sound(2)
                        pygame.time.delay(200)
                        return
                    elif buttons[selected_index].use == "Main":
                        buttons[selected_index].play_sound(2)
                        pygame.time.delay(200)
                        return True
        for button in buttons:
            button.draw(screen)
        
        pygame.display.update()
    
