import pygame
from pipe import Pipe
from bird import Bird
from random import randint

pygame.init()

black = (0, 0, 0)
bg = pygame.image.load("bkgrnd.png")
flappy = Bird()

highScore = 0

size = 700, 500
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Flappy Bird")
all = pygame.sprite.Group()
all.add(flappy)

done = False
clock = pygame.time.Clock()  # will setup frames per second

allPipes = pygame.sprite.Group() #the pipe.py sprites for the game

# define x and y
x = 350
y = 250
x_speed = 0
y_speed = 0
ground = 495
xloc = 700
yloc = 0
xsize = 100
ysize = randint(200, 350)
space = 200
pipespeed = 2.5
points = 0
lastKey = 0
allPipes.add(Pipe(0, xloc, yloc+ysize+space))
allPipes.add(Pipe(1, xloc, yloc))

pygame.display.flip()

def gameOver():  # check if the ball goes too far down
    font = pygame.font.SysFont("comicsansms.tff", 20)
    text = font.render("Game over", True, black)
    screen.blit(text, [200, 350])
    pygame.display.flip()
    pygame.time.wait(6000)

def score(points):
    font = pygame.font.SysFont("comicsansms.tff", 20)
    text = font.render("Score: " + str(points), True, black)
    screen.blit(text, [0, 0])

while not done:

    for event in pygame.event.get():  # game interaction

        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:  # to start the game?
            if event.key == pygame.K_UP:
                y_speed = -10
                lastKey = pygame.K_UP
            elif event.key == pygame.K_w:
                y_speed = -10
                lastKey = pygame.K_w
            elif event.key == pygame.K_SPACE:
                y_speed = -10
                lastKey = pygame.K_SPACE
        if event.type == pygame.KEYUP:
            if event.key == lastKey:  # release key
                y_speed = 5

    screen.blit(bg, [0, 0])
    flappy.update(x, y)
    allPipes.update(xloc, yloc)
    all.draw(screen)
    allPipes.draw(screen)
    score(points)

    hit_list = pygame.sprite.spritecollide(flappy, allPipes, False)
    if len(hit_list) != 0:
        done = True  # quit the whole program
        gameOver()
    y += y_speed
    xloc -= pipespeed

    if y > ground:
        gameOver()
        y_speed = 0
        pipespeed = 0  # stop screen movement

    # hit the pipe.py condition
    if x + 2 > xloc and y - 20 < ysize and x - 15 < xsize + xloc:  # upper pipe.py
        gameOver()
        y_speed = 0
        pipespeed = 0
        done = True

    if x + 2 > xloc and y + 20 > ysize + space and x - 15 < xsize + xloc:  # lower pipe.py
        gameOver()
        y_speed = 0
        pipespeed = 0
        done = True

    if xloc < -80:
        xloc = 700  # reset
        ysize = randint(50, 350)  # reset gap between pipes

    if x > xloc and x < xloc + 3:
        points = (points + 1)

    pygame.display.flip()
    clock.tick(60)

quit();