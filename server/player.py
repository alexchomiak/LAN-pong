# * ------ 
# * File: /player.py
# * File Created: Friday, 22nd November 2019 5:12:15 pm
# * Author: Alex Chomiak 
# * 
# * Last Modified: Friday, 22nd November 2019 6:07:12 pm
# * Modified By: Alex Chomiak 
# * 
# * Author Github: https://github.com/alexchomiak
# * ------ 
import pygame
import random
import math
from colors import BLACK, WHITE
class Player (pygame.sprite.Sprite):
    def __init__(self, y_pos, name):
        super().__init__()
        self.name = name
        self.width = 75
        self.height = 15
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
    
        self.display_width = pygame.display.get_surface().get_width()
        self.display_height = pygame.display.get_surface().get_height()
        
        self.x = 0
        self.y = y_pos
        
        self.score = 0

        self.rect.x = self.x
        self.rect.y = self.y

        self.connected = False
        
    def setX(self, x):
        if(x > self.display_width - self.width) :
            self.x = self.display_width - self.width
        elif (x < 0):
            self.x = 0
        else: 
            self.x = x

    def setY(self, y):
        self.y = y

    def update(self):
        self.rect.x = self.x
    
    def move(self, inc):
        self.setX(self.x + inc)