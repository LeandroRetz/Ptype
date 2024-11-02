import pygame
from menus import Menu
pygame.init()

class Tela:
    largura = 720
    altura = 1280
    screen = pygame.display.set_mode((altura, largura))
    clock = pygame.time.Clock()
    imagem_de_fundo = pygame.image.load("plano de fundo.png")
    pygame.transform.scale(imagem_de_fundo, (largura, altura))
    def __init__(self):
        self.menu = Menu()

    def mostra(self):
        self.screen.blit(self.imagem_de_fundo, (0, 0))
        self.menu.MostraBotao(self.screen)