import pygame


class Bird(pygame.sprite.Sprite):
    def __init__(self, x=350, y=250):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.image = pygame.image.load("flappy.png")
        self.rect = pygame.Rect(x, y, 39, 30)

    def update(self, x, y):
        self.rect = pygame.Rect(x, y, 39, 30)
