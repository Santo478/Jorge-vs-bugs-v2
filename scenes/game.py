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

    coin_pickup = pygame.mixer.Sound('assets/audio/Sound/CoinPick.wav')
    coin_pickup.set_volume(0.1)

    from elements.jorge import Player
    from elements.bug import Enemy
    from elements.intro import Coins
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
    coins = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    
    '''texto? tal vez'''
    puntaje = 0
    font = pygame.font.Font('freesansbold.ttf', 32)

    '''Zanax: Generador de Coins'''
    ADDCOIN = pygame.USEREVENT + 2
    pygame.time.set_timer(ADDCOIN, random.randint(7500,15000))

    ''' hora de hacer el gameloop '''
    running = True
    music_playing = False
    
    '''Animaciones de bugs'''
    from funciones.animations import SpriteSheet

    bug_sheet_image = pygame.image.load("assets/skins/bugs/BugSheet1.png").convert_alpha()
    bug_sprite_sheet = SpriteSheet(bug_sheet_image)

    num_frames = 3
    animation_list = []
    last_update = pygame.time.get_ticks()
    animation_cooldown = 100
    frame = 0

    for i in range(num_frames):
        aa = bug_sprite_sheet.get_frame(i, 32, 32)
        
        animation_list.append(aa)


    '''Loop principal'''

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
                    pause_state = PauseMenu(screen)
                    if pause_state == True:
                        return
                    else:
                        pass

            elif event.type == QUIT:
                pygame.display.quit()
                pygame.quit()

            elif event.type == ADDENEMY:
                new_enemy = Enemy(SCREEN_WIDTH, SCREEN_HEIGHT)
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)

            elif puntaje >= 10:
                if event.type == ADDCOIN:
                    new_coins = Coins(SCREEN_WIDTH, SCREEN_HEIGHT)
                    coins.add(new_coins)

        
        screen.blit(background_image, [0,0])
        screen.blit(font.render(str(puntaje), True, (255,255,255), (0,0,0)), (0,0))

        '''Bug animation handler'''
        current_time = pygame.time.get_ticks()
        if current_time - last_update >= animation_cooldown:
            frame += 1
            last_update = current_time
            if frame >= len(animation_list):
                frame = 0

        ''''''

        for entity in enemies:
            screen.blit(pygame.transform.scale(animation_list[frame], (entity.size, entity.size)), entity.rect)
        screen.blit(player.surf, player.rect)

        for X in coins:
            screen.blit(X.surf,X.rect)
            
        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)
        for entity in enemies:
            score = entity.update()
            puntaje += score

        #COLLIDE DE ENEMIGOS
        if pygame.sprite.spritecollide(player, enemies, False):   
            if pygame.sprite.spritecollide(player, enemies, False, pygame.sprite.collide_mask):
                player.kill()
                death = DeathScreen(screen)
                if death == True:
                    StartScene(screen)
                elif death == False:
                    return
        #COLLIDE DE MONEDAS 
        if pygame.sprite.spritecollide(player, coins, False):   
            if pygame.sprite.spritecollide(player, coins, True, pygame.sprite.collide_mask):
                coin_pickup.play()
                puntaje += 500
        
        pygame.display.flip()
        clock.tick(40)


