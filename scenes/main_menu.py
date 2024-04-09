import pygame
import random

from pygame import mixer
from funciones.button import Button
from pygame.locals import (QUIT)

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background_image1 = pygame.image.load('assets//Backgrounds/portada.png').convert()
background_image = pygame.transform.scale(background_image1, (1000,700))

pygame.mouse.set_visible(False)

opacity_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
def opacity_to_screen():
    pygame.draw.rect(opacity_surface, (0, 0, 0, 55), (0,0,1000,700))


def MainMenu():
    pygame.display.set_caption("Main Menu")
    from .game import StartScene
    from .stage2 import StartScene2
    from .stage3 import StartScene3


    #button handler

    SideButton = pygame.transform.scale(pygame.image.load("assets/Buttons/SideButton.png"), (70,70))

    PlayImg = pygame.image.load('assets/Buttons/PlayButton.png').convert_alpha()
    QuitImg = pygame.image.load('assets/Buttons/QuitButton.png').convert_alpha()
    TutorialImg = pygame.image.load("assets/Buttons/TutorialButton.PNG").convert_alpha()
    
    buttons = [Button(500, 300, PlayImg, "Play"),
               Button(500, 450, TutorialImg, "Tutorial"),
               Button(500, 600, QuitImg, "Quit")]
    selected_index = 0
    buttons[selected_index].selected = True


    #variables
    run = True
    music_played = True

    '''
    range = 0
    range_bool = True
    '''

    clock = pygame.time.Clock()

    while run:
        
        #Maneja que la musica suene de nuevo al volver al menu
        if music_played:
            music_played = False
            pygame.mixer.music.load('assets/audio/Music/MenuMusic.mp3')
            pygame.mixer.music.set_volume(0.1)
            pygame.mixer.music.play(-1, 0, 1000)

        screen.blit(background_image, [0,0])
        screen.blit(opacity_surface, (0,0))
        opacity_to_screen()

        '''if range_bool:
            range += 1
        elif range_bool == False:
            range -= 1
        if range == 20:
            range_bool = False
        if range == -20:
            range_bool = True
        '''
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
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
                    if buttons[selected_index].use == "Play":
                        music_played = True
                        buttons[selected_index].play_sound(2)
                        pygame.time.delay(300)
                        StartScene(screen)
                    elif buttons[selected_index].use == "Quit":
                        buttons[selected_index].play_sound(2)
                        pygame.time.delay(700)
                        pygame.quit()
                        run = False
                    elif buttons[selected_index].use == "Tutorial":
                        buttons[selected_index].play_sound(2)
                        pygame.time.delay(300)
        for button in buttons:
            button.draw(screen)

        screen.blit(SideButton, (270 ,buttons[selected_index].rect.midleft[1] -30))
        pygame.display.update()
        clock.tick(40)
