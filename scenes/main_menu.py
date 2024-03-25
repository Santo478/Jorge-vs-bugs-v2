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



def MainMenu():

    #music handler
    

    pygame.display.set_caption("Main Menu")

    PlayImg = pygame.image.load('assets/Buttons/PlayButton.png').convert_alpha()
    play_button = Button(500, 300, PlayImg)

    QuitImg = pygame.image.load('assets/Buttons/QuitButton.png').convert_alpha()
    quit_button = Button(500, 450, QuitImg)


    #variables
    run = True
    button_pressed = False
    button_timer = 0
    
    music_played = True

    clock = pygame.time.Clock()

    while run:

        #Maneja que la musica suene de nuevo al volver al menu
        if music_played:
            music_played = False
            pygame.mixer.music.load('assets/audio/Music/MenuMusic.mp3')
            pygame.mixer.music.set_volume(0.1)
            pygame.mixer.music.play(-1, 0, 1000)


        #Cooldown para clickear
        if button_pressed:
            button_timer += 1
            if button_timer == 25:
                button_timer = 0
                button_pressed = False

        screen.blit(background_image, [0,0])
        from .game import StartScene
        if quit_button.draw(screen) and (button_pressed == False):
            button_pressed = True
            run = False
        if play_button.draw(screen) and (button_pressed == False):
            button_pressed = True
            music_played = True
            StartScene(screen)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False

        pygame.display.update()
        clock.tick(40)
    