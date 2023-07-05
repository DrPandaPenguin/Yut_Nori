import pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the game loop
running = True
while running:
    # Limit the frame rate to FPS
    pygame.time.Clock().tick(FPS)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the game state

    # Draw the game state to the screen
    pygame.display.flip()

pygame.quit()
