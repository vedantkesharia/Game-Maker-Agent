import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Dinosaur settings
DINO_WIDTH = 40
DINO_HEIGHT = 40
GRAVITY = 1
JUMP_STRENGTH = 15

# Obstacle settings
OBSTACLE_WIDTH = 20
OBSTACLE_HEIGHT = 40
OBSTACLE_MIN_DISTANCE = 300
OBSTACLE_MAX_DISTANCE = 600

# Game settings
FPS = 30

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dino Game")

# Load dinosaur image
dino_image = pygame.Surface((DINO_WIDTH, DINO_HEIGHT))
dino_image.fill(BLACK)

# Define the Dinosaur class
class Dinosaur:
    def __init__(self):
        self.rect = dino_image.get_rect()
        self.rect.x = 50
        self.rect.y = SCREEN_HEIGHT - DINO_HEIGHT
        self.jump_speed = 0
        self.is_jumping = False

    def update(self):
        if self.is_jumping:
            self.jump_speed -= GRAVITY
            self.rect.y -= self.jump_speed
            if self.rect.y >= SCREEN_HEIGHT - DINO_HEIGHT:
                self.rect.y = SCREEN_HEIGHT - DINO_HEIGHT
                self.is_jumping = False
                self.jump_speed = 0

    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            self.jump_speed = JUMP_STRENGTH

    def draw(self, screen):
        screen.blit(dino_image, self.rect)

# Define the Obstacle class
class Obstacle:
    def __init__(self, x):
        self.rect = pygame.Rect(x, SCREEN_HEIGHT - OBSTACLE_HEIGHT, OBSTACLE_WIDTH, OBSTACLE_HEIGHT)

    def update(self, speed):
        self.rect.x -= speed

    def draw(self, screen):
        pygame.draw.rect(screen, BLACK, self.rect)

# Main game loop
def main():
    clock = pygame.time.Clock()
    score = 0
    speed = 5
    dino = Dinosaur()
    obstacles = [Obstacle(SCREEN_WIDTH + random.randint(OBSTACLE_MIN_DISTANCE, OBSTACLE_MAX_DISTANCE))]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    dino.jump()

        dino.update()

        if len(obstacles) == 0 or obstacles[-1].rect.x < SCREEN_WIDTH - OBSTACLE_MAX_DISTANCE:
            new_obstacle_x = SCREEN_WIDTH + random.randint(OBSTACLE_MIN_DISTANCE, OBSTACLE_MAX_DISTANCE)
            obstacles.append(Obstacle(new_obstacle_x))

        for obstacle in obstacles:
            obstacle.update(speed)
            if obstacle.rect.colliderect(dino.rect):
                running = False
            if obstacle.rect.x + OBSTACLE_WIDTH < 0:
                obstacles.remove(obstacle)

        speed += 0.01
        score += 1

        # Drawing
        screen.fill(WHITE)
        dino.draw(screen)
        for obstacle in obstacles:
            obstacle.draw(screen)

        # Display score
        font = pygame.font.Font(None, 36)
        text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(text, (10, 10))

        pygame.display.flip()
        clock.tick(FPS)

    # Display game over message
    screen.fill(WHITE)
    
    font = pygame.font.Font(None, 72)
    text = font.render("Game Over", True, BLACK)
    screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(2000)
    print(f"Final Score: {score}")

    pygame.quit()

if __name__ == "__main__":
    main()






# import pygame
# import random

# # Initialize Pygame
# pygame.init()

# # Screen dimensions
# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 400

# # Colors
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)

# # Dinosaur settings
# DINO_WIDTH = 40
# DINO_HEIGHT = 40
# DINO_X = 50
# DINO_Y = SCREEN_HEIGHT - DINO_HEIGHT - 10
# DINO_JUMP_VELOCITY = -15
# GRAVITY = 1

# # Obstacle settings
# OBS_WIDTH = 20
# OBS_HEIGHT = 40
# OBS_GAP = 300

# # Game settings
# FPS = 60
# INITIAL_OBSTACLE_SPEED = 5
# SPEED_INCREMENT = 0.01  # Increase speed factor per frame

# # Initialize screen
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption("Dino Game")

# # Load dinosaur image
# dino_image = pygame.Surface((DINO_WIDTH, DINO_HEIGHT))
# dino_image.fill(BLACK)

# # Function to draw dinosaur
# def draw_dino(x, y):
#     screen.blit(dino_image, (x, y))

# # Function to draw obstacles
# def draw_obstacle(obs_list):
#     for obs in obs_list:
#         pygame.draw.rect(screen, BLACK, (obs[0], obs[1], OBS_WIDTH, OBS_HEIGHT))

# # Main game loop
# def main():
#     # Dinosaur variables
#     dino_y = DINO_Y
#     dino_velocity = 0
#     is_jumping = False

#     # Obstacle variables
#     obs_list = []
#     last_obs_x = SCREEN_WIDTH

#     # Score
#     score = 0

#     # Clock
#     clock = pygame.time.Clock()

#     # Obstacle speed
#     obstacle_speed = INITIAL_OBSTACLE_SPEED

#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False

#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_SPACE and not is_jumping:
#                     dino_velocity = DINO_JUMP_VELOCITY
#                     is_jumping = True

#         # Update dinosaur position
#         dino_velocity += GRAVITY
#         dino_y += dino_velocity

#         if dino_y >= DINO_Y:
#             dino_y = DINO_Y
#             is_jumping = False

#         # Update obstacles
#         if len(obs_list) == 0 or obs_list[-1][0] < SCREEN_WIDTH - OBS_GAP:
#             obs_list.append([SCREEN_WIDTH, SCREEN_HEIGHT - OBS_HEIGHT - 10])

#         for obs in obs_list:
#             obs[0] -= obstacle_speed
#             if obs[0] + OBS_WIDTH < 0:
#                 obs_list.pop(0)
#                 score += 1

#         # Check for collision
#         for obs in obs_list:
#             if DINO_X + DINO_WIDTH > obs[0] and DINO_X < obs[0] + OBS_WIDTH:
#                 if dino_y + DINO_HEIGHT > obs[1]:
#                     running = False

#         # Increase obstacle speed over time
#         obstacle_speed += SPEED_INCREMENT

#         # Clear screen
#         screen.fill(WHITE)

#         # Draw dinosaur
#         draw_dino(DINO_X, dino_y)

#         # Draw obstacles
#         draw_obstacle(obs_list)

#         # Update display
#         pygame.display.flip()

#         # Cap the frame rate
#         clock.tick(FPS)

#     print("Game Over! Your score was:", score)

# if __name__ == "__main__":
#     main()
#     pygame.quit()



