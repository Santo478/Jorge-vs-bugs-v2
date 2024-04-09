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
background_image = pygame.transform.scale(background_image1, (SCREEN_WIDTH, SCREEN_HEIGHT))
background_image2 = pygame.image.load('assets//Backgrounds/RepeatBGBlue.png').convert()
background_imageBlue = pygame.transform.scale(background_image2, (SCREEN_WIDTH, SCREEN_HEIGHT))
background_image3 = pygame.image.load('assets//Backgrounds/RepeatBGYellow.png').convert()
background_imageYellow = pygame.transform.scale(background_image3, (SCREEN_WIDTH, SCREEN_HEIGHT))
background_image4 = pygame.image.load('assets//Backgrounds/RepeatBGRed.png').convert()
background_imageRed = pygame.transform.scale(background_image4, (SCREEN_WIDTH, SCREEN_HEIGHT))


'''vidas'''

VidasPNG = pygame.image.load('assets/Extras/Heart.png').convert_alpha()
VidasPNG_scaled = pygame.transform.scale(VidasPNG, (40,40))
FullPNG = pygame.image.load('assets/Extras/FullCharge.png').convert_alpha()
FullPNG_scaled = pygame.transform.scale(VidasPNG, (40,40))

#Ajustador de opacity
opacity_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
def opacity_to_screen():
    pygame.draw.rect(opacity_surface, (0, 0, 0, 55), (0,0,15 + 32*len,30))


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

    Power_pickup = pygame.mixer.Sound('assets/audio/Sound/PowerUP.wav')
    Power_pickup.set_volume(0.1)



    from elements.jorge import Player
    from elements.bug import Enemy
    from elements.intro import Coins
    from elements.Bullet import Bullet
    from .death_screen import DeathScreen
    from elements.power_ups import PowerUp

    pygame.display.set_caption("Stage 1")
    clock = pygame.time.Clock()
    ''' 2.- generador de enemigos'''

    ADDENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDENEMY, 600)

    ''' 3.- creamos la instancia de jugador'''
    player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)

    ''' 4.- contenedores de enemigos y jugador'''
    enemies = pygame.sprite.Group()
    coins = pygame.sprite.Group()
    powerups = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    all_sprites.add(player)

    
    '''texto? tal vez'''
    puntaje = 0
    opacity_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
    def opacity_to_screen():
        pygame.draw.rect(opacity_surface, (0, 0, 0, 155), (0,0,15 + 16*len(str(puntaje)),30))

    font = pygame.font.Font('assets/Fontxd.otf', 16)

    '''Zanax: Generador de Coins'''
    ADDCOIN = pygame.USEREVENT + 2
    pygame.time.set_timer(ADDCOIN, random.randint(7500,15000))

    '''Generador power ups'''

    ShieldPNG = pygame.image.load('assets/Extras/Shield.PNG').convert_alpha()
    ShieldPNG_scaled = pygame.transform.scale(ShieldPNG,(35,35))
    SpeedPNG = pygame.image.load('assets/Extras/PowerSpeed.png').convert_alpha()
    SpeedPNG_scaled = pygame.transform.scale(SpeedPNG,(35,35))
    SlownessPNG = pygame.image.load('assets/Extras/Snail.PNG').convert_alpha()
    SlownessPNG_scaled = pygame.transform.scale(SlownessPNG,(35,35))

    POWERUP_TYPES = ["speed", "shield", "slowness"]

    def spawn_power_up():
        x = 1000
        y = random.randint(50,SCREEN_HEIGHT - 50)
        powerup_type = random.choice(POWERUP_TYPES)
        if powerup_type == "speed":
            powerup = PowerUp(x, y, powerup_type, SpeedPNG_scaled)
        elif powerup_type == "shield":
            powerup = PowerUp(x, y, powerup_type, ShieldPNG_scaled)
        elif powerup_type == "slowness":
            powerup = PowerUp(x, y, powerup_type, SlownessPNG_scaled)
        powerups.add(powerup)
        

    SPAWN_POWERUP_EVENT = pygame.USEREVENT + 3
    pygame.time.set_timer(SPAWN_POWERUP_EVENT, random.randint(500,1000))

    ''' hora de hacer el gameloop '''
    running = True
    music_playing = False
    
    '''Animaciones'''
    from funciones.animations import SpriteSheet

    bug_sheet_image = pygame.image.load("assets/skins/bugs/BugSheet1.png").convert_alpha()
    jorge_sheet_image = pygame.image.load("assets/skins/Jorge/JorgeVJSheet.png").convert_alpha()
    coin_sheet_image = pygame.image.load('assets/Extras/IntroCoinsSheet.png').convert_alpha()
    sprite_sheets = [SpriteSheet(bug_sheet_image, 3, 100, 32, 32),
                    SpriteSheet(jorge_sheet_image, 2, 75, 50, 50),
                    SpriteSheet(coin_sheet_image, 8, 85, 30, 30),]

    for i in sprite_sheets:
        i.get_frames()
        i.last_update = pygame.time.get_ticks()

    frame_num = 0
    '''Control de Balas'''
    shoot_state = False

    '''Loop principal'''
    last = -5000

    while running:
        frame_num += 1
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
                if event.key == pygame.K_SPACE:
                            bullet = Bullet(player.rect.centerx + 20, player.rect.centery + 2)
                            bullets.add(bullet)
                            shoot_state = True
            elif event.type == QUIT:
                pygame.display.quit()
                pygame.quit()

            elif event.type == ADDENEMY:
                new_enemy = Enemy(SCREEN_WIDTH, SCREEN_HEIGHT, 1)
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)

            elif puntaje >= 10:
                if event.type == ADDCOIN:
                    new_coins = Coins(SCREEN_WIDTH, SCREEN_HEIGHT)
                    coins.add(new_coins)

            elif event.type == SPAWN_POWERUP_EVENT:
                spawn_power_up()

        #background scroller

        if shoot_state =="Charge":
            if now - last >= 5000:
                last = pygame.time.get_ticks()
                shoot_state = False
        for i in range(2):
            screen.blit(background_image, (i * 1000 + background_scrolls, 0))

        background_scrolls -= 2
        if abs(background_scrolls) > 1000:
            background_scrolls = 0
        
        screen.blit(opacity_surface, (0,0))
        opacity_to_screen()
        screen.blit(font.render(str(puntaje), True, (255,255, 255)), (5,-3))

        #animacion sprite sheets
        for i in sprite_sheets:
            i.animate()


        if player.is_dead:
            if frame_num % 3 == 0:
                sprite_sheets[1].screen_blit(screen, player.rect, 64)
        elif player.is_dead == False:
            sprite_sheets[1].screen_blit(screen, player.rect, 64)
        for entity in enemies:
            sprite_sheets[0].screen_blit(screen, entity.rect, entity.size)
        for coin in coins:
            sprite_sheets[2].screen_blit(screen, coin.rect, 30)
        if shoot_state == "Charge":
            if now - last <5000:
                sprite_sheets[3].screen_blit(screen,[910,40],40)
        elif shoot_state == "False":
            screen.blit(FullPNG_scaled,(910,40))
            
        #actualizar objetos
        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)

        for entity in coins:
            entity.update()
        for entity in enemies:
            score = entity.update()
            puntaje += score
        for entity in bullets:
            entity.update()
            screen.blit(entity.surf, entity.rect)
            shoot_state = entity.update()
        for entity in powerups:
            entity.update()

        #TickSearcher
        now = pygame.time.get_ticks()
        #COLLIDE DE ENEMIGOS
        if player.is_dead == False:
            if pygame.sprite.spritecollide(player, enemies, False):   
                if pygame.sprite.spritecollide(player, enemies, False, pygame.sprite.collide_mask) and player.shield == False:
                    player.is_dead = True
                    player.lives -= 1
                    hurt_sound.play()
            
        if player.lives <= 0:
            player.kill()
            death = DeathScreen(screen)
            if death == True:
                StartScene(screen)
            elif death == False:
                from .main_menu import MainMenu
                MainMenu()
        #COLLIDE DE MONEDAS 
        if pygame.sprite.spritecollide(player, coins, False):   
            if pygame.sprite.spritecollide(player, coins, True, pygame.sprite.collide_mask):
                coin_pickup.play()
                puntaje += 500
        
        #COLLIDE DE BALAS
        if pygame.sprite.groupcollide(bullets, enemies, False, False):   
            if pygame.sprite.groupcollide(bullets, enemies, True, True, pygame.sprite.collide_mask):
                puntaje += 150
                hurt_sound.play()
                shoot_state = "Charge"

        
        #COLLIDE DE POWER UPS

        if pygame.sprite.spritecollide(player, powerups, False):   
            if pygame.sprite.spritecollide(player, powerups, True, pygame.sprite.collide_mask):
                for powerup in pygame.sprite.spritecollide(player, powerups, True):
                    powerup.apply_effect(enemies.sprites(),player)
                    powerup.play_pickup()
        for powerup in powerups.sprites():
            screen.blit(powerup.image, powerup.rect)

        #DISPLAY VIDAS
        for i in range(player.lives):
            screen.blit(VidasPNG_scaled,(770 + 40*i, 40))

        
        if puntaje >= 25000:
            from .StageComplete import StageComplete
            StageComplete(screen, 2)


        pygame.display.flip()
        clock.tick(40)

        