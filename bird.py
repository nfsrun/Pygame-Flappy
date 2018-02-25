import pygame


class Bird(pygame.sprite.Sprite):
    def __init__(self, x=350, y=250):
        # Call the parent class (Sprite) constructor
        super(Bird,self).__init__()
        self.image = pygame.image.load("flappy.png")
        self.rect = pygame.image.load("flappy.png")
        self.mask = pygame.mask.from_surface(self.image) #make a mask out of the image

    def update(self, x, y):
        self.rect = pygame.Rect(x, y, 39, 30)
        self.mask = pygame.mask.from_surface(self.image) #make an updated mask out of the image
