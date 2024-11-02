import pygame
import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename

class Menu():
    def __init__(self):
        self.font = pygame.font.Font(None, 40)
        self.buttons = [
            {"text": "Jogar", "rect": pygame.Rect(300, 200, 350, 50), "action": self.start_game},
            {"text": "Upload de Perguntas", "rect": pygame.Rect(300, 300, 350, 50), "action": self.perguntas},
            {"text": "Sair", "rect": pygame.Rect(300, 400, 350, 50), "action": self.quit_game}
        ]

    def MostraBotao(self, surface):
        for button in self.buttons:
            pygame.draw.rect(surface, (70,82,106), button["rect"])
            text = self.font.render(button["text"], True, (255, 255, 255))
            surface.blit(text, (button["rect"].x + 50, button["rect"].y + 10))

    def click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for button in self.buttons:
                if button["rect"].collidepoint(event.pos):
                    button["action"]()

    def start_game(self):
        print("Iniciar o jogo...")

    def perguntas(self):
        root = Tk()
        root.withdraw()
        nome_arquivo = askopenfilename(title="Selecione o arquivo CSV", filetypes=[("CSV files", "*.csv")])

    def quit_game(self):
        pygame.quit()