### Pygame - Flappy - Pipe Class
### Created by Shaila Hirji and Kevin Tran
### This is the Pipe Class that defines what a pipe can be. Pipes have a
### constructor and an update method.

import pygame

class Pipe(pygame.sprite.Sprite):

    # Constructor creates a pipe accordingly based on its x, y location and
    # its intended orientation in order to display the pipes correctly. The
    # pipes uses a png picture with a mask overlay on top of a pipe to help
    # detect collisions more accurately.
    def __init__(self, orientation, x, yloc, spacesize=80):
        # Call the parent class (Sprite) constructor
        self.o = orientation
        self.space = spacesize
        self.yloc = yloc / 2
        super(Pipe, self).__init__()

        if self.o == 1:
            self.image = pygame.image.load("pipe.png")
            self.rect = pygame.Rect(x, 500 - yloc, 69, 397)

        if self.o == 0:
            self.image = pygame.image.load("pipeFlip.png")
            self.rect = pygame.Rect(x, 500 - yloc - self.space - 397, 69, 397)
        self.mask = pygame.mask.from_surface(self.image)

    # update method updates a pipe accordingly based on its x, y location and
    # space size. It will do two different behaviors depending on its
    # orientation in order to display the pipes correctly.
    def update(self, x, yloc, space=80):
        if self.o == 1:
            self.image = pygame.image.load("pipe.png")
            self.rect = pygame.Rect(x, 500 - yloc, 69, 397)
        if self.o == 0:
            self.image = pygame.image.load("pipeFlip.png")
            self.rect = pygame.Rect(x, 500 - yloc - self.space - 397, 69, 397)
        self.mask = pygame.mask.from_surface(self.image)
        self.space = space
