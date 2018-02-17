import pygame
from random import randint


pygame.init()

black= (0,0,0)
white= (255,255,255)
green= (59,204,100)
bg = pygame.image.load("bkgrnd.png")
flappy= pygame.image.load("flappy.png")


size= 700,500
screen =pygame.display.set_mode(size)
pygame.display.set_caption("Flappy Bird")

done = False
clock = pygame.time.Clock() #will setup frames per second

# the bird
def bird(x,y):
    screen.blit(flappy, [x,y])
    #pygame.draw.circle(screen,black,[x,y],20)

def gameOver(): # check if the ball goes too far down

    font =pygame.font.SysFont("comicsansms.tff",20)
    text = font.render("Game over",True, black)
    screen.blit(text, [150,250])

def pipes(xloc, yloc, xsize, ysize):    
    pygame.draw.rect(screen, green, [xloc,yloc, xsize, ysize]) #top rectangle 
    pygame.draw.rect(screen, green, [xloc,int(yloc+ysize+space), xsize, ysize+500])

def score(points):
    font =pygame.font.SysFont("comicsansms.tff",20)
    text = font.render("Score: "+str(points),True, black)
    screen.blit(text, [0,0])
    
    
# define x and y
x= 350
y= 250
x_speed =0
y_speed=0
ground = 495 #500 pi - redius of ball
xloc=700
yloc=0
xsize=70
ysize= randint (0,350)
space = 150
pipespeed= 2.5
points=0
                                     
 
#main program loop
while not done:
    for event in pygame.event.get(): #game interaction
        if event.type == pygame.QUIT:
                done =True

        if event.type == pygame.KEYDOWN: # to start the game? 
            if event.key == pygame.K_UP:
                y_speed=-10

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP: #release key
                y_speed=5 

 #   screen.fill(white)
    screen.blit(bg,[0,0]) 
    pipes(xloc,yloc,xsize,ysize)
    bird(x,y)
    score(points)

    y+= y_speed
    xloc -= pipespeed

    if y > ground:
        gameOver()
        y_speed=0
        pipespeed=0 #stop screen movement

    # hit the pipe condition
    if x+2>xloc and y-20 < ysize and x-15 < xsize+xloc: #upper pipe
        gameOver()
        y_speed=0
        pipespeed=0
        done=True

    if x+2 > xloc and y+20 > ysize+space and x-15 < xsize+xloc: #lower pipe
        gameOver()
        y_speed=0
        pipespeed=0
        done=True
        
    
    if xloc< -80:
        xloc =700 # reset
        ysize=randint(50,350) #reset gap between pipes 

    if x> xloc and x< xloc+3:
        points = (points+1)
        
    pygame.display.flip()
    clock.tick(60)


pygame.quit() # quit the whole program 
            


