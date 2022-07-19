# raindrops.py

import sys

import pygame

from random import randint

from drop import Drop

class Raindrops:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        self.screen_width = 1900
        self.screen_height = 1000
        self.screen = pygame.display.set_mode((self.screen_width, \
            self.screen_height))
        pygame.display.set_caption("Raindrops")

        self.drops = pygame.sprite.Group()

        self._create_drops()

    def run_game(self):
        """Start the main loop for the game."""
        try:
            while True:
                self._check_events()
                self._update_drops()
                self._update_screen()
        except:
            pass

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _create_drops(self):
        """Create a group of drops."""
        drop = Drop(self)
        drop_width, drop_height = drop.rect.size
        available_space_x = self.screen_width - (2 * drop_width)
        number_drops_x = available_space_x // (2 * drop_width)
        
        # Determine the number of rows of drops that fit on the screen.
        available_space_y = (self.screen_height - (3 * drop_height))
        number_rows = available_space_y // (2 * drop_height)

        # Create the full pattern of drops.
        for row_number in range(number_rows):
            for drop_number in range(number_drops_x):
                self._create_drop(drop_number, row_number)


    def _update_drops(self):
        """Updates the positions of all drops"""
        for drop in self.drops.sprites():
            drop.rect.y += 1

        # Get rid of drops that have disappeared.
        for drop in self.drops.copy():
            if drop.rect.top >= 1000:
                self.drops.remove(drop)

        if len(self.drops) <= 59:
            drop = Drop(self)
            drop_width, drop_height = drop.rect.size
            available_space_x = self.screen_width - (2 * drop_width)
            number_drops_x = available_space_x // (2 * drop_width)

            # Create the full pattern of drops.
            for drop_number in range(number_drops_x):
                self._create_drop(drop_number, 1)

    def _create_drop(self, drop_number, row_number):
        """Create a star and place it in the row."""
        drop = Drop(self)
        drop_width, drop_height = drop.rect.size
        drop.x = drop_width + 2 * drop_width * drop_number + randint(-1900, 1900)
        drop.rect.x = drop.x
        drop.rect.y = drop_height + 2 * drop.rect.height * row_number
        self.drops.add(drop)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill((0, 0, 0))
        self.drops.draw(self.screen)

        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    rain = Raindrops()
    rain.run_game()