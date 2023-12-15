import pygame
from random import randint
from variables import *

class Player:
    def __init__(self, x, y):
        self.speed = playerSpeed
        self.size = playerSize
        self.color = playerColor
        self.rect = pygame.Rect(x, y, self.size, self.size)
    def main(self, display):
        pygame.draw.rect(display, self.color, self.rect)

class Body:
    def __init__(self, x, y, time):
        self.x = x
        self.y = y
        self.time = time
        self.size = bodySize
        self.color = bodyColor
        self.rect = pygame.Rect(x, y, self.size, self.size)
    def main(self, display):
        pygame.draw.circle(display, self.color, (self.x, self.y), self.size)

class Apple:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, appleSize, appleSize)
    def main(self, display):
        pygame.draw.rect(display, appleColor, (self.x, self.y, appleSize, appleSize))

def getApple():
    length = wallSize + appleSize
    return Apple(randint(length, screenWidth - length), randint(length, screenHeight - length))

class Wall:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = wallColor
    def main(self, display):
        pygame.draw.rect(display, self.color, self.rect)

walls = []
walls.append(Wall(0, 0, wallSize, screenHeight))
walls.append(Wall(screenWidth - wallSize, 0, wallSize, screenHeight))
walls.append(Wall(0, screenHeight - wallSize, screenWidth, wallSize))
walls.append(Wall(0, 0, screenWidth, wallSize))