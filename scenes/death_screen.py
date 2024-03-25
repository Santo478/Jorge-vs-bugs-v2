import pygame
from pygame import mixer
from funciones.button import Button
from pygame.locals import (QUIT)

mixer.init()

#sound = pygame.mixer.Sound()
#sound.set_volume(0.2)

def DeathScreen(screen):

    pygame.display.set_caption("You Died")
    '''Cambiar musica'''
    pygame.mixer.music.pause()

    RetryImg = pygame.image.load('assets/Buttons/RetryButton.png').convert_alpha()
    MainMenuImg = pygame.image.load('assets/Buttons/MainMenuButton.png').convert_alpha()

    buttons = [Button(500, 300, RetryImg, "Retry"),
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
                if event.key == pygame.K_UP:
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
                    if buttons[selected_index].use == "Retry":
                        buttons[selected_index].play_sound(2)
                        pygame.time.delay(200)
                        return True
                    elif buttons[selected_index].use == "Main":
                        buttons[selected_index].play_sound(2)
                        pygame.time.delay(200)
                        return False
        for button in buttons:
            button.draw(screen)
        
        pygame.display.update()