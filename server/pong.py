# * ------ 
# * File: /pong.py
# * File Created: Friday, 22nd November 2019 5:16:31 pm
# * Author: Alex Chomiak 
# * 
# * Last Modified: Friday, 22nd November 2019 6:50:42 pm
# * Modified By: Alex Chomiak 
# * 
# * Author Github: https://github.com/alexchomiak
# * ------ 
import pygame
import random
import math
from ball import Ball
from colors import BLACK, WHITE
from player import Player
import time
import os
# Init pygame
pygame.init()
screen = pygame.display.set_mode([800,600])
pygame.display.set_caption('Multiplayer Pong')
pygame.mouse.set_visible(0)


player1 = Player(25, "Player 1")
player2 = Player(580, "Player 2")


EXITED = False

def start():

    # setup text
    font = pygame.font.Font(None, 36)

    background = pygame.Surface(screen.get_size())

    # create game ball
    ball = Ball()

    # ball sprite group
    balls = pygame.sprite.Group()
    balls.add(ball)



    # game sprite group
    gamesprites = pygame.sprite.Group()
    gamesprites.add(player1)
    gamesprites.add(player2)
    gamesprites.add(ball)

    # Game Timing
    done = False
    clock = pygame.time.Clock()
    exit_program = False
    while not exit_program:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_program = True
        
        if abs(player1.score - player2.score) > 3:
            done = True
        
        if not done:
            player1.update()
            player2.update()
            if player1.connected and player2.connected:
                ball.update()
        else:
            text = font.render("Game Over", 1 (200,200,200))
            textpos = text.get_rect(centerx=background.get_width()/2)
            textpos.top = 50
            screen.blit(text, textpos)

        # See if the ball hits the player paddle
        if pygame.sprite.spritecollide(player1, balls, False):
            # The 'diff' lets you try to bounce the ball left or right depending where on the paddle you hit it
            diff = (player1.rect.x + player1.width/2) - (ball.rect.x+ball.width/2)
    
            # Set the ball's y position in case we hit the ball on the edge of the paddle
            ball.y = 570
            ball.bounce(diff)
    
        # See if the ball hits the player paddle
        if pygame.sprite.spritecollide(player2, balls, False):
            # The 'diff' lets you try to bounce the ball left or right depending where on the paddle you hit it
            diff = (player2.rect.x + player2.width/2) - (ball.rect.x+ball.width/2)
    
            # Set the ball's y position in case we hit the ball on the edge of the paddle
            ball.y = 40
            ball.bounce(diff)
        
        if ball.y < 0:
            player2.score += 1
            ball.reset()
        elif ball.y > 600:
            player1.score += 1
            ball.reset()

        # Print the score
        scoreprint = "Player 1: "+str(player1.score)
        text = font.render(scoreprint, 1, WHITE)
        textpos = (0, 0)
        screen.blit(text, textpos)
    
        scoreprint = "Player 2: "+str(player2.score)
        text = font.render(scoreprint, 1, WHITE)
        textpos = (300, 0)
        screen.blit(text, textpos)
    
        # Draw Everything
        gamesprites.draw(screen)
        

        # flip display buffer
        pygame.display.flip()
        clock.tick(1000.0 / 30.0) # 30ms frame
    pygame.quit()
    os._exit(0)

    

