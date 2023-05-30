import pygame

class Flag:
    def __init__(self, x, y, flag_color, size):
        self.position = pygame.Vector2(x, y)
        self.flag_color = flag_color
        self.is_captured = False
        self.size = size
    
    def draw(self, screen):
        flag_rect = pygame.Rect(self.position.x, self.position.y, self.size, self.size)
        pygame.draw.rect(screen, self.flag_color, flag_rect)