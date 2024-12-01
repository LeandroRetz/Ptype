
import pygame
from menus import Menu
pygame.init()

class Tela:
    altura = 1080
    largura = 720
    screen = pygame.display.set_mode((altura, largura))
    clock = pygame.time.Clock()
    imagem_de_fundo = pygame.image.load("images/backgroundimage.png")
    pygame.transform.scale(imagem_de_fundo, (largura, altura))

    def __init__(self):
        self.menu = Menu()

    def mostra(self):
        if self.menu.game_state == "menu":
            self.mostraMenu()
        elif self.menu.game_state == "game":
            self.mostraJogo()

    def mostraMenu(self):
        self.screen.blit(self.imagem_de_fundo, (0, 0))
        self.menu.mostrar_botoes(self.screen)