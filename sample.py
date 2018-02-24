import pygame
from pipe import Pipe
from bird import Bird
from random import randint

pygame.init()

black = (0, 0, 0)
red = (255, 0, 0)
bg = pygame.image.load("bkgrnd.png")
startscreen = pygame.image.load("startscreen.png")
flappy = Bird()

highScore = 0

size = 700, 500
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Flappy Bird")
all = pygame.sprite.Group()
all.add(flappy)

done = False
clock = pygame.time.Clock()  # will setup frames per second

allPipes = pygame.sprite.Group()  # the pipe.py sprites for the game

# define coordinates
# start position of flappy
x = 350
y = 250
#speed of
x_speed = 0
y_speed = 0
# mark ground
ground = 495
#position to start drawing  pipes
xloc = 700
yloc = 0 # we will determine this by a random call

# size of the pipes LxW
xsize = 100
ysize = randint(100, 325)
#passage for bird between pipes
space = 100
# speed to draw a pipe, make pipe visual on screen
pipespeed = 2.5
points = 0
lastKey = 0
allPipes.add(Pipe(0, xloc, yloc, space))
allPipes.add(Pipe(1, xloc, yloc, space))

# start game screen
start = False
while not start:
    pygame.display.flip()
    screen.blit(startscreen, [0, 0])

    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if mouse_x>306 and mouse_x< 391 and mouse_y>319 and mouse_y<352:
                start=True;

pygame.display.flip()


def gameOver():  # check if the bird goes too far down
    font = pygame.font.Font(None, 30)
    text = font.render("Game over", True, red)
    screen.blit(text, [200, 350])
    pygame.display.flip()
    pygame.time.wait(6000)


def score(points):
    font = pygame.font.Font(None, 20)
    text = font.render("Score: " + str(points), True, black)
    screen.blit(text, [1, 1])


while not done and start:

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

    allPipes.update(xloc, yloc, space)
    all.draw(screen)
    allPipes.draw(screen)
    score(points)

    hit_list = pygame.sprite.spritecollide(flappy, allPipes, False)
    if len(hit_list) != 0:
        done = True  # quit the whole program
        gameOver()
    y += y_speed/2
    xloc -= pipespeed

    if y > ground:
        gameOver()
        y_speed = y_speed/2
        pipespeed = 0

        gameOver()
        y_speed = y_speed/2
        pipespeed = 0
        done = True

    if xloc < -80: # 80 px from the last pipe, draw the next one
        xloc = 700  # reset, x coordinate of drawing next pipe
        ysize = randint(100, 300)  # reset gap between pipes
        yloc = randint(200, 500-ysize)

    if x > xloc and x < xloc + 3: # made it past the pipe
        points = (points + 1)

    pygame.display.flip()
    clock.tick(60)

quit();