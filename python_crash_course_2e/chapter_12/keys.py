# keys.py

import sys

import pygame

class PrintKeys:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Print Keys")


    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)                

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        print(event.key)
        if event.key == pygame.K_q:
            sys.exit()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.bg_color = (0, 0, 0)
        self.screen.fill(self.bg_color)

        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    pk = PrintKeys()
    pk.run_game()