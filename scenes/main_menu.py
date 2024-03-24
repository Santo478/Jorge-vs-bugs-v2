import pygame

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

    pygame.display.set_caption("Main Menu")

    PlayImg = pygame.image.load('assets/Buttons/PlayButton.png').convert_alpha()
    play_button = Button(500, 300, PlayImg)

    QuitImg = pygame.image.load('assets/Buttons/QuitButton.png').convert_alpha()
    quit_button = Button(500, 450, QuitImg)

    run = True
    button_pressed = False

    clock = pygame.time.Clock()

    while run:
        screen.blit(background_image, [0,0])
        from .game import StartScene
        if quit_button.draw(screen) and button_pressed == False:
            run = False
        if play_button.draw(screen) and button_pressed == False:
            button_pressed = True
            StartScene(screen)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
        
        button_pressed = False
        pygame.display.update()
        clock.tick(40)
    