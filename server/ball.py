# * ------
# * File: /ball.py
# * File Created: Friday, 22nd November 2019 5:08:27 pm
# * Author: Alex Chomiak
# *
# * Last Modified: Sunday, 24th November 2019 2:20:53 am
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
        self.r = 20 # length of side

        # * Initiialize Rectangle
        self.image = pygame.Surface([self.r,self.r])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()

        # * Get display attributes
        self.display_width = pygame.display.get_surface().get_width()
        self.display_height = pygame.display.get_surface().get_height()

        # * Set initial position attributes
        self.speedGoal = 35.0
        self.speedIncrement = 5.0
        self.speed = 0.0
        self.x = 0.0
        self.y = 0.0
        self.direction = 0
        self.updateCt = 0

        # * Reset ball initially
        self.reset()
        print("Initialized ball")

    def reset(self):
        # * Center Ball
        self.center()

        # * Increase overall speed goal
        self.speedGoal = min(self.speedGoal * 1.1, 40.0)

        # * Set initial speed
        self.speed = 0.0

        # * Calculate random direction
        angle = random.randint(-45,45)
        if(random.randint(0,10) % 2 == 0):
            angle += 180

        # * Set direction
        self.direction = angle

    def bounce(self, diff):
        print("Bouncing!!!")
        self.direction = (180 - self.direction) % 360
        self.direction -= diff # * increase ball speed?

    def center(self):
        self.x = (self.display_width / 2) - (self.r / 2)
        self.y = (self.display_height / 2) - (self.r / 2)

    def update(self):
        # * Update Speed
        self.updateCt += 1
        if(self.updateCt == 20):
            self.updateCt = 0
            if(self.speed + self.speedIncrement > self.speedGoal): self.speed = self.speedGoal
            else: self.speed += self.speedIncrement

        # * Update Position
        self.x += self.speed * (math.sin(math.radians(self.direction)))
        self.y -= self.speed * (math.cos(math.radians(self.direction)))

        if(abs(self.direction - 90) < 5  or abs(self.direction - 270) < 5):
            self.direction = (math.copysign(1.0,self.direction) * 20) + self.direction

        self.rect.x = self.x
        self.rect.y = self.y

        if self.x <= 0:
            self.direction = (360 - self.direction) % 360
        elif self.x > self.display_width - self.r :
            self.direction = (360 - self.direction) % 360