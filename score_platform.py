# A class for a platform that will exist in the fort to act as a place to capture the enemy flag.
# If a player is touching the platform and has the enemy flag, they will score a point.
import pygame

class Platform:
    def __init__(self, x, y, width, height, team):
        self.rect = pygame.Rect(x, y, width, height)
        self.team = team
        self.color = (255, 255, 255)
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
