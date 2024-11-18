import pygame
from tela import Tela

pygame.init()

tela = Tela()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        tela.menu.click(event)

    tela.mostra()
    pygame.display.flip()
    tela.clock.tick(60)

pygame.quit()
