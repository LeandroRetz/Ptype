from tela import Tela
import pygame
from game import Game
pygame.init()

tela = Tela()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        tela.menu.click(event)

    if tela.menu.game_state == "menu":
        tela.mostraMenu()
    elif tela.menu.game_state == "game":
        Game.rodajogo()
        tela.menu.game_state = "menu"    
    
    pygame.display.flip()
    tela.clock.tick(60)

pygame.quit()
