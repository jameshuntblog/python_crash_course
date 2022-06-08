# blue_sky.py

import sys

import pygame

from mario import Mario

class BlueSky:
    """A class to manage game assets and behavior."""
    
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        # Screen settings
        self.screen = pygame.display.set_mode((1200, 680))
        pygame.display.set_caption("Blue Sky")

        self.mario = Mario(self)

        # Set the background color.
        self.bg_color = (0,120,255)


    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.bg_color)

            # Redraw Mario during each pass through the loop.
            self.mario.blitme()

            # Make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the geme.
    bs = BlueSky()
    bs.run_game()
