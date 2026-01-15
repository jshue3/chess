import pygame
from pygame.locals import *
pygame.init()
boardState = 1
height = 900
width = 1000
window = pygame.display.set_mode([width, height])
light_gray = (220, 220, 220)


def drawBoard():
    tileSize = 100
    for row in range(8):
        for col in range(8):
            if (row + col) % 2 == 0:
                color = light_gray
            else:
                color = 'gray'

            pygame.draw.rect(window, color, [col*tileSize+100, row*tileSize+50, tileSize, tileSize])

        


        




while boardState:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            boardState = 0
    
    window.fill('black')
    drawBoard()
    pygame.display.flip()

pygame.quit()