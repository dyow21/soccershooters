import pygame
import src.ball
import src.goalie
import src.goal
from src.constants import SCREEN_WIDTH, SCREEN_HEIGHT
import sys


class Game:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        # Initialize pygame and create the game window
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        # Create the ball and goalie
        self.ball = src.ball.Ball(self.screen_width - 50, self.screen_height - 50)
        self.goalie = src.goalie.Goalie(self.screen_width // 2, 300)
        self.goalie = src.goalie.Goalie(50, 50)
        self.goal = src.goal.Goal(self.screen_width // 2, self.screen_height - 50)
        self.background = pygame.image.load("assets/images/bckgrnd.png")
        # Add the ball and goalie to a sprite group
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.ball)
        self.sprites.add(self.goalie)
        self.sprites.add(self.goal)
        # Set the ball's initial velocity
        self.ball.velocity = [0, 0]
        # Set the goalie's initial velocity
        self.goalie.velocity = [0, 0]
        # Initialize the player's score
        self.score = 0

    def run(self):
        # Run the game loop
        while True:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # Set the ball's velocity based on player input
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.ball.velocity[0] = -5
                    elif event.key == pygame.K_RIGHT:
                        self.ball.velocity[0] = 5
                    elif event.key == pygame.K_UP:
                        self.ball.velocity[1] = -5
                    elif event.key == pygame.K_DOWN:
                        self.ball.velocity[1] = 5

            # Update the ball and goalie positions
            self.ball.update()
            self.goalie.update()

            # Check for collisions between the ball and the goalie
            if pygame.sprite.collide_rect(self.ball, self.goalie):
                # Reset the ball's position and velocity
                self.ball.rect.x = self.screen_width // 2
                self.ball.rect.y = self.screen_height // 2
                self.ball.velocity = [0, 0]
            # Check if the ball goes past the goalie
            elif self.ball.rect.x > self.screen_width or self.ball.rect.x < 0 or self.ball.rect.y > self.screen_height or self.ball.rect.y < 0:
                # Increment the player's score and reset the ball's position and velocity
                self.score += 1
                self.ball.rect.x = self.screen_width // 2
                self.ball.rect.y = self.screen_height // 2
                self.ball.velocity = [0, 0]
            # Clear the screen and draw the background image
            self.screen.blit(self.background, (0, 0))

            # Draw the sprites
            self.sprites.draw(self.screen)

            # Update the display
            pygame.display.flip()

    def update(self):
        # Update the ball and goalie positions
        self.ball.update()
        self.goalie.update()
        # Check for collisions between the ball and the goalie
        if pygame.sprite.collide_rect(self.ball, self.goalie):
            # Reset the ball's position and velocity
            self.ball.rect.x = self.screen_width // 2
            self.ball.rect.y = self.screen_height // 2
            self.ball.velocity = [0, 0]
        # Check if the ball goes past the goalie
        elif self.ball.rect.x > self.screen_width or self.ball.rect.x < 0 or self.ball.rect.y > self.screen_height or self.ball.rect.y < 0:
            # Increment the player's score and reset the ball's position and velocity
            self.score += 1
            self.ball.rect.x = self.screen_width // 2
            self.ball.rect.y = self.screen_height // 2
            self.ball.velocity = [0, 0]
        # Check if the ball goes into the goal
        if pygame.sprite.collide_rect(self.ball, self.goal):
            # Increment the player's score and reset the ball's position and velocity
            self.score += 1
            self.ball.rect.x = self.screen_width // 2
            self.ball.rect.y = self.screen_height // 2
            self.ball.velocity = [0, 0]
