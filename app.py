import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen size
WIDTH = 500
HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
BLUE = (0, 0, 200)

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Car Racing Game")

clock = pygame.time.Clock()

# Player car
car_width = 50
car_height = 100
car_x = WIDTH // 2 - car_width // 2
car_y = HEIGHT - 120
car_speed = 7

# Enemy car
enemy_width = 50
enemy_height = 100
enemy_x = random.randint(0, WIDTH - enemy_width)
enemy_y = -100
enemy_speed = 5

# Score
score = 0
font = pygame.font.SysFont(None, 35)

# Show Score Function
def show_score(score):
    text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(text, (10, 10))

# Game loop
running = True
while running:
    clock.tick(60)
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

    # Key controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 0:
        car_x -= car_speed
    if keys[pygame.K_RIGHT] and car_x < WIDTH - car_width:
        car_x += car_speed

    # Enemy movement
    enemy_y += enemy_speed

    if enemy_y > HEIGHT:
        enemy_y = -100
        enemy_x = random.randint(0, WIDTH - enemy_width)
        score += 1
        enemy_speed += 0.3  # Increase difficulty

    # Collision detection
    if (car_x < enemy_x + enemy_width and
        car_x + car_width > enemy_x and
        car_y < enemy_y + enemy_height and
        car_y + car_height > enemy_y):

        print("Game Over! Final Score:", score)
        pygame.quit()
        sys.exit()

    # Draw cars
    pygame.draw.rect(screen, BLUE, (car_x, car_y, car_width, car_height))
    pygame.draw.rect(screen, RED, (enemy_x, enemy_y, enemy_width, enemy_height))

    # Show score
    show_score(score)

    pygame.display.update()