# * ------ 
# * File: /pong.py
# * File Created: Friday, 22nd November 2019 5:16:31 pm
# * Author: Alex Chomiak 
# * 
# * Last Modified: Sunday, 24th November 2019 1:05:06 am
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
import os

#  * Init pygame
pygame.init()

# * Initialize game screen
screen = pygame.display.set_mode((1920,1080) )#pygame.FULLSCREEN)

# * Initialize background for screen
background = pygame.Surface(screen.get_size())

# * Set screen caption
pygame.display.set_caption('Multiplayer Pong')

# * Initialize font
font = pygame.font.Font(None, 36)

# * Init game clock
clock = pygame.time.Clock()

# * Make mouse invisible
# pygame.mouse.set_visible(0)



# *  Width Height Variables
display_width = pygame.display.get_surface().get_width()
display_height = pygame.display.get_surface().get_height()

# * Initialize players
player1 = Player(25, "Player 1")
player2 = Player(display_height - 50, "Player 2")


# * Game Tracking Variables
done = False
exit_program = False


def update_display():
    global clock, pygame, exit_program
        
    # * flip display buffer
    pygame.display.flip()
    
    # * 30fps frame refresh
    clock.tick(30) 
    
    # * Event processing
    for event in pygame.event.get():
        # ! When user clicks X on window, exit program
        if event.type == pygame.QUIT:
            exit_program = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.unicode == 'q':
                exit_program = True

    # * Update display
    pygame.display.update()

     # * fill screen
    screen.fill(BLACK)

    # * Print Scores
    print_scores()

# * Prints scores
def print_scores():
    # * Print the score for player 1
    scoreprint = "Player 1: "+str(player1.score)
    text = font.render(scoreprint, 1, WHITE)
    textpos = (0, 0)
    screen.blit(text, textpos)

    # * Print the score for player 2
    scoreprint = "Player 2: "+str(player2.score)
    text = font.render(scoreprint, 1, WHITE)
    textpos = (display_width - 200, 0)
    screen.blit(text, textpos)

# * This function counts down before the beginning of a game
# * Announce game starting/restartnig in 5 seconds   
def count_down(result_str, restarting = True):

    for i in range(0, 5):
        # * Display Result to users
        result = font.render(result_str, 1, WHITE)
        resultpos = result.get_rect(centerx=background.get_width()/2)
        resultpos.top = (background.get_height() / 2) - 25
        screen.blit(result, resultpos)

        # * Display seconds left
        time_str = f'Game {"restarting" if restarting else "starting"} in {5 - i} seconds'
        print(time_str)
        time = font.render(time_str, 1, WHITE)
        timepos = time.get_rect(centerx=background.get_width()/2)
        timepos.top = (background.get_height() / 2)
        screen.blit(time, timepos)
        
        # * Update Display
        update_display()
        
        # * Wait one second
        clock.tick(1) 

# * This function resets the game, and scores
# * It has a 10 second buffer between games
def reset_game():
    # * Declare globals
    global done, screen, background

    # * Construct Result String
    result_str = ""
    if(player1.score > player2.score): result_str += player1.name
    else: result_str += player2.name
    result_str += " won the game!"

    # * Display Result to users
    result = font.render(result_str, 1, WHITE)
    resultpos = result.get_rect(centerx=background.get_width()/2)
    resultpos.top = (background.get_height() / 2) - 25
    screen.blit(result, resultpos)

    # * Update Display
    update_display()

    # * Wait 5 seconds
    clock.tick(1.0 / 5.0) 

    # * Reset score
    player1.score = 0
    player2.score = 0
    
    # * Mark done as false
    done = False

    # * Trigger Count Down
    count_down(result_str)
    




# * Start function to start game
def start():
    global done, background, exit_program
    # * Trigger start countdown
    count_down("Welcome to PyPong!",False)
    
    # * create game ball
    ball = Ball()

    # * Initialize Ball sprite group (used for collision)
    balls = pygame.sprite.Group()
    balls.add(ball)

    # * Initialize Game sprite group
    gamesprites = pygame.sprite.Group()
    gamesprites.add(player1)
    gamesprites.add(player2)
    gamesprites.add(ball)


    # * Main event loop
    while not exit_program:        
        # * If Either player 3 more than the other, end the game
        if abs(player1.score - player2.score) > 3:
            done = True # TODO Add way to restart game
        
        
        if not done: # * If game isnt finished, update Player and Ball positions
            # * If both players are connected, update ball position
            if not player1.connected and not player2.connected:
                ball.center()
             
            # * Update Player positions
            player1.update()
            player2.update()
            ball.update()
        else:
            update_display()
            reset_game() # * Resets Game
            
        # * See if the ball hits the player paddle
        if pygame.sprite.spritecollide(player1, balls, False):
            # * The 'diff' lets you try to bounce the ball left or right depending where on the paddle you hit it
            diff = (player1.rect.x + player1.width/2) - (ball.rect.x+ball.r/2)
    
            #*  Set the ball's y position in case we hit the ball on the edge of the paddle
            ball.y += player1.rect.height
            ball.bounce(diff)
        

        # * See if the ball hits the player paddle
        if pygame.sprite.spritecollide(player2, balls, False):
            # * The 'diff' lets you try to bounce the ball left or right depending where on the paddle you hit it
            diff = (player2.rect.x + player2.width/2) - (ball.rect.x+ball.r/2)
    
            # * Set the ball's y position in case we hit the ball on the edge of the paddle
            ball.y -= player2.rect.height
            ball.bounce(diff)
        
        # * Determine if player has scored, and update score accordingly
        if ball.y < 0:
            player2.score += 1
            ball.reset()
        elif ball.y > display_height:
            player1.score += 1
            ball.reset()


        # * Draw Game Sprites
        gamesprites.draw(screen)

        # * Update Display
        update_display()

    pygame.display.flip() # * Flip display buffer
    screen.fill(BLACK) # * Fill Screen black
    pygame.quit() # * Close pygame window
    os._exit(0) # * Close all threads associated with process

    

