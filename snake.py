import pygame
import random

block_size = 22
header_margin = 80
frame_color = (0, 255, 200)
white_color = (255, 255, 255)
blue_color = (200, 255, 255)
header_color = (0, 200, 150)
blocks_number = 30
margin = 1
size = [block_size * blocks_number + 2 * block_size + margin * blocks_number,
        block_size * blocks_number + 2 * block_size + margin * blocks_number + header_margin]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Змейка')


class SnakeBlock():
    def __init__(self, x, y):
        self.x = x
        self.y = y


def draw_block(color, row, col):
    pygame.draw.rect(screen, color, [block_size + col * block_size + margin * (col + 1),
                                     header_margin + block_size + row * block_size + margin * (row + 1),
                                     block_size, block_size])


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill(frame_color)
    pygame.draw.rect(screen, header_color, [0, 0, size[0], header_margin])
    for row in range(blocks_number):
        for col in range(blocks_number):
            if (row + col) % 2 == 0:
                color = blue_color
            else:
                color = white_color
            draw_block(color, row, col)

    pygame.display.flip()
