import pygame
from src.constants import BALL_SIZE
# This class represents the soccer ball in the game. It takes an x and y
# position as arguments and sets the ball's initial position using these values.
# It also has a velocity attribute which is a list containing the ball's horizontal
# and vertical velocity. The update method is used to update the ball's position
# based on its velocity in each frame.


class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/images/ball.png")
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (BALL_SIZE, BALL_SIZE))
        self.rect.x = x
        self.rect.y = y
        self.velocity = [0, 0]

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
