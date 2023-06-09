import pygame

class Player:
    def __init__(self, x, y, color, speed, radius, team):
        self.position = pygame.Vector2(x, y)
        self.radius = radius
        self.color = color
        self.speed = speed
        self.is_alive = True
        self.team = team
        self.captured_flag = None
    
    def update(self, keys, walls, flags, scoreboard):
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
        
        # Normalize and scale by speed
        if direction.length() > 0:
            direction.normalize_ip()
            direction *= self.speed
            self.position += direction
        
        # Collide with walls
        for wall in walls:
            if self.collide(wall):
                self.position = self.prev_position
                break
        
        # Capture flags
        for flag in flags:
            self.capture_flag(flag)
            self.score(flag, scoreboard)
    
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
    
    def capture_flag(self, flag):
        # Capture flag if touching, not captured, on opposite team
        if self.collide_flag(flag) and not flag.is_captured and self.team != flag.team:
            flag.capture()
            self.captured_flag = flag
            print(f"I captured the {flag.team} flag!")
    
    def collide_flag(self, flag):
        # Collide if the edge of the circle is within the flag
        if flag.position.x < self.position.x + self.radius and flag.position.x + flag.size > self.position.x - self.radius:
            if flag.position.y < self.position.y + self.radius and flag.position.y + flag.size > self.position.y - self.radius:
                return True
        return False
    
    def score(self, flag, scoreboard):
        # Score if touching home platform and has flag and on same team, reset flag
        if self.collide_flag(flag) and self.captured_flag != None and self.team == flag.team:
            self.captured_flag.reset()
            self.captured_flag = None
            print("I scored!")
            scoreboard.update(self.team)