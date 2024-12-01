import pygame
import random as rand
from enemy import Enemy
from player import Player

class Game:
    def __init__(self, pergunta_obj, menu):
        self.pergunta_obj = pergunta_obj
        self.menu = menu

    def spawn_new_enemies(screen_width, screen_height, enemy_image_path, respostas, size=(50, 50)):
        distancia_inimigos = rand.randint(400, 700)
        
        largura_inimigos = size[0] * 2 + distancia_inimigos
        posicao_inicial_x = (screen_width - largura_inimigos) // 2

        positions = [(posicao_inicial_x, 70), 
                     (posicao_inicial_x + size[0] + distancia_inimigos, 70)]

        enemies = [
            Enemy(position, text, 0.5, enemy_image_path, screen_height, size)
            for position, text in zip(positions, respostas)
        ]
        return enemies

    def rodar_jogo(self):
        pygame.init()

        screen = pygame.display.set_mode((1080, 720))
        clock = pygame.time.Clock()
        screen_height = screen.get_height()
        screen_width = screen.get_width()

        background_image = pygame.image.load("images/gamebackgroundimage.png")
        background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

        enemy_image_path = "images/enemy.png"
        player_image_path = "images/player.png"
        player_size = (100, 100)

        player = Player((screen_width // 2, screen_height - 100), player_image_path, size=player_size)
        player_width = player.image_rect.width
        player_x = (screen_width - player_width) // 2
        player_y = screen_height - 150
        player.image_rect.topleft = (player_x, player_y)

        pergunta_data = self.pergunta_obj.get_pergunta_atual()
        pergunta_text = pergunta_data["pergunta"]
        respostas = pergunta_data["respostas"]

        enemies = Game.spawn_new_enemies(screen_width, screen_height, enemy_image_path, respostas)

        running = True
        input_text = ""
        font = pygame.font.Font("fonts/ChicaGogoRegular.ttf", 36)
        score = 0

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if input_text == pergunta_data["certo"]:
                            print(f"Correto! '{input_text}' é a resposta certa.")
                            score += 1
                            self.pergunta_obj.proxima_pergunta()
                            pergunta_data = self.pergunta_obj.get_pergunta_atual()
                            pergunta_text = pergunta_data["pergunta"]
                            respostas = pergunta_data["respostas"]
                            enemies = Game.spawn_new_enemies(screen_width, screen_height, enemy_image_path, respostas)
                        else:
                            print(f"Incorreto! '{input_text}' não é a resposta certa.")
                        
                        input_text = ""
                    elif event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    else:
                        input_text += event.unicode

            for enemy in enemies:
                game_over_state = enemy.move()
                if game_over_state == "game_over":
                    running = False

            if player.check_collision(enemies):
                running = False

            screen.fill((0, 0, 0))
            screen.blit(background_image, (0, 0))

            for enemy in enemies:
                enemy.draw(screen)
            player.draw(screen, pergunta_text)

            input_surface = font.render(f"{input_text}", True, (255, 255, 255))
            text_width = input_surface.get_width()
            text_x = (screen.get_width() - text_width) // 2
            screen.blit(input_surface, (text_x, 500))

            score_surface = font.render(f"Score: {score}", True, (255, 255, 255))
            screen.blit(score_surface, (10, 10))

            pygame.display.flip()
            clock.tick(60)

        self.menu.game_state = "menu"
        if not self.menu.pergunta_obj.perguntas: 
            self.menu.pergunta_obj.leperguntas() 


