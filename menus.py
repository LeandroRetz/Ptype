import pygame
from game import Game
from pergunta import Pergunta

class Menu:
    def __init__(self):
        self.font = pygame.font.Font("fonts/ChicaGogoRegular.ttf", 40)
        self.pergunta_obj = Pergunta()
        self.buttons = [
            {"text": "Jogar", "rect": pygame.Rect(438, 413, 202, 40), "action": self.start_game},
            {"text": "Upload de Perguntas", "rect": pygame.Rect(346, 494, 385, 40), "action": self.perguntas},
            {"text": "Sair", "rect": pygame.Rect(505, 575, 68, 30), "action": self.quit_game}
        ]
        self.game_state = "menu"

    pygame.mixer.init()
    pygame.mixer.music.load("audio/BackgroundMusic.mp3")
    pygame.mixer.music.play(loops=-1, start=0.0)


    def mostrar_botoes(self, surface):
        for button in self.buttons:
            pass

    def click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for button in self.buttons:
                if button["rect"].collidepoint(event.pos):
                    button["action"]()

    def perguntas(self):
        self.pergunta_obj.leperguntas()

    def start_game(self):
        self.game_state = "game"
        game = Game(self.pergunta_obj, self)
        game.rodar_jogo()

    def quit_game(self):
        pygame.quit()
        exit()
