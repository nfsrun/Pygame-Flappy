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
yloc = randint(250, 400) # we will determine this by a random call

# size of the pipes LxW
xsize = 100
ysize = randint(100, 325)
#passage for bird between pipes  will  be randomized per pass
space = 100
# speed to draw a pipe, make pipe visual on screen
pipespeed = 3.5
points = 0
lastKey = 0

bottomPipe = Pipe(1, xloc, yloc, space)
topPipe = Pipe(0, xloc,bottomPipe.rect.y, space)

allPipes.add(topPipe) #IMPORTANT THIS GOES FIRST LOOOOL OR IT WONT CALCULATE IT CORRECTLY OMG
allPipes.add(bottomPipe)

pygame.draw.rect(screen, black, [0, 300, 700, 60])

# start game screen
start = False
while not start:
    pygame.display.flip()
    screen.blit(startscreen, [0, 0])

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
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

        if event.type == pygame.KEYDOWN:  # to start the game / control
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

    for p in allPipes: #for each on all pipes instead
        if pygame.sprite.collide_mask(flappy, p) != None: #change to check via collide mask for more accurate check on bird
            done = True  # quit the whole program
            gameOver()
    y += y_speed/2 # what does this do?
    xloc -= pipespeed

    if y >= ground:
        gameOver()
        y_speed = y_speed/2
        pipespeed = 0

        # gameOver()
        # y_speed = y_speed/2
        # pipespeed = 0
        done = True

    if xloc < -80: # 80 px from the last pipe, draw the next one
        xloc = 700  # reset, x coordinate of drawing next pipe
        ysize = randint(100, 200)  # reset gap between

        yloc = randint(80, 200) #randomize the pipe placements
        space = randint(80, 100)  #randomize the gap length

    if x > xloc and x < xloc + 5: # made it past the pipe
        points = (points + 1)

    pygame.display.flip()
    clock.tick(60)

quit();