# drop.py

import pygame
from pygame.sprite import Sprite

class Drop(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, rain_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = rain_game.screen

        # Load the drop image and set its rect attribute.
        self.image = pygame.image.load('drop.bmp')
        self.default_image_size = (56, 72)
        self.image = pygame.transform.scale(self.image, self.default_image_size)
        self.rect = self.image.get_rect()

        # Start each new drop near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the drop's exact horizontal position.
        self.x = float(self.rect.x)