import pygame
from drawText import draw_text

def End():
    from main import clock, TRUE, WIDTH, HEIGHT, fin, screen
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