import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
LANE_WIDTH = WIDTH // 3
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Dino Game')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (34, 139, 34)  # Tree color

# Load images
dino_img = pygame.Surface((50, 50))
dino_img.fill(BLACK)
tree_img = pygame.Surface((50, 50))
tree_img.fill(GREEN)

# Game variables
dino_width, dino_height = 50, 50
dino_speed = 5
obstacle_speed = 10
score = 0
obstacles = {0: [], 1: [], 2: []}  # Three lanes
obstacle_spawn_time = 30  # frames
obstacle_timer = 0
current_lane = 1  # Start in the middle lane
dino_x = current_lane * LANE_WIDTH + (LANE_WIDTH - dino_width) // 2
dino_y = HEIGHT - dino_height
clock = pygame.time.Clock()

# Key state tracking
keys = {
    pygame.K_LEFT: False,
    pygame.K_RIGHT: False,
    pygame.K_DOWN: False
}

def spawn_obstacle(lane):
    # Obstacles spawn at the top of their respective lane
    return {
        'rect': pygame.Rect(lane * LANE_WIDTH + (LANE_WIDTH - 50) // 2, -50, 50, 50)
    }

def draw_obstacle(obstacle):
    screen.blit(tree_img, (obstacle['rect'].x, obstacle['rect'].y))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key in keys:
                keys[event.key] = True
        if event.type == pygame.KEYUP:
            if event.key in keys:
                keys[event.key] = False

    # Move to the center lane with down arrow
    if keys[pygame.K_DOWN]:
        current_lane = 1
    else:
        # Move left or right based on key presses
        if keys[pygame.K_LEFT]:
            current_lane = 0
        if keys[pygame.K_RIGHT]:
            current_lane = 2
    
    dino_x = current_lane * LANE_WIDTH + (LANE_WIDTH - dino_width) // 2

    # Spawn and move obstacles
    obstacle_timer += 1
    if obstacle_timer > obstacle_spawn_time:
        lane = random.randint(0, 2)  # Random lane for each new obstacle
        obstacles[lane].append(spawn_obstacle(lane))
        obstacle_timer = 0

    for lane in obstacles:
        for obstacle in obstacles[lane]:
            obstacle['rect'].y += obstacle_speed  # Move obstacles down
            if obstacle['rect'].y > HEIGHT:
                obstacles[lane].remove(obstacle)
                score += 1

    # Collision detection
    dino_rect = pygame.Rect(dino_x, dino_y, dino_width, dino_height)
    for obstacle in obstacles[current_lane]:
        if dino_rect.colliderect(obstacle['rect']):
            print("Game Over! Score:", score)
            running = False

    # Drawing
    screen.fill(WHITE)
    screen.blit(dino_img, (dino_x, dino_y))
    for lane in obstacles:
        for obstacle in obstacles[lane]:
            draw_obstacle(obstacle)
    pygame.display.flip()

    clock.tick(30)

pygame.quit()
