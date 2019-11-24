# * ------
# * File: /player.py
# * File Created: Friday, 22nd November 2019 5:12:15 pm
# * Author: Alex Chomiak
# *
# * Last Modified: Saturday, 23rd November 2019 11:40:41 pm
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
        # * Initialize sprite
        super().__init__()

        # * Set Name
        self.name = name

        # * Set dimensions of rectangle
        self.width = 150
        self.height = 25

        # * Initialize Surface Texture For Sprite
        self.image = pygame.Surface([self.width, self.height])

        # * Fill sprite with white pixels
        self.image.fill(WHITE)

        # * Get Bounding rectangle of sprite
        self.rect = self.image.get_rect()

        # * Get display dimensions
        self.display_width = pygame.display.get_surface().get_width()
        self.display_height = pygame.display.get_surface().get_height()

        # * Positional Coordinates
        self.x = 0
        self.y = y_pos

        # * Player Score
        self.score = 0

        # * Set rectangle coordinates
        self.rect.x = self.x
        self.rect.y = self.y

        # * Player connected
        self.connected = False

    def setX(self, x):
        #print(f"{self.display_width}px")
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