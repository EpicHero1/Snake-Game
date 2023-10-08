import pygame
from random import randint
from variables import *

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = playerSpeed
        self.rect = pygame.Rect(self.x, self.y, playerSize, playerSize)
    def main(self, display):
        pygame.draw.rect(display, playerColor, (self.x, self.y, playerSize, playerSize))

class Body:
    def __init__(self, x, y, time):
        self.x = x
        self.y = y
        self.time = time
        self.rect = pygame.Rect(self.x, self.y, bodySize, bodySize)
    def main(self, display):
        pygame.draw.circle(display, bodyColor, (self.x, self.y), bodySize)

class Apple:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, appleSize, appleSize)
    def main(self, display):
        pygame.draw.rect(display, appleColor, (self.x, self.y, appleSize, appleSize))

def getApple():
    return Apple(randint(50, screenWidth - 50), randint(50, screenHeight - 50))

class Wall:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.heigth = height
        self.rect = pygame.Rect(self.x, self.y, width, height)
    def main(self, display):
        pygame.draw.rect(display, wallColor, (self.x, self.y, self.width, self.heigth))
walls = []
walls.append(Wall(0, 0, wallSize, screenHeight))
walls.append(Wall(screenWidth - wallSize, 0, wallSize, screenHeight))
walls.append(Wall(0, screenHeight - wallSize, screenWidth, wallSize))
walls.append(Wall(0, 0, screenWidth, wallSize))