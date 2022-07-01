# ship.py

import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self, rkt_game):
        """Initialize the ship and set its starting position."""
        self.screen = rkt_game.screen
        self.settings = rkt_game.settings
        self.screen_rect = rkt_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('rocket.bmp')
        self.default_image_size = (75, 75)
        self.image = pygame.transform.scale(self.image, self.default_image_size)
        self.rect = self.image.get_rect()
        # Start each new ship at the center of the screen.
        self.rect.center = self.screen_rect.center

        # Store a decimal value for the ship's horizontal and vertical 
        # positions.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)


        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_down = False
        self.moving_up = False

    def update(self):
        """Update the ship's position based on the movement flags."""
        # Update the ship's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed

        # Update rect object from self.x.
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)