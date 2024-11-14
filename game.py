from enemy import Enemy
import pygame

class Game:
    def __init__(self, pergunta_obj):
        self.pergunta_obj = pergunta_obj  # Instância de Pergunta para obter perguntas

    def rodajogo(self):
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        clock = pygame.time.Clock()
        screen_height = screen.get_height()
        screen_width = screen.get_width()

        enemy_image_path = "enemy.png"
        enemy_size = (50, 50)

        # Obtenha a primeira pergunta e respostas
        pergunta_data = self.pergunta_obj.get_pergunta_atual()
        pergunta_text = pergunta_data["pergunta"]
        respostas = pergunta_data["respostas"]

        enemy_left = Enemy((100, 50), respostas[0], 0.5, enemy_image_path, screen_height, size=enemy_size)
        enemy_right = Enemy((screen_width - 150, 50), respostas[1], 0.5, enemy_image_path, screen_height, size=enemy_size)

        running = True
        input_text = ""
        font = pygame.font.Font(None, 36)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:  
                        if input_text == enemy_left.text or input_text == enemy_right.text:
                            print(f"Texto correto! '{input_text}' foi digitado corretamente.")
                            self.pergunta_obj.proxima_pergunta()  # Avança para a próxima pergunta
                            pergunta_data = self.pergunta_obj.get_pergunta_atual()
                            pergunta_text = pergunta_data["pergunta"]
                            respostas = pergunta_data["respostas"]

                            # Atualiza os inimigos com novas respostas
                            enemy_left = Enemy((100, 50), respostas[0], 0.5, enemy_image_path, screen_height, size=enemy_size)
                            enemy_right = Enemy((screen_width - 150, 50), respostas[1], 0.5, enemy_image_path, screen_height, size=enemy_size)
                        input_text = ""
                    elif event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    else:
                        input_text += event.unicode

            if enemy_left.move() or enemy_right.move():
                print("Inimigos tocaram o limite inferior e serão reposicionados.")
                self.pergunta_obj.proxima_pergunta()
                pergunta_data = self.pergunta_obj.get_pergunta_atual()
                pergunta_text = pergunta_data["pergunta"]
                respostas = pergunta_data["respostas"]

                enemy_left = Enemy((100, 50), respostas[0], 0.5, enemy_image_path, screen_height, size=enemy_size)
                enemy_right = Enemy((screen_width - 150, 50), respostas[1], 0.5, enemy_image_path, screen_height, size=enemy_size)

            screen.fill((0, 0, 0))
            enemy_left.draw(screen)
            enemy_right.draw(screen)

            pergunta_surface = font.render(pergunta_text, True, (255, 255, 255))
            screen.blit(pergunta_surface, (10, 10))

            text_surface = font.render(f"Texto: {input_text}", True, (255, 255, 255))
            screen.blit(text_surface, (10, 550))

            pygame.display.flip()
            clock.tick(60)

        pygame.quit()
