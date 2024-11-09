
import pygame
from menus import Menu
pygame.init()

class Tela:
    altura = 1080
    largura = 720
    screen = pygame.display.set_mode((altura, largura))
    clock = pygame.time.Clock()
    imagem_de_fundo = pygame.image.load("plano de fundo.png")
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
        self.menu.MostraBotao(self.screen)

    def mostraJogo(self):
        self.screen.blit(self.imagem_de_fundo, (0, 0))
        font = pygame.font.Font(None, 50)
        text = font.render("Tela do Jogo", True, (255, 255, 255))
        self.screen.blit(text, (300, 250))
