# Scoreboard for RLCTF that shows the current standings of the teams
import pygame

class Scoreboard:
    def __init__(self):
        self.blue_score = 0
        self.red_score = 0
        self.font = pygame.font.SysFont("Arial", 30)
    
    def update(self, team):
        if team == "blue":
            self.blue_score += 1
        elif team == "red":
            self.red_score += 1
    
    def draw(self, screen):
        blue_score_text = self.font.render("Blue: " + str(self.blue_score), True, (255, 255, 255))
        red_score_text = self.font.render("Red: " + str(self.red_score), True, (255, 255, 255))
        screen.blit(blue_score_text, (10, 10))
        screen.blit(red_score_text, (10, 40))
    
    def reset(self):
        self.blue_score = 0
        self.red_score = 0