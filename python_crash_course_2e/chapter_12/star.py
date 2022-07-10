# star.py

import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, star_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = star_game.screen

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('star.bmp')
        self.default_image_size = (18, 10)
        self.image = pygame.transform.scale(self.image, self.default_image_size)
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)