import pygame


class Goal(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        # Load the goal image and set its rect attributes
        self.image = pygame.image.load("assets/images/goal.png")
        self.rect = self.image.get_rect()

        # Set the goal's position
        self.rect.x = x
        self.rect.y = y
