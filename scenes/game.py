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


'''background logic'''
background_image1 = pygame.image.load('assets//Backgrounds/RepeatBG.png').convert()
background_image = pygame.transform.scale(background_image1, (1000,700))

'''vidas'''

VidasPNG = pygame.image.load('assets/Extras/Heart.png').convert_alpha()
VidasPNG_scaled = pygame.transform.scale(VidasPNG, (40,40))


def StartScene(screen):
    background_scrolls = 0
    
    '''play music'''

    pygame.mixer.music.load('assets/audio/Music/8bitmusic.mp3')
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1, 0, 1000)


    menu_sound = pygame.mixer.Sound('assets/audio/Sound/MenuSound.wav')
    menu_sound.set_volume(0.2)

    coin_pickup = pygame.mixer.Sound('assets/audio/Sound/CoinPick.wav')
    coin_pickup.set_volume(0.1)

    hurt_sound = pygame.mixer.Sound("assets/audio/Sound/Hurt.mp3")
    hurt_sound.set_volume(0.3)



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
    bug_sprite_sheet = SpriteSheet(bug_sheet_image, 3, 100)
    bug_sprite_sheet.get_frames(32, 32)

    jorge_sheet_image = pygame.image.load("assets/skins/Jorge/JorgeVJSheet.png").convert_alpha()
    jorge_sprite_sheet = SpriteSheet(jorge_sheet_image, 2, 100)
    jorge_sprite_sheet.get_frames(50, 50)

    coins_sprite_image = pygame.image.load("assets/Extras/IntroCoinsSheet.png").convert_alpha()
    coins_sprite_sheet = SpriteSheet(coins_sprite_image, 8, 100)
    coins_sprite_sheet.get_frames(30, 30)

    last_update = pygame.time.get_ticks()


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

        #background scroller
        for i in range(2):
            screen.blit(background_image, (i * 1000 + background_scrolls, 0))
        background_scrolls -= 2
        if abs(background_scrolls) > 1000:
            background_scrolls = 0
        


        screen.blit(font.render(str(puntaje), True, (255,255,255), (0,0,0)), (0,0))

        '''animation cooldown handler'''
        current_time = pygame.time.get_ticks()
        if current_time - last_update >= bug_sprite_sheet.cooldown:
            bug_sprite_sheet.frame += 1
            jorge_sprite_sheet.frame += 1
            coins_sprite_sheet.frame += 1
            last_update = current_time
            if bug_sprite_sheet.frame >= len(bug_sprite_sheet.animation_list):
                bug_sprite_sheet.frame = 0
            if jorge_sprite_sheet.frame >= len(jorge_sprite_sheet.animation_list):
                jorge_sprite_sheet.frame = 0
            if coins_sprite_sheet.frame >= len(coins_sprite_sheet.animation_list):
                coins_sprite_sheet.frame = 0
    
            

        ''''''

        for entity in enemies:
            screen.blit(pygame.transform.scale(bug_sprite_sheet.animation_list[bug_sprite_sheet.frame], (entity.size, entity.size)), entity.rect)
        screen.blit(pygame.transform.scale(jorge_sprite_sheet.animation_list[jorge_sprite_sheet.frame], (64, 64)), player.rect)
        for entity in coins:
            screen.blit(coins_sprite_sheet.animation_list[coins_sprite_sheet.frame],entity.rect)

            
        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)
        for entity in enemies:
            score = entity.update()
            puntaje += score

        #COLLIDE DE ENEMIGOS
        if pygame.sprite.spritecollide(player, enemies, False):   
            if pygame.sprite.spritecollide(player, enemies, False, pygame.sprite.collide_mask):
                player.hide(pressed_keys)
                player.lives -= 1
                hurt_sound.play()
            
        if player.lives <= 0:
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
        
        #DISPLAY VIDAS
        for i in range(player.lives):
            screen.blit(VidasPNG_scaled,(820 + 40*i, 40))
        
        pygame.display.flip()
        clock.tick(40)


