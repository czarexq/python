import pygame
import random
from settings import SCREEN_HEIGHT, SCREEN_WIDTH, RED, BLOCK_SIZE
pygame.init()

max_height = SCREEN_HEIGHT // BLOCK_SIZE
max_width = SCREEN_WIDTH // BLOCK_SIZE

def generate_food(snake):
    while True:
        x = random.randint(0, max_width - 1)
        y = random.randint(0, max_height - 1)
        if (x, y) not in snake:
            return (x, y)

def draw_food(x,y, screen):
    position = [
        x * BLOCK_SIZE,
        y * BLOCK_SIZE,
        BLOCK_SIZE,
        BLOCK_SIZE
    ]

    pygame.draw.rect(screen, RED, position)

