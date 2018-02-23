import pygame


class Bird(pygame.sprite.Sprite):
    def __init__(self, x=350, y=250):
        # Call the parent class (Sprite) constructor
<<<<<<< HEAD
        super(Bird,self).__init__()
=======
        super().__init__()
>>>>>>> 3628712dde745c9119484744e1b345718d265e6c
        self.image = pygame.image.load("flappy.png")
        self.rect = pygame.Rect(x, y, 39, 30)

    def update(self, x, y):
        self.rect = pygame.Rect(x, y, 39, 30)
