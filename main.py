import pygame
from wall import Wall
from player import Player

pygame.init()

# Constants
WIDTH = 1280
HEIGHT = 720

# Game Window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Capture the Flag Reinforcement Learning")

# Fort Variables
FORT_WIDTH = 100
FORT_HEIGHT = 200
blue_fort_x = 0
blue_fort_y = (HEIGHT - FORT_HEIGHT) // 2
red_fort_x = WIDTH - FORT_WIDTH
red_fort_y = (HEIGHT - FORT_HEIGHT) // 2

# Border Walls
wall_width = 10
wall_color = (255, 255, 255)
walls = [
    Wall(0, 0, WIDTH, wall_width, wall_color), # Top
    Wall(0, 0, wall_width, HEIGHT, wall_color), # Left
    Wall(0, HEIGHT - wall_width, WIDTH, wall_width, wall_color), # Bottom
    Wall(WIDTH - wall_width, 0, wall_width, HEIGHT, wall_color) # Right
]

# Player Variables
player_x = WIDTH // 2
player_y = HEIGHT // 2
player_radius = 10
player_speed = .3
player_color = (0, 255, 0)
player = Player(player_x, player_y, player_color, player_speed, player_radius)

# Game Loop
running = True
while running:
    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Game Logic Update
    # Key Presses
    keys = pygame.key.get_pressed()
    # Quit
    if keys[pygame.K_ESCAPE]:
        running = False

    # Player Update
    player.update(keys, walls)
    
    # Draw Game Objects
    # Background
    window.fill((0, 0, 0))

    # Forts
    pygame.draw.rect(window, (0, 0, 255), (blue_fort_x, blue_fort_y, FORT_WIDTH, FORT_HEIGHT))
    pygame.draw.rect(window, (255, 0, 0), (red_fort_x, red_fort_y, FORT_WIDTH, FORT_HEIGHT))

    # Walls
    for wall in walls:
        wall.draw(window)
    
    # Player
    player.draw(window)

    # Update Display
    pygame.display.update()

pygame.quit()