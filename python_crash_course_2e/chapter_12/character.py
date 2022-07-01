# character.py

import pygame

class Character:
    """A class to manage the ship."""

    def __init__(self, gc_game):
        """Initialize the character and set its starting position."""
        self.screen = gc_game.screen
        self.screen_rect = gc_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('game_character.bmp')
        self.default_image_size = (75, 97)
        self.image = pygame.transform.scale(self.image, self.default_image_size)
        self.rect = self.image.get_rect()
        # Start each new character at the center of the screen.
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the character at its current location."""
        self.screen.blit(self.image, self.rect)