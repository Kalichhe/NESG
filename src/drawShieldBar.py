import pygame, random


WIDTH = 1280
HEIGHT = 720

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

def draw_shield_bar(surface, x, y, percentage):
    
    from drawText import draw_text
    from main import screen, player

    BAR_LENGHT = 100
    BAR_HEIGHT = 10
    fill = (percentage / 5) * BAR_LENGHT
    borde = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
    fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surface, GREEN, fill)
    pygame.draw.rect(surface, WHITE, borde, 2)
    draw_text(screen, str(player.shield), 20, WIDTH // 11, HEIGHT // 1000)