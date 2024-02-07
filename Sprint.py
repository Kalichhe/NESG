
#from cProfile import run
from pickle import TRUE
#from re import S
from sys import platlibdir
from tkinter import CENTER, W, font
from turtle import Screen
from xmlrpc.client import TRANSPORT_ERROR
import pygame, random


WIDTH = 1280
HEIGHT = 720

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

pygame.init() # Inicializa pygame
pygame.mixer.init() # Inicializa el sonido para el juego
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Creamos una ventana donde esta nuestro juego  
pygame.display.set_caption("Navecita Espacial Super Galáctica") # Le colocamos un titulo al juego 
clock = pygame.time.Clock() # Creamos un reloj para controlar los fps

def draw_text(surface, text, size, x, y):
    font = pygame.font.SysFont("serif", size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)

def draw_shield_bar(surface, x, y, percentage):
    
    BAR_LENGHT = 100
    BAR_HEIGHT = 10
    fill = (percentage / 5) * BAR_LENGHT
    borde = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
    fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surface, GREEN, fill)
    pygame.draw.rect(surface, WHITE, borde, 2)
    draw_text(screen, str(player.shield), 20, WIDTH // 11, HEIGHT // 1000)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.player_1 = pygame.image.load("assets/player_1.png").convert()
        self.player_2 = pygame.image.load("assets/player_2.png").convert()
        self.player_3 = pygame.image.load("assets/player_3.png").convert()
        self.player_4 = pygame.image.load("assets/player_4.png").convert()
        while True:
            try:
                self.image = int(input("Ingresa el jugador que quieras usar: 1, 2, 3, 4: ")) #pygame.image.load("assets/Jugador.png").convert()
                if self.image == 1:
                    self.image = self.player_1
                    break
                elif self.image == 2:
                    self.image = self.player_2
                    break
                elif self.image == 3:
                    self.image = self.player_3
                    break
                elif self.image == 4:
                    self.image = self.player_4
                    break
                elif self.image != 1 or self.image != 2 or self.image != 3 or self.image != 4:
                    print("------------------------")
                    print("Ingresa un numero valido")
                    print("------------------------")
                
            except (AttributeError, ValueError):
                print("------------------------")
                print("Ingresa un numero valido")
                print("------------------------")

        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 10
        self.speed_x = 0
        self.speed_y = 0
        self.shield = 5
    
    def update(self):
        self.speed_x = 0
        self.speed_y = 0 
         
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speed_x = -8
        if keystate[pygame.K_RIGHT]:
            self.speed_x = 8
        self.rect.x += self.speed_x

        if keystate[pygame.K_UP]:
            self.speed_y = -8
        if keystate[pygame.K_DOWN]:
            self.speed_y = 8
        self.rect.y += self.speed_y
        
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0
 
    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)
        laser_sound.play()

class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = random.choice(meteor_images)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-140, -100)
        self.speedy = random.randrange(1, 10)
        self.speedx = random.randrange(-5, 5)

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 25:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 10)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/laserBlue06.png")
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.centerx = x
        self.speedy = -10
    
    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()

class Explosion(pygame.sprite.Sprite):
    def __init__(self, center):
        super().__init__()
        self.image = explosion_anim[0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50 # Velocidad de la explosion

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

def show_go_screen():
    screen.blit(principal, [0,0])
    draw_text(screen, "Navecita Espacial Super Galáctica", 70, WIDTH // 2, HEIGHT // 8)
    draw_text(screen, "Presiona una tecla para jugar", 40, WIDTH // 2, HEIGHT // 3)
    draw_text(screen, "Historia", 30, WIDTH // 2, HEIGHT // 2)
    draw_text(screen, "Erase una vez una navecita espacial super galáctica, que viajaba por el espacio, ", 20, WIDTH // 2, HEIGHT // 1.8)
    draw_text(screen, "destruyendo meteoritos para no ser destruida, y poder sobrevivir por mucho más tiempo con el fin de poder volver a casa y ver a sus hijos y esposa.", 20, WIDTH // 2, HEIGHT // 1.7)
    draw_text(screen, "::Presiona cualquier tecla y dirigete a la terminal::", 40, WIDTH // 2, HEIGHT // 1.3)
    pygame.display.flip()
    waiting = TRUE
    while waiting:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False

def End():
    screen.blit(fin, [0,0])
    draw_text(screen, "Game Over", 150, WIDTH // 2, HEIGHT // 3)
    draw_text(screen, "Iniciar Una Nueva Partida" , 50, WIDTH // 2, HEIGHT // 1.5)
    draw_text(screen, "Presione Una Tecla Para Iniciar", 30, WIDTH // 2, HEIGHT // 1.3)
    pygame.display.flip()
    waiting = TRUE
    while waiting:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False

meteor_images = []
meteor_list = ["assets/meteorBrown_big1.png", "assets/meteorBrown_big2.png", "assets/meteorBrown_big3.png", "assets/meteorBrown_big4.png", "assets/meteorBrown_med1.png", "assets/meteorBrown_med3.png", "assets/meteorBrown_small1.png", "assets/meteorBrown_small2.png", "assets/meteorBrown_tiny1.png", "assets/meteorBrown_tiny2.png"]
#
for img in meteor_list:
    meteor_images.append(pygame.image.load(img).convert())

# Explosion
explosion_anim = []
for i in range(9):
    file = "assets/regularExplosion0{}.png".format(i)
    img = pygame.image.load(file).convert()
    img.set_colorkey(BLACK)
    img_scale = pygame.transform.scale(img,(70,70))
    explosion_anim.append(img_scale)

# Fondos
background = pygame.image.load("assets/background.jpg").convert()
principal = pygame.image.load("assets/principal.jpg").convert()
fin = pygame.image.load("assets/fin.jpg").convert()
next_level = pygame.image.load("assets/next_level.jpg").convert()

# Cargar sonidos
laser_sound = pygame.mixer.Sound("assets/sfx_laser1.ogg")
explosion_sound = pygame.mixer.Sound("assets/explosion.wav")
fondo = pygame.mixer.Sound("assets/fondo.mp3")
pantalla_inicial = pygame.mixer.Sound("assets/music.ogg")
victory = pygame.mixer.Sound("assets/victory.wav")

#Game Over
game_over = True

running = True

while running:
    
    if game_over:

        pygame.mixer.music.load("assets/music.ogg")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(loops=-1)
        
        show_go_screen()

        game_over = False 
        pygame.mixer.music.load("assets/fondo.mp3")
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

    # Colisiones
    hits = pygame.sprite.groupcollide(meteor_list, bullets, True, True)
    for hit in hits:
         score += 1
         explosion_sound.play()
         explosion = Explosion(hit.rect.center)
         all_sprites.add(explosion)
         meteor = Meteor()
         all_sprites.add(meteor)
         meteor_list.add(meteor)
         if score % 20 == 0:
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
    draw_text(screen, str(score  ), 25, WIDTH // 2, 10)

    # Vida

    draw_shield_bar(screen, 5, 5, player.shield)

    pygame.display.flip()


pygame.quit()
