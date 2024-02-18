import pygame

WIDTH = 1280
HEIGHT = 720

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.player_1 = pygame.image.load("../images/players/player_1.png").convert()
        self.player_2 = pygame.image.load("../images/players/player_2.png").convert()
        self.player_3 = pygame.image.load("../images/players/player_3.png").convert()
        self.player_4 = pygame.image.load("../images/players/player_4.png").convert()
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
        import bullet
        from main import bullets, all_sprites, laser_sound

        bullet = bullet.Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)
        laser_sound.play()