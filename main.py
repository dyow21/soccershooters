import pygame
from src.ball import Ball
from src.goalie import Goalie
import src
from src.game import Game
from src.constants import SCREEN_WIDTH, SCREEN_HEIGHT
import sys


def main():
    # Create the game
    game = src.game.Game(SCREEN_WIDTH, SCREEN_HEIGHT)
    # Run the game loop
    game.run()
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {game.score}", 1, (0, 0, 0))
    game.screen.blit(text, (10, 10))
    # Update the game state
    game.update()
    # Update the display
    pygame.display.flip()


if __name__ == "__main__":
    main()
