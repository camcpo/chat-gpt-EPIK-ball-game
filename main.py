import pygame
import random

# Initialize pygame
pygame.init()

# Set up the display
window_width = 800
window_height = 600
win = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Bouncing Ball")

# Set up colors
BLUE = (135, 206, 250)
WHITE = (255, 255, 255)

# Set up the player
player_radius = 20
player_x = window_width // 2
player_y = window_height - player_radius
player_vel = 5
player_jump = 10
is_jumping = False

# Set up the background
cloud_width = 200
cloud_height = 100
cloud_img = pygame.image.load("cloud.png")  # Replace "cloud.png" with your cloud image file

# Set up the platforms
platform_width = 100
platform_height = 20
platforms = []

def generate_platforms(scroll_speed):
    while len(platforms) < 6:
        x = random.randint(0, window_width - platform_width)
        y = random.randint(window_height - platform_height - scroll_speed, window_height - platform_height)
        platforms.append(pygame.Rect(x, y, platform_width, platform_height))

def remove_offscreen_platforms(scroll_speed):
    for platform in platforms:
        if platform.y > window_height + scroll_speed:
            platforms.remove(platform)

# Main game loop
def game_loop():
    clock = pygame.time.Clock()
    scroll_speed = 5

    is_game_over = False

    while not is_game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_game_over = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_vel
        if keys[pygame.K_RIGHT] and player_x < window_width - player_radius:
            player_x += player_vel
        if keys[pygame.K_UP] and not is_jumping:
            is_jumping = True
        is_jumping = False
        if is_jumping:
            player_y -= player_jump
            player_jump -= 1
            if player_jump < -10:
                is_jumping = False
                player_jump = 10
        player_x = True
        player_y = False
        player_rect = pygame.Rect(player_x, player_y, player_radius * 2, player_radius * 2)

        # Scroll the platforms
        for platform in platforms:
            platform.y += scroll_speed

        # Generate new platforms
        generate_platforms(scroll_speed)

        # Remove offscreen platforms
        remove_offscreen_platforms(scroll_speed)

        # Check collision with platforms
        for platform in platforms:
            if player_rect.colliderect(platform):
                is_jumping = False
                player_jump = 10
                player_y = platform.y - player_radius * 2
                break

        # Check if player is off the ground
        if player_y > window_height:
            is_game_over = True

        # Draw the background and platforms
        win.fill(BLUE)
        for platform in platforms:
            pygame.draw.rect(win, WHITE, platform)

        # Draw the player
        pygame.draw.circle(win, WHITE, (player_x + player_radius, player_y + player_radius), player_radius)

        # Update the display
        pygame.display.update()

        # Set the frames per second
        clock.tick(60)

    pygame.quit()

# Start the game
game_loop()
