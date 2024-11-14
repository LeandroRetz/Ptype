from game import Game
import pygame
from pergunta import Pergunta

class Menu():
    def __init__(self):
        self.font = pygame.font.Font(None, 40)
        self.buttons = [
            {"text": "Jogar", "rect": pygame.Rect(300, 200, 350, 50), "action": self.start_game},
            {"text": "Upload de Perguntas", "rect": pygame.Rect(300, 300, 350, 50), "action": self.perguntas},
            {"text": "Sair", "rect": pygame.Rect(300, 400, 350, 50), "action": self.quit_game}
        ]
        self.game_state = "menu"

    def MostraBotao(self, surface):
        for button in self.buttons:
            pygame.draw.rect(surface, (70, 82, 106), button["rect"])
            text = self.font.render(button["text"], True, (255, 255, 255))
            surface.blit(text, (button["rect"].x + 50, button["rect"].y + 10))

    def click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for button in self.buttons:
                if button["rect"].collidepoint(event.pos):
                    button["action"]()

    def perguntas(self):
        arquivoperguntas = Pergunta()
        arquivoperguntas.leperguntas()
        return True

    def start_game(self):
        self.game_state = "game"
        game = Game()
        game.rodajogo()
        


    def quit_game(self):
        pygame.quit()
        exit()
