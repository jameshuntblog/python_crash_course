# game_character.py

import sys

import pygame

from character import Character

class GameCharacter:
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Game Character")
        self.bg_color = (230, 230, 230)

        self.character = Character(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            self.screen.fill(self.bg_color)

            self.character.blitme()

            pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    gc = GameCharacter()
    gc.run_game()