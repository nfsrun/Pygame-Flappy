import pygame
from random import randint


class Pipe(pygame.sprite.Sprite):

    def __init__(self, orientation, x, y, space=100):
        # Call the parent class (Sprite) constructor
        self.o=orientation
        super(Pipe,self).__init__()
        if orientation == 1:

            self.image = pygame.image.load("pipeFlip.png")
            self.rect = pygame.Rect(x, y-space, 69, 397)

        else:
            self.image = pygame.image.load("pipe.png")
            self.rect = pygame.Rect(x, y+space, 69, 397)

#we need to draw both upper and lower pipe, this only draw the same pipe as the very first, without changing the gaps
    def update(self, x, y):

        if(self.o == 1):
            if x < -80:
                self.rect = pygame.Rect(x, y, 69, 397)
                self.rect = pygame.Rect(x, self.rect.y, 69, 397)
                print("here")

        else:
            self.rect = pygame.Rect(x, y, 69, 397)
            self.rect = pygame.Rect(x, self.rect.y, 69, 397)
            print("this one")
