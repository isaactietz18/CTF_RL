import pygame

class Flag:
    def __init__(self, x, y, flag_color, size):
        self.position = pygame.Vector2(x, y)
        self.flag_color = flag_color
        self.reset_color = flag_color
        self.is_captured = False
        self.size = size
        self.team = "blue" if flag_color == (0, 0, 200) else "red"
    
    def draw(self, screen):
        flag_rect = pygame.Rect(self.position.x, self.position.y, self.size, self.size)
        pygame.draw.rect(screen, self.flag_color, flag_rect)
    
    def capture(self):
        self.is_captured = True
        self.flag_color = (0, 0, 0)
    
    def reset(self):
        self.is_captured = False
        self.flag_color = self.reset_color