# mario.py

import pygame

class Mario:
    """A class to manage the Mario image."""

    def __init__(self, bs_game):
        """Initialize the Mario image and set its starting position."""
        self.screen = bs_game.screen
        self.screen_rect = bs_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('mario.bmp')
        self.rect = self.image.get_rect()
        # Start each new Mario at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.center

    def blitme(self):
        """Draw Mario at its current location."""
        self.screen.blit(self.image, self.rect)