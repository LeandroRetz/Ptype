import pygame
from enemy import Enemy
from player import Player

class Game:
    def __init__(self, pergunta_obj):
        self.pergunta_obj = pergunta_obj  # Instância de Pergunta para obter perguntas

    def rodajogo(self):
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        clock = pygame.time.Clock()
        screen_height = screen.get_height()
        screen_width = screen.get_width()

        # Carregar recursos
        enemy_image_path = "enemy.png"
        player_image_path = "enemy.png"
        enemy_size = (50, 50)
        player_size = (50, 50)

        # Inicializar jogador
        player = Player((screen_width // 2, screen_height - 100), player_image_path, size=player_size)

        # Obter a primeira pergunta e respostas
        pergunta_data = self.pergunta_obj.get_pergunta_atual()
        pergunta_text = pergunta_data["pergunta"]
        respostas = pergunta_data["respostas"]

        # Inicializar inimigos
        enemy_left = Enemy((100, 50), respostas[0], 0.5, enemy_image_path, screen_height, size=enemy_size)
        enemy_right = Enemy((screen_width - 150, 50), respostas[1], 0.5, enemy_image_path, screen_height, size=enemy_size)
        enemies = [enemy_left, enemy_right]

        running = True
        input_text = ""
        font = pygame.font.Font(None, 36)

        while running:
            keys = pygame.key.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if input_text in [enemy.text for enemy in enemies]:
                            print(f"Texto correto! \'{input_text}\' foi digitado corretamente.")
                            self.pergunta_obj.proxima_pergunta()
                            pergunta_data = self.pergunta_obj.get_pergunta_atual()
                            pergunta_text = pergunta_data["pergunta"]
                            respostas = pergunta_data["respostas"]

                            # Atualizar inimigos com novas respostas
                            enemies[0] = Enemy((100, 50), respostas[0], 0.5, enemy_image_path, screen_height, size=enemy_size)
                            enemies[1] = Enemy((screen_width - 150, 50), respostas[1], 0.5, enemy_image_path, screen_height, size=enemy_size)
                        input_text = ""
                    elif event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    else:
                        input_text += event.unicode

            # Movimento dos inimigos e verificação de colisões
            for enemy in enemies:
                if enemy.move():
                    print("Inimigo atingiu o limite inferior.")
                    running = False

            if player.check_collision(enemies):
                print("Jogador colidiu com um inimigo! Fim de jogo.")
                running = False

            # Desenhar a tela
            screen.fill((0, 0, 0))
            for enemy in enemies:
                enemy.draw(screen)
            player.draw(screen, pergunta_text)

            # Exibir texto de entrada
            input_surface = font.render(f"Entrada: {input_text}", True, (255, 255, 255))
            screen.blit(input_surface, (10, 550))

            pygame.display.flip()
            clock.tick(60)

        pygame.quit()
