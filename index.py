import pygame
import random
import math

# Initi pygame
pygame.init()
pygame.display.set_caption('Multiplayer Pong')
screen = pygame.display.set_mode((800,600))

# Game Booleans
done = False

# Define colors
BLACK = (0,0,0)
WHITE = (255,255,255)


# Game ball
class Ball (pygame.sprite.Sprite) :
    def __init__(self):
        # Call sprite constructor
        super().__init__()

        # Size attributes
        self.r = 10 # length of side

        # Initiialize Rectangle
        self.image = pygame.Surface([self.r,self.r])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()

        # Get display attributes
        self.display_width = pygame.display.get_surface().get_width()
        self.display_height = pygame.display.get_surface().get_height()

        # set initial position attributes
        self.speed = 0.0
        self.x = 0.0
        self.y = 0.0
        self.direction = 0

        self.reset()
        print("Initialized ball")

    def reset(self, initialDirection = random.randrange(-45,45)):
        self.x = pygame.display.get_surface().get_width() / 2
        self.y = 350.0
        self.direction = initialDirection

    def bounce(self, diff):
        self.direction = (180 - self.direction) % 360
        self.direction -= diff # increase ball speed?
    
    def update(self):
        self.x += self.speed * (math.sin(math.radians(self.direction)))
        self.y -= self.speed * (math.cos(math.radians(self.direction)))
        
        if self.y < 0 or self.y > 600 :
            self.reset()

        self.rect.x = self.x
        self.rect.y = self.y

        if self.x <= 0:
            self.direction = (360 - self.direction) % 360
        elif self.x > self.display_width - self.r :
            self.direction = (360 - self.direction) % 360

class Player (pygame.sprite.Sprite):
    def __init__(self, y_pos):
        super().__init__()
        self.width = 75
        self.height = 15
        self.image = pygame.Surface([self.width, self.height])



while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        pygame.display.flip()