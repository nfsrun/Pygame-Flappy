import pygame


class Pipe(pygame.sprite.Sprite):
    def __init__(self, orientation, x, y, space=50):
        # Call the parent class (Sprite) constructor
        super().__init__()
        if orientation == 1:
            self.image = pygame.image.load("pipeFlip.png")
            self.rect = pygame.Rect(x, y-space/2, 69, 397)
        else:
            self.image = pygame.image.load("pipe.png")
            self.rect = pygame.Rect(x, y+space/2, 69, 397)

    def update(self, x, y):
        if x < 0:
            self.rect = pygame.Rect(x, y, 69, 397)
        else:
            self.rect = pygame.Rect(x, self.rect.y, 69, 397)
