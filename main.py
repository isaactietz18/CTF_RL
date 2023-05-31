import pygame
from wall import Wall
from player import Player
from flag import Flag

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

# Blue Fort Walls with an entrance on the right
blue_fort_walls = [
    Wall(blue_fort_x, blue_fort_y, FORT_WIDTH, 10, (255, 255, 255)), # Top
    Wall(blue_fort_x, blue_fort_y, 10, FORT_HEIGHT, (255, 255, 255)), # Left
    Wall(blue_fort_x, blue_fort_y + FORT_HEIGHT - 10, FORT_WIDTH, 10, (255, 255, 255)), # Bottom
    Wall(blue_fort_x + FORT_WIDTH - 10, blue_fort_y, 10, FORT_HEIGHT // 3, (255, 255, 255)), # Right Top
    Wall(blue_fort_x + FORT_WIDTH - 10, blue_fort_y + FORT_HEIGHT // 3 * 2, 10, FORT_HEIGHT // 3, (255, 255, 255)), # Right Bottom
]

# Red Fort Walls with an entrance on the left
red_fort_walls = [
    Wall(red_fort_x, red_fort_y, FORT_WIDTH, 10, (255, 255, 255)), # Top
    Wall(red_fort_x, red_fort_y, 10, FORT_HEIGHT // 3, (255, 255, 255)), # Left Top
    Wall(red_fort_x, red_fort_y + FORT_HEIGHT // 3 * 2, 10, FORT_HEIGHT // 3, (255, 255, 255)), # Left Bottom
    Wall(red_fort_x, red_fort_y + FORT_HEIGHT - 10, FORT_WIDTH, 10, (255, 255, 255)), # Bottom
    Wall(red_fort_x + FORT_WIDTH - 10, red_fort_y, 10, FORT_HEIGHT, (255, 255, 255)), # Right
]

# Border Walls
wall_width = 10
wall_color = (255, 255, 255)
walls = [
    Wall(0, 0, WIDTH, wall_width, wall_color), # Top
    Wall(0, 0, wall_width, HEIGHT, wall_color), # Left
    Wall(0, HEIGHT - wall_width, WIDTH, wall_width, wall_color), # Bottom
    Wall(WIDTH - wall_width, 0, wall_width, HEIGHT, wall_color) # Right
]

# Flag Variables
flag_size = 20
blue_flag_x = blue_fort_x + FORT_WIDTH // 2 - flag_size // 2
blue_flag_y = blue_fort_y + FORT_HEIGHT // 2 - flag_size // 2
blue_flag_color = (0, 0, 200)
blue_flag = Flag(blue_flag_x, blue_flag_y, blue_flag_color, flag_size)

red_flag_x = red_fort_x + FORT_WIDTH // 2 - flag_size // 2
red_flag_y = red_fort_y + FORT_HEIGHT // 2 - flag_size // 2
red_flag_color = (200, 0, 0)
red_flag = Flag(red_flag_x, red_flag_y, red_flag_color, flag_size)

# Player Variables
player_x = WIDTH // 2
player_y = HEIGHT // 2
player_radius = 10
player_speed = .3
red_color = (200, 100, 100)
blue_color = (100, 100, 200)
blue_player_one = Player(player_x, player_y, blue_color, player_speed, player_radius, "blue")

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
    blue_player_one.update(keys, walls + blue_fort_walls + red_fort_walls, [blue_flag, red_flag])
    
    # Draw Game Objects
    # Background
    window.fill((0, 0, 0))

    # Forts
    pygame.draw.rect(window, (0, 0, 255), (blue_fort_x, blue_fort_y, FORT_WIDTH, FORT_HEIGHT))
    pygame.draw.rect(window, (255, 0, 0), (red_fort_x, red_fort_y, FORT_WIDTH, FORT_HEIGHT))

    # Walls
    for wall in walls:
        wall.draw(window)
    for wall in blue_fort_walls:
        wall.draw(window)
    for wall in red_fort_walls:
        wall.draw(window)
    
    # Flags
    blue_flag.draw(window)
    red_flag.draw(window)
    
    # Player
    blue_player_one.draw(window)

    # Update Display
    pygame.display.update()

pygame.quit()