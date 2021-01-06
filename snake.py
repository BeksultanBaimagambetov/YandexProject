import pygame
import random

size = [600, 800]

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Змейка')


class SnakeBlock():
    def __init__(self, x, y):
        self.x = x
        self.y = y


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
