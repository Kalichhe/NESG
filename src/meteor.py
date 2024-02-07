import pygame, random

WIDTH = 1280
HEIGHT = 720

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.load_images()  # Cargar las imágenes de los meteoritos
        self.image = random.choice(self.meteor_images)  # Elegir una imagen al azar
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-140, -100)
        self.speedy = random.randrange(1, 10)
        self.speedx = random.randrange(-5, 5)
        
    def load_images(self):
        self.meteor_images = []
        meteor_list = ["../images/meteorBrown_big1.png",
                        "../images/meteorBrown_big2.png",
                        "../images/meteorBrown_big3.png",
                        "../images/meteorBrown_big4.png",
                        "../images/meteorBrown_med1.png",
                        "../images/meteorBrown_med3.png",
                        "../images/meteorBrown_small1.png",
                        "../images/meteorBrown_small2.png",
                        "../images/meteorBrown_tiny1.png",
                        "../images/meteorBrown_tiny2.png"
                        ]
        for img in meteor_list:
            self.meteor_images.append(pygame.image.load(img).convert())

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 25:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 10)
            