### Pygame - Flappy
### Created by Shaila Hirji and Kevin Tran
### This is just another bootleg flappy bird game with our intention to make the
### bird continuously glide.

import pygame
from pipes import Pipe
from bird import Bird
import random

# initialize game with important variables that will be repeatedly used
pygame.init()
black = (0, 0, 0)
red = (255, 0, 0)
bg = pygame.image.load("bkgrnd.png")
startscreen = pygame.image.load("startscreen_400x500.png")
bgm = pygame.mixer.Sound("bgm.wav")
bgmOn = True
up = pygame.mixer.Sound("up.wav")
fail = pygame.mixer.Sound("fail.wav")
points = 0
lastKey = 0
upSound = True
done = False

# initialize bird and put it in a group
flappy = Bird()
all = pygame.sprite.Group()
all.add(flappy)

# initialize a screen and set a fixed size on it
size = 400, 500
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Flappy Bird")

# function will setup frames per second reference
clock = pygame.time.Clock()

# define start position coordinates of the bird
x = 150
y = 250

# speed of bird's descent
y_speed = 0

# mark ground y-position
ground = 495

# position to start drawing pipes
xloc = 500

# passage for bird between pipes will be randomized per pass
space = random.randint(80, 100)
ready = False
yloc = random.randint(32, 400-32-space)  # we will determine this by a random call

# size of the pipes LxW
xsize = 100
ysize = random.randint(100, 325)

# speed to draw a pipe, make pipe visual on screen
pipespeed = 4.0

# initialize and group top and bottom pipes
bottomPipe = Pipe(1, xloc, yloc, space)
topPipe = Pipe(0, xloc, bottomPipe.rect.y, space)
allPipes = pygame.sprite.Group()
# IMPORTANT THIS GOES FIRST OR IT WONT CALCULATE IT CORRECTLY
allPipes.add(topPipe)
allPipes.add(bottomPipe)

# initialize window with black screen
pygame.draw.rect(screen, black, [0, 300, 400, 60])

# start game screen and do initial startup tasks
start = False
while not start:
    pygame.display.flip()
    screen.blit(startscreen, [0, 0])
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if mouse_x > 156 and mouse_x < 241 and mouse_y > 319 and mouse_y < 352:
                start = True
pygame.display.flip()

# method checks if the bird goes too far down
def gameOver():  # check if the bird goes too far down
    if upSound:
        fail.play()
    bgm.stop()
    font = pygame.font.Font(None, 30)
    text = font.render("Game over", True, red)
    screen.blit(text, [200, 350])
    pygame.display.flip()
    pygame.time.wait(6000)

# function preps ready screen so user gets a head start
# warning before game play starts. Also renders a choice
# in which users can change the sound effect option. 
def readyScreen():
    font = pygame.font.Font(None, 30)
    text0 = font.render("Press up to start", True, red)
    screen.blit(text0, [125, 300])
    text1 = font.render("Click on feature to change setting. ", True, red)
    screen.blit(text1, [30, 350])
    text2 = font.render("SoundFX: On", True, red)
    text3 = font.render("BGM: On", True, red)
    if not upSound:
        text2 = font.render("SoundFX: Off", True, red)
    screen.blit(text2, [145, 400])
    if not bgmOn:
        text3 = font.render("BGM: Off", True, red)
    screen.blit(text3, [160, 450])
    pygame.display.flip()

# function to handle score updating
def score(points):
    font = pygame.font.Font(None, 20)
    text = font.render("Score: " + str(points), True, black)
    screen.blit(text, [1, 1])

# update screen initially with the starting screen, pipes, points, etc.
screen.blit(bg, [0, 0])
allPipes.draw(screen)
screen.blit(flappy.image, [150, 250])
score(points)
readyScreen()

# while loop that checks to make sure the player is ready (does nothing but
# allow players to change sound settings before the initial up key start.
while not ready:
    for event in pygame.event.get():

        # if statement to check that player presses play initially.
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if mouse_x >= 145 and mouse_x <= 230 and mouse_y >= 400 and mouse_y <= 420:
                upSound = not upSound
            if mouse_x >= 160 and mouse_x <= 210 and mouse_y >= 450 and mouse_y <= 470:
                bgmOn = not bgmOn
            screen.blit(bg, [0, 0])
            screen.blit(flappy.image, [150, 250])
            readyScreen()

        # this will launch the game and finish the while loop.
        if event.type == pygame.KEYDOWN:  # to start the game / control
            y_speed = -10
            lastKey = pygame.K_UP
            ready = True
            if bgmOn:
                bgm.play()
            if upSound:
                up.play()

# second while loop
while not done and start:

    # for each event for all frames
    for event in pygame.event.get():  # game interaction

        # quit when done
        if event.type == pygame.QUIT:
            done = True

        # else if user presses applicable up key, it will keep the bird up and
        # on release it will let the bird gradually descend.
        if event.type == pygame.KEYDOWN:  # to start the game / control
            if event.key == pygame.K_UP:
                y_speed = -10
                lastKey = pygame.K_UP
                if upSound:
                    up.play()
            elif event.key == pygame.K_w:
                y_speed = -10
                lastKey = pygame.K_w
                if upSound:
                    up.play()
            elif event.key == pygame.K_SPACE:
                y_speed = -10
                lastKey = pygame.K_SPACE
                if upSound:
                    up.play()
        if event.type == pygame.KEYUP:
            if event.key == lastKey:  # release key
                y_speed = 5

    # at the end, update the bird and the pipes and draw onto window. 
    screen.blit(bg, [0, 0])
    flappy.update(x, y)
    allPipes.update(xloc, yloc, space)
    all.draw(screen)
    allPipes.draw(screen)
    score(points)

    # for each on all pipes
    for p in allPipes:
        # change to check via collide mask for more accurate check on bird
        if pygame.sprite.collide_mask(flappy, p) != None:
            done = True  # quit the whole program
            gameOver()
    y += y_speed/2  # increase the bird descent by half the y_speed
    xloc -= pipespeed

    # if statement to account for when the bird dips below the surface
    if y >= ground:
        gameOver()
        y_speed = y_speed/2
        pipespeed = 0
        done = True

    if xloc < -80:  # 80 px from the last pipe, draw the next one
        xloc = 400  # reset, x coordinate of drawing next pipe

        ysize = random.randint(100, 200)  # reset gap between

        space = random.randint(80, 100)  #randomize the gap length
        random.seed()
        yloc = random.randint(32, 400-space-32) #randomize the pipe placements
    if x > xloc and x < xloc + 5 :  # made it past the pipe
        points = (points + 1)

    pygame.display.flip()
    clock.tick(60)

quit()