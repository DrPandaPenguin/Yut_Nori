import pygame
from stick import Stick 
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
FPS = 10
font = pygame.font.Font(None, 32)
# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE =(255,244,244)
BLACK =(222,0,0)

def draw_screen():
    screen.fill(WHITE)
    pygame.display.flip()

def write_screen(word,postions):
    text_surface = font.render(str(word), True, BLACK)
    screen.blit(text_surface, postions)  # The tuple (20, 20) is the position
    pygame.display.update()



def main():
    # Set up the game loop
    running = True
    while running:
        # Limit the frame rate to FPS
        pygame.time.Clock().tick(FPS)
        draw_screen()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                throw_result = Stick.throw()
                write_screen(throw_result,(20,20))





    # 버튼으로 계속 누를수있도록 해보기


    pygame.quit()
main()