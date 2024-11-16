
import pygame

class Player:
    def __init__(self, position, image_path, size=(50, 50)):
        self.position = position  
        self.image = pygame.image.load(image_path)  
        self.image = pygame.transform.scale(self.image, size)  
        self.image_rect = self.image.get_rect(topleft=position)  
        self.font = pygame.font.Font(None, 36)  
        self.speed = 5  


    def draw(self, screen, question):
        """
        Desenha o jogador na tela e exibe a pergunta abaixo dele.
        """
        screen.blit(self.image, self.image_rect)  

        
        question_surface = self.font.render(question, True, (255, 255, 255))
        question_rect = question_surface.get_rect(midtop=(self.image_rect.centerx, self.image_rect.bottom + 10))
        screen.blit(question_surface, question_rect)

    def check_collision(self, enemies):
        """
        Verifica colisão entre o jogador e os inimigos.
        """
        for enemy in enemies:
            if self.image_rect.colliderect(enemy.image_rect):
                return True  
        return False
