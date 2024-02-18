import pygame


class GoScreen:
    def __init__(self):
        self.WIDTH = 1280
        self.HEIGHT = 720

    def show_go_screen(self):
        from drawText import draw_text
        from main import screen, clock, principal, TRUE 
        
        input_text = ""
        font = pygame.font.Font(None, 32)

        screen.blit(principal, [0,0])
        draw_text(screen, "Navecita Espacial Super Galáctica", 70, self.WIDTH // 2, self.HEIGHT // 8)
        draw_text(screen, "Presiona una tecla para jugar", 40, self.WIDTH // 2, self.HEIGHT // 3)
        draw_text(screen, "Historia", 30, self.WIDTH // 2, self.HEIGHT // 2)
        draw_text(screen, "Erase una vez una navecita espacial super galáctica, que viajaba por el espacio, ", 20, self.WIDTH // 2, self.HEIGHT // 1.8)
        draw_text(screen, "destruyendo meteoritos para no ser destruida, y poder sobrevivir por mucho más tiempo con el fin de poder volver a casa y ver a sus hijos y esposa.", 20, self.WIDTH // 2, self.HEIGHT // 1.7)
        draw_text(screen, "::Presiona cualquier tecla y dirigete a la terminal::", 40, self.WIDTH // 2, self.HEIGHT // 1.3)
        pygame.display.flip()
        waiting = TRUE
        while waiting:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYUP:
                    waiting = False
            pygame.display.flip()


