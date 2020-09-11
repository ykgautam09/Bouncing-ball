import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((480, 320))
pygame.display.set_caption('Bouncing Ball')
pygame.display.set_icon(pygame.image.load('icon.png'))

ball = pygame.image.load('./icon.png')
positionX = random.randint(0, 480-32)
positionY = random.randint(0, 320-32)
position_dx = 0.08
position_dy = 0.08

while True:

    pygame.color=(123,0,200 )  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if positionX<=0:
        position_dx=-position_dx
    if positionY<=0:
        position_dy=-position_dy
    if positionY>=320-32:
        position_dy=-position_dy
    if positionX>=480-32:
        position_dx=-position_dx

    positionX += position_dx
    positionY += position_dy
    screen.blit(ball, (positionX, positionY))
    pygame.display.update()
