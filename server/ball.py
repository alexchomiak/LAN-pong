# * ------ 
# * File: /ball.py
# * File Created: Friday, 22nd November 2019 5:08:27 pm
# * Author: Alex Chomiak 
# * 
# * Last Modified: Friday, 22nd November 2019 6:31:54 pm
# * Modified By: Alex Chomiak 
# * 
# * Author Github: https://github.com/alexchomiak
# * ------ 


# * Game ball
import pygame
import random
import math
from colors import BLACK, WHITE
class Ball (pygame.sprite.Sprite) :
    def __init__(self):
        # * Call sprite constructor
        super().__init__()

        # * Size attributes
        self.r = 10 # length of side

        # * Initiialize Rectangle
        self.image = pygame.Surface([self.r,self.r])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()

        # * Get display attributes
        self.display_width = pygame.display.get_surface().get_width()
        self.display_height = pygame.display.get_surface().get_height()

        # * Set initial position attributes
        self.speed = 10.0
        self.x = 0.0
        self.y = 0.0
        self.direction = 0

        self.reset()
        print("Initialized ball")

    def reset(self, initialDirection = random.randrange(-45,45)):
        self.x = pygame.display.get_surface().get_width() / 2
        self.y = 350.0
        self.speed *= 1.1
        self.direction = initialDirection

    def bounce(self, diff):
        self.direction = (180 - self.direction) % 360
        self.direction -= diff # increase ball speed?
    
    def update(self):
        self.x += self.speed * (math.sin(math.radians(self.direction)))
        self.y -= self.speed * (math.cos(math.radians(self.direction)))
        
   
        self.rect.x = self.x
        self.rect.y = self.y
        
        if self.x <= 0:
            self.direction = (360 - self.direction) % 360
        elif self.x > self.display_width - self.r :
            self.direction = (360 - self.direction) % 360