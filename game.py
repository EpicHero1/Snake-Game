import pygame
from sys import exit
from random import randint
from classes import *
from variables import *

pygame.init()

FPS = 60

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()

player = pygame.Rect(screenWidth / 2 - playerSize, screenHeight / 2 - playerSize, playerSize, playerSize)
apple = getApple()

horizontal = vertical = 0
bodyList = []
pause = False

#Main Game Loop
while True:
    screen.fill(backgroundColor)
    apple.main(screen)

    if pause == False:
        player.x += playerSpeed * horizontal
        player.y += playerSpeed * vertical

    #Manage Collisions
    if player.colliderect(apple):
        apple = getApple()
        bodyTime += grow
        for body in bodyList:
            body.time += grow

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == leftKey and horizontal == 0:
                horizontal = -1
                vertical = 0
            elif event.key == rightKey and horizontal == 0:
                horizontal = 1
                vertical = 0
            elif event.key == upKey and vertical == 0:
                horizontal = 0
                vertical = -1
            elif event.key == downKey and vertical == 0:
                horizontal = 0
                vertical = 1
    
    for wall in walls:
        wall.main(screen)
        if player.colliderect(wall):
            pause = True

    bodyList.append(Body(player.x + playerSize / 2, player.y + playerSize / 2, bodyTime))
    
    count = 0
    for body in bodyList:
        body.main(screen)
        if pause == False:
            body.time -= 1
        if body.time < 0:
            bodyList.remove(body)
        if player.colliderect(body):
            count += 1
    
    if count > collide:
        pause = True

    pygame.draw.rect(screen, playerColor, player)

    clock.tick(FPS)
    pygame.display.update()