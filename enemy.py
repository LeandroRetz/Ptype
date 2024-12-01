import pygame

class Enemy:
    def __init__(self, position, text, speed, image_path, screen_height, size=(50, 50)):
        self.position = position
        self.text = text
        self.speed = speed
        self.screen_height = screen_height
        
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, size)
        self.image_rect = self.image.get_rect(topleft=position)
        
        self.font = pygame.font.Font("fonts/ChicaGogoRegular.ttf", 36)
        self.touched_bottom = False

    def move(self):
        self.position = (self.position[0], self.position[1] + self.speed)
        self.image_rect.topleft = self.position
        if self.image_rect.bottom >= self.screen_height and not self.touched_bottom:
            self.touched_bottom = True
            return "game_over"
        return False

    def draw(self, screen):
        screen.blit(self.image, self.image_rect)
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.image_rect.centerx, self.image_rect.top - 20))
        screen.blit(text_surface, text_rect)
