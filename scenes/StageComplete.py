import pygame
from pygame import mixer
from pygame.locals import (K_ESCAPE, KEYDOWN, QUIT)

mixer.init()

sound = pygame.mixer.Sound('assets/audio/Sound/ExitpauseMenu.wav')
sound.set_volume(0.2)

def StageComplete(screen, next_stage):
    from .main_menu import MainMenu
    from .stage2 import StartScene2
    from .stage3 import StartScene3
    pygame.display.set_caption("Stage Completed")
    '''Cambiar musica'''
    pygame.mixer.music.pause()

    from funciones.button import Button
    SideButton = pygame.transform.scale(pygame.image.load("assets/Buttons/SideButton.png"), (70,70))
    ContinueImg = pygame.image.load('assets/Buttons/ContinueButton.png').convert_alpha()
    MainMenuImg = pygame.image.load('assets/Buttons/MainMenuButton.png').convert_alpha()

    buttons = [Button(500, 300, ContinueImg, "Continue"),
               Button(500, 450, MainMenuImg, "Main")]
    selected_index = 0
    buttons[selected_index].selected = True

    run = True

    while run:
        screen.fill((61, 105, 132))
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()
                pygame.quit()
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
                    if buttons[selected_index].use == "Continue":
                        buttons[selected_index].play_sound(2)
                        pygame.time.delay(200)
                        if next_stage == 2:
                            StartScene2(screen)
                        elif next_stage == 3:
                            StartScene3(screen)
                    elif buttons[selected_index].use == "Main":
                        buttons[selected_index].play_sound(2)
                        pygame.time.delay(200)
                        from .main_menu import MainMenu
                        MainMenu()
        for button in buttons:
            button.draw(screen)
        screen.blit(SideButton, (270 ,buttons[selected_index].rect.midleft[1] -30))
        pygame.display.update()

        pygame.display.update()