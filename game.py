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

player = Player(screenWidth / 2 - playerSize, screenHeight / 2 - playerSize)
apple = getApple()

horizontal, vertical = 0, 0
bodyList = []
pause = False

#Main Game Loop
while True:
    screen.fill(backgroundColor)
    apple.main(screen)

    #Player movement
    if pause == False:
        player.rect.x += player.speed * horizontal
        player.rect.y += player.speed * vertical

    #Manage Collisions
    if player.rect.colliderect(apple):
        apple = getApple()
        bodyTime += growRate
        for body in bodyList:
            body.time += growRate

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
        if player.rect.colliderect(wall):
            pause = True

    bodyList.append(Body(player.rect.x + player.size / 2, player.rect.y + player.size / 2, bodyTime))
    
    #Handle body and collisions
    count = 0
    for idx, body in enumerate(bodyList):
        body.main(screen)
        if pause == False:
            body.time -= 1
        if body.time < 0:
            bodyList.remove(body)
        if player.rect.colliderect(body) and idx < bodyTime - collide:
            pause = True

    player.main(screen)

    clock.tick(FPS)
    pygame.display.update()