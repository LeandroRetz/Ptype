import pygame
pygame.init()

class Tela:
    largura = 720
    altura = 1280
    screen = pygame.display.set_mode((altura, largura))
    clock = pygame.time.Clock()
    imagem_de_fundo = pygame.image.load("plano de fundo.png")
    pygame.transform.scale(imagem_de_fundo, (largura, altura))