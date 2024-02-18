import pygame

BLACK = (0, 0, 0)

class Explosion(pygame.sprite.Sprite):
    def __init__(self, center):
        super().__init__()
        explosion_anim = self.explosion_anim()
        self.image = explosion_anim[0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50 # Velocidad de la explosion

    def explosion_anim(self):
        explosion_anims = []
        for i in range(9):
            file = "../images/explosions/regularExplosion0{}.png".format(i)
            img = pygame.image.load(file).convert()
            img.set_colorkey(BLACK)
            img_scale = pygame.transform.scale(img,(70,70))
            explosion_anims.append(img_scale)
        return explosion_anims

    def update(self):
        explosion_anim = self.explosion_anim()
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