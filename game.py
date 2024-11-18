import pygame
from enemy import Enemy
from player import Player

class Game:
    def __init__(self, pergunta_obj):
        self.pergunta_obj = pergunta_obj

    def spawn_new_enemies(screen_width, screen_height, enemy_image_path, respostas, size=(50, 50)):
        positions = [(100, 50), (screen_width - 150, 50)]
        enemies = [
            Enemy(position, text, 0.5, enemy_image_path, screen_height, size)
            for position, text in zip(positions, respostas)
        ]
        return enemies

    def rodar_jogo(self):
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        clock = pygame.time.Clock()
        screen_height = screen.get_height()
        screen_width = screen.get_width()

        enemy_image_path = "enemy.png"
        player_image_path = "enemy.png"
        player_size = (50, 50)
        player = Player((screen_width // 2, screen_height - 100), player_image_path, size=player_size)

        pergunta_data = self.pergunta_obj.get_pergunta_atual()
        pergunta_text = pergunta_data["pergunta"]
        respostas = pergunta_data["respostas"]

        # Chamando o método estático diretamente pela classe
        enemies = Game.spawn_new_enemies(screen_width, screen_height, enemy_image_path, respostas)

        running = True
        input_text = ""
        font = pygame.font.Font(None, 36)
        speed_multiplier = 1.0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if input_text == pergunta_data["certo"]: 
                            print(f"Correto! '{input_text}' é a resposta certa.")
                            self.pergunta_obj.proxima_pergunta()
                            pergunta_data = self.pergunta_obj.get_pergunta_atual()
                            pergunta_text = pergunta_data["pergunta"]
                            respostas = pergunta_data["respostas"]
                            speed_multiplier += 0.5
                        
                            # Gera novos inimigos com a velocidade aumentada
                            enemies = Game.spawn_new_enemies(
                                screen_width, 
                                screen_height, 
                                enemy_image_path, 
                                respostas
                            )
                            for enemy in enemies:
                                enemy.speed *= speed_multiplier
                        else:
                            print(f"Incorreto! '{input_text}' não é a resposta certa.")
                        
                        input_text = ""
                    elif event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    else:
                        input_text += event.unicode

            for enemy in enemies:
                if enemy.move():
                    running = False

            if player.check_collision(enemies):
                running = False

            screen.fill((0, 0, 0))
            for enemy in enemies:
                enemy.draw(screen)
            player.draw(screen, pergunta_text)

            input_surface = font.render(f"Entrada: {input_text}", True, (255, 255, 255))
            screen.blit(input_surface, (10, 550))

            pygame.display.flip()
            clock.tick(60)

        pygame.quit()


