import pygame
from random import randint


class Pipe(pygame.sprite.Sprite):

    def __init__(self, orientation, x, yloc, spacesize=80):
        # Call the parent class (Sprite) constructor
        self.o = orientation
        self.space = spacesize
        self.yloc = yloc/2
        super(Pipe, self).__init__()

        if (self.o == 1):
            self.image = pygame.image.load("pipe.png")
            self.rect = pygame.Rect(x, 500 - yloc, 69, 397)
        
        if (self.o == 0):
            self.image = pygame.image.load("pipeFlip.png")
            self.rect = pygame.Rect(x, 500 - yloc - self.space - 397, 69, 397)
        self.mask = pygame.mask.from_surface(self.image) #make a mask out of the image

        # we need to draw both upper and lower pipe, this only draw the same pipe as the very first, without changing the gaps

    def update(self, x, yloc, space):
        if self.o == 1:
            self.image = pygame.image.load("pipe.png")
            self.rect = pygame.Rect(x, 500 - yloc, 69, 397)
            # self.rect = pygame.Rect(x, self.rect.y+self.yloc-yloc/2+self.space-space, 69, 397)
            print("here")
        if self.o == 0:
            self.image = pygame.image.load("pipeFlip.png")
            self.rect = pygame.Rect(x, 500 - yloc - self.space - 397, 69, 397)
            # self.rect = pygame.Rect(x, self.rect.y+self.space-space/2, 69, 397)
            print("this one")
        self.mask = pygame.mask.from_surface(self.image) #make an updated mask out of the image
        # what do these 2 do?
        self.space = space
        self.yloc = yloc/2
