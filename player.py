import pygame

class Player:
    def __init__(self, x, y, color, speed, radius):
        self.position = pygame.Vector2(x, y)
        self.radius = radius
        self.color = color
        self.speed = speed
        self.is_alive = True
    
    def update(self, keys, walls):
        self.prev_position = self.position.copy()
        direction = pygame.Vector2(0, 0) 

        # Key Presses
        if keys[pygame.K_w]:
            direction += pygame.Vector2(0, -1)
        if keys[pygame.K_a]:
            direction += pygame.Vector2(-1, 0)
        if keys[pygame.K_s]:
            direction += pygame.Vector2(0, 1)
        if keys[pygame.K_d]:
            direction += pygame.Vector2(1, 0)

        if direction.length() > 0:
            direction.normalize_ip()
            direction *= self.speed
            self.position += direction
        
        for wall in walls:
            if self.collide(wall):
                self.position = self.prev_position
                break
    
    def collide(self, wall):
        # Collide if the edge of the circle is within the wall
        if wall.rect.collidepoint(self.position + pygame.Vector2(self.radius, 0)):
            return True
        if wall.rect.collidepoint(self.position + pygame.Vector2(-self.radius, 0)):
            return True
        if wall.rect.collidepoint(self.position + pygame.Vector2(0, self.radius)):
            return True
        if wall.rect.collidepoint(self.position + pygame.Vector2(0, -self.radius)):
            return True
        return False
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius)