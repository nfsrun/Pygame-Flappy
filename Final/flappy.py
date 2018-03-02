import pygame
from pipes import Pipe
from bird import Bird
import random

pygame.init()

black = (0, 0, 0)
red = (255, 0, 0)
bg = pygame.image.load("bkgrnd.png")
startscreen = pygame.image.load("startscreen_400x500.png")
flappy = Bird()

bgm = pygame.mixer.Sound("bgm.wav")
bgmOn = True
up = pygame.mixer.Sound("up.wav")
fail = pygame.mixer.Sound("fail.wav")
upSound = True

all = pygame.sprite.Group()
all.add(flappy)


size = 400, 500
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Flappy Bird")

done = False
clock = pygame.time.Clock()  # will setup frames per second

allPipes = pygame.sprite.Group()  # the pipe.py sprites for the game

# define coordinates
# start position of flappy
x = 150
y = 250
#speed of
x_speed = 0
y_speed = 0
# mark ground
ground = 495
#position to start drawing  pipes
xloc = 500
#passage for bird between pipes  will  be randomized per pass

space = random.randint(80, 100)
ready = False
yloc = random.randint(32, 400-32-space) # we will determine this by a random call

# size of the pipes LxW
xsize = 100
ysize = random.randint(100, 325)

# speed to draw a pipe, make pipe visual on screen
pipespeed = 4.0
points = 0
lastKey = 0

bottomPipe = Pipe(1, xloc, yloc, space)
topPipe = Pipe(0, xloc, bottomPipe.rect.y, space)

allPipes.add(topPipe) #IMPORTANT THIS GOES FIRST LOOOOL OR IT WONT CALCULATE IT CORRECTLY OMG
allPipes.add(bottomPipe)

pygame.draw.rect(screen, black, [0, 300, 400, 60])

# start game screen
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

def gameOver():  # check if the bird goes too far down
    if upSound:
        fail.play()
    bgm.stop()
    font = pygame.font.Font(None, 30)
    text = font.render("Game over", True, red)
    screen.blit(text, [200, 350])
    pygame.display.flip()
    pygame.time.wait(6000)

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

def score(points):
    font = pygame.font.Font(None, 20)
    text = font.render("Score: " + str(points), True, black)
    screen.blit(text, [1, 1])

screen.blit(bg, [0, 0])
allPipes.draw(screen)
screen.blit(flappy.image, [150, 250])
score(points)
readyScreen()

while not ready:
    for event in pygame.event.get():
        print(pygame.mouse.get_pos())
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if mouse_x >= 145 and mouse_x <= 230 and mouse_y >= 400 and mouse_y <= 420:
                upSound = not upSound
            if mouse_x >= 160 and mouse_x <= 210 and mouse_y >= 450 and mouse_y <= 470:
                bgmOn = not bgmOn
            screen.blit(bg, [0, 0])
            screen.blit(flappy.image, [150, 250])
            readyScreen()
        if event.type == pygame.KEYDOWN:  # to start the game / control
            y_speed = -10
            lastKey = pygame.K_UP
            ready = True
            if bgmOn:
                bgm.play()
            if upSound:
                up.play()

while not done and start:

    for event in pygame.event.get():  # game interaction

        if event.type == pygame.QUIT:
            done = True
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

        done = True

    if xloc < -80: # 80 px from the last pipe, draw the next one
        xloc =400  # reset, x coordinate of drawing next pipe

        ysize = random.randint(100, 200)  # reset gap between

        space = random.randint(80, 100)  #randomize the gap length
        random.seed()
        yloc = random.randint(32, 400-space-32) #randomize the pipe placements
    if x > xloc and x < xloc + 5 : # made it past the pipe
        points = (points + 1)

    pygame.display.flip()
    clock.tick(60)

quit();