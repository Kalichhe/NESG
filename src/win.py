import pygame
from drawText import draw_text

def Win():
    from main import clock, TRUE, WIDTH, HEIGHT, fin, screen
    screen.blit(fin, [0,0])
    draw_text(screen, "''Win''", 150, WIDTH // 2, HEIGHT // 3)
    draw_text(screen, "Que man tan maquina" , 50, WIDTH // 2, HEIGHT // 1.5)
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