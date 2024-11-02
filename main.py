from tela import Tela
import pygame

pygame.init()

tela = Tela()
running = True
while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        tela.screen.fill("purple")

        pygame.display.flip()

        tela.clock.tick(60)

pygame.quit()