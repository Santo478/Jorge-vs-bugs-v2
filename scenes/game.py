'''
Hola este es modulo game,
este modulo manejara la escena donde ocurre nuestro juego
'''
import random
import pygame
from pygame import mixer
from pygame.locals import (K_ESCAPE, KEYDOWN, QUIT)
from .pausemenu import PauseMenu

pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()
pygame.init()
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700

'''cargar musica'''


''' 2.- crear el objeto pantalla'''
background_image1 = pygame.image.load('assets//Backgrounds/pixelBackground.png').convert()
background_image = pygame.transform.scale(background_image1, (1000,700))


def StartScene(screen):

    '''play music'''

    pygame.mixer.music.load('assets/audio/Music/8bitmusic.mp3')
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1, 0, 1000)


    menu_sound = pygame.mixer.Sound('assets/audio/Sound/MenuSound.wav')
    menu_sound.set_volume(0.2)

    from elements.jorge import Player
    from elements.bug import Enemy
    from .death_screen import DeathScreen

    pygame.display.set_caption("Game")
    clock = pygame.time.Clock()
    ''' 2.- generador de enemigos'''

    ADDENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDENEMY, 600)

    ''' 3.- creamos la instancia de jugador'''
    player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)

    ''' 4.- contenedores de enemigos y jugador'''
    enemies = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    
    ''' hora de hacer el gameloop '''
    running = True
    music_playing = False
    

    while running:
        retry = False
        if music_playing:
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.play(-1, 0, 1000)
            music_playing = True
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    menu_sound.play()
                    PauseMenu(screen)

            elif event.type == QUIT:
                pygame.display.quit()
                pygame.quit()

            elif event.type == ADDENEMY:
                new_enemy = Enemy(SCREEN_WIDTH, SCREEN_HEIGHT)
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)

        
        screen.blit(background_image, [0,0])
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)
            
        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)
        enemies.update()

        if pygame.sprite.spritecollide(player, enemies, False):   
            if pygame.sprite.spritecollide(player, enemies, False, pygame.sprite.collide_mask):
                player.kill()
                if DeathScreen(screen):
                    StartScene(screen)
                else:
                    return
                    
        pygame.display.flip()
        clock.tick(40)


