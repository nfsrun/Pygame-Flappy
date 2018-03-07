### Pygame - Flappy - Bird Class
### Created by Shaila Hirji and Kevin Tran
### This is the Bird Class that defines what a bird is. Birds have a
### constructor and an update method.

import pygame

class Bird(pygame.sprite.Sprite):

    # Constructor can be called as default or with specific (x, y) coordinates.
    # Constructor (x, y) defaults are x = 350 and y = 250. Bird's graphics are
    # derived from a png and is collision detected over a mask surrounding the
    # pixels.
    def __init__(self, x = 350, y = 250):
        # Call the parent class (Sprite) constructor
        super(Bird, self).__init__()
        self.image = pygame.image.load("flappy.png")
        self.rect = pygame.image.load("flappy.png")
        self.mask = pygame.mask.from_surface(self.image)  # make a mask out of the image

    # Updates the bird accordingly to specific coordinates
    def update(self, x, y):
        self.rect = pygame.Rect(x, y, 39, 30)
        self.mask = pygame.mask.from_surface(self.image)  # make an updated mask out of the image
