import pygame

# Initialize the game engine
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

size = [400, 300]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Game Title")

done = False
clock = pygame.time.Clock()

while not done:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True

    screen.fill(WHITE)

    pygame.draw.polygon(screen, GREEN, [[30, 150], [125, 100], [255, 150]], 5)
    pygame.draw.polygon(screen, GREEN, [[30, 150], [125, 100], [220, 150]], 0)

    pygame.display.flip()