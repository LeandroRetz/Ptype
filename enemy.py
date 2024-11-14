'''
Classe Enemy criada e implementada dentro do arquivo enemy.py. Precisa implementar ela na main em conjunto com o restante.
Creio que dá pra ter uma ideia da coisa inicial.
'''

import pygame

class Enemy:
    def __init__(self, position, text, speed, image_path, screen_height, size=(50, 50)):
        self.position = position  # (x, y) para a posição inicial do inimigo
        self.text = text  # Texto no inimigo, para as alternativas
        self.speed = speed  # Velocidade de movimento do inimigo
        self.screen_height = screen_height  # Altura pra verificar colisão
        
        self.image = pygame.image.load(image_path) # Carrega a imagem do inimigo
        self.image = pygame.transform.scale(self.image, size) # Ajusta o tamanho da imagem
        self.image_rect = self.image.get_rect(topleft=position) # 
        
        self.font = pygame.font.Font(None, 36)  # Define uma fonte padrão para o texto
        self.touched_bottom = False  # Atributo para registrar se tocou o limite inferior

    def move(self): # Movimenta o inimigo em direção a parte inferior da tela, verifica se a tocou.
        self.position = (self.position[0], self.position[1] + self.speed)  # Move o inimigo para baixo
        self.image_rect.topleft = self.position  # Atualiza a posição do retângulo da imagem

        # Verifica se o inimigo tocou o final da tela
        if self.image_rect.bottom >= self.screen_height and not self.touched_bottom:
            self.touched_bottom = True  # Marca que tocou o limite
            return True  # Retorna True para indicar que o inimigo tocou o limite da tela

        return False

    def draw(self, screen): # Renderiza o inimigo
        screen.blit(self.image, self.image_rect) # Desenha a imagem do inimigo

        text_surface = self.font.render(self.text, True, (255, 255, 255))   # Renderiza o texto acima do inimigo
        
        # Calcula a posição do texto para que fique acima do inimigo
        text_rect = text_surface.get_rect(center=(self.image_rect.centerx, self.image_rect.top - 20)) 
        screen.blit(text_surface, text_rect)

    def spawn_new_enemies(screen_width, screen_height, enemy_image_path, size=(50, 50)):
        enemy_left_position = (100, 50)
        enemy_right_position = (screen_width - 150, 50)

        texts = ["Censo", "Senso"]
        
        # Criação dos inimigos
        enemy_left = Enemy(enemy_left_position, texts[0], 0.5, enemy_image_path, screen_height, size)
        enemy_right = Enemy(enemy_right_position, texts[1], 0.5, enemy_image_path, screen_height, size)
        
        return enemy_left, enemy_right

"""
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
screen_height = screen.get_height()
screen_width = screen.get_width()

enemy_image_path = "enemy.png"
enemy_size = (50, 50)

enemy_left, enemy_right = spawn_new_enemies(screen_width, screen_height, enemy_image_path, size=enemy_size)

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

                    enemy_left, enemy_right = spawn_new_enemies(screen_width, screen_height, enemy_image_path, size=enemy_size)
                input_text = ""  
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode  


    if enemy_left.move() or enemy_right.move():
        print("Inimigos tocaram o limite inferior e serão reposicionados.")

        enemy_left, enemy_right = spawn_new_enemies(screen_width, screen_height, enemy_image_path, size=enemy_size)


    screen.fill((0, 0, 0))  
    enemy_left.draw(screen)  
    enemy_right.draw(screen)  


    text_surface = font.render(f"Texto: {input_text}", True, (255, 255, 255))
    screen.blit(text_surface, (10, 550))

    pygame.display.flip()  
    clock.tick(60)  


pygame.quit()
"""