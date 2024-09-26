import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Dino Run')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load images
dino_img = pygame.Surface((50, 50))
dino_img.fill(BLACK)
obstacle_img = pygame.Surface((50, 50))
obstacle_img.fill(BLACK)

# Game variables
dino_x, dino_y = 100, HEIGHT - 100
dino_y_velocity = 0
gravity = 0.5
jump_strength = -10
obstacle_x, obstacle_y = WIDTH, HEIGHT - 100
obstacle_speed = 5
score = 0
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dino_y_velocity = jump_strength

    # Game logic
    dino_y += dino_y_velocity
    dino_y_velocity += gravity

    if dino_y > HEIGHT - 100:
        dino_y = HEIGHT - 100
        dino_y_velocity = 0

    obstacle_x -= obstacle_speed
    if obstacle_x < -50:
        obstacle_x = WIDTH
        score += 1

    # Collision detection
    dino_rect = pygame.Rect(dino_x, dino_y, 50, 50)
    obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, 50, 50)
    if dino_rect.colliderect(obstacle_rect):
        print("Game Over! Score:", score)
        running = False

    # Drawing
    screen.fill(WHITE)
    screen.blit(dino_img, (dino_x, dino_y))
    screen.blit(obstacle_img, (obstacle_x, obstacle_y))
    pygame.display.flip()

    clock.tick(30)

pygame.quit()
