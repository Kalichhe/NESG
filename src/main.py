from pickle import TRUE  # This is activated, when the game is initialized
import pygame
from player import Player
from meteor import Meteor
from drawShieldBar import draw_shield_bar
from explosion import Explosion
from drawText import draw_text
from end import End
from showGoScreen import GoScreen
from win import Win
from pygame.locals import KEYDOWN, K_ESCAPE, QUIT

WIDTH = 1280
HEIGHT = 720

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Class instance
GoScreen = GoScreen()


pygame.init()  # Inicializa pygame
pygame.mixer.init()  # Inicializa el sonido para el juego
screen = pygame.display.set_mode(
    (WIDTH, HEIGHT)
)  # Creamos una ventana donde esta nuestro juego
pygame.display.set_caption(
    "Navecita Espacial Super Galáctica"
)  # Le colocamos un titulo al juego
clock = pygame.time.Clock()  # Creamos un reloj para controlar los fps


# Wallpapers
background = pygame.image.load("../images/images/background.jpg").convert()
principal = pygame.image.load("../images/images/principal.jpg").convert()
fin = pygame.image.load("../images/images/fin.jpg").convert()
next_level = pygame.image.load("../images/images/next_level.jpg").convert()

# Load sounds
laser_sound = pygame.mixer.Sound("../sounds/sfx_laser1.ogg")
explosion_sound = pygame.mixer.Sound("../sounds/explosion.wav")
fondo = pygame.mixer.Sound("../sounds/fondo.mp3")
pantalla_inicial = pygame.mixer.Sound("../sounds/music.ogg")
victory = pygame.mixer.Sound("../sounds/victory.wav")

# Game Over
game_over = True

running = True

while running:
    
    if game_over:

        pygame.mixer.music.load("../sounds/music.ogg")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(loops=-1)

        GoScreen.show_go_screen()

        game_over = False
        pygame.mixer.music.load("../sounds/fondo.mp3")
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(loops=-1)

        all_sprites = pygame.sprite.Group()
        meteor_list = pygame.sprite.Group()
        bullets = pygame.sprite.Group()

        player = Player()
        all_sprites.add(player)
        for i in range(8):
            meteor = Meteor()
            all_sprites.add(meteor)
            meteor_list.add(meteor)

        score = 0

    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    all_sprites.update()

    # Collisions
    hits = pygame.sprite.groupcollide(meteor_list, bullets, True, True)
    for hit in hits:
        score += 1
        explosion_sound.play()
        explosion = Explosion(hit.rect.center)
        all_sprites.add(explosion)
        meteor = Meteor()
        all_sprites.add(meteor)
        meteor_list.add(meteor)

        if score == 100:
            game_over = True
            Win()
        elif score % 20 == 0:
            player.shield += 1
            victory.play()
            if player.shield > 5:
                player.shield = 5

    hits = pygame.sprite.spritecollide(player, meteor_list, True)
    for hit in hits:
        player.shield -= 1
        meteor = Meteor()
        all_sprites.add(meteor)
        meteor_list.add(meteor)
        if player.shield <= 0:
            explosion_sound.play()
            game_over = True
            End()

    screen.blit(background, [0, 0])

    all_sprites.draw(screen)

    # Marcador
    draw_text(screen, str(score), 25, WIDTH // 2, 10)

    # Vida

    draw_shield_bar(screen, 5, 5, player.shield)

    pygame.display.flip()

pygame.quit()
