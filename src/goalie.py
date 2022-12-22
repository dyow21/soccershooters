import pygame
from src.constants import GOALIE_SIZE
# This class represents the goalie in the game. It takes an x and y position as arguments
# and sets the goalie's initial position using these values. It also has a velocity attribute
# which is a list containing the goalie's horizontal and vertical velocity. The update method
# is used to update the goalie's position based on its velocity in each frame.
# You can then use these classes to create instances of the ball and the goalie in your main game script.


class Goalie(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/images/goalie.png")
        self.image = pygame.transform.scale(self.image, (GOALIE_SIZE, GOALIE_SIZE))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocity = [0, 0]

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
