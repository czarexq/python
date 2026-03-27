import pygame
from settings import BLOCK_SIZE, GREEN

pygame.init()

def draw_snake_part(x, y, screen):
    pixel_x = x * BLOCK_SIZE
    pixel_y = y * BLOCK_SIZE
    rect = (pixel_x, pixel_y, BLOCK_SIZE, BLOCK_SIZE)

    pygame.draw.rect(screen, GREEN, rect)