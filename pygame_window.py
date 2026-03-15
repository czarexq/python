import pygame

pygame.init()

CUBE_SIZE = 25
CUBE_NUMBER = 20
WIDTH = CUBE_NUMBER * CUBE_SIZE

screen = pygame.display.set_mode((WIDTH, WIDTH))

#colors:
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

screen.fill(WHITE)

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
