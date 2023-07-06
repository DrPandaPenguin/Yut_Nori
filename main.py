import pygame
from stick import Stick 
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE =(255,244,244)
BLACK =(222,0,0)
def draw_screen():
    screen.fill(WHITE)
    font = pygame.font.Font(None, 32)

# Create a surface with text on it
# The arguments are the text string and anti-aliasing,
        # and the color of the text
    
    throw_result = Stick.throw()    
    text_surface = font.render(str(throw_result), True, BLACK)
    screen.blit(text_surface, (20, 20))  # The tuple (20, 20) is the position

    pygame.display.flip()
    pygame.display.update()

def main():
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
        # pygame.display.flip()
        draw_screen()


    pygame.quit()
main()