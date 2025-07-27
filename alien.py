'''
alien.py
Nathaniel Decker
This porgram manages specific alien entities within the fleet
27JUL2025
'''
import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_fleet import AlienFleet

class Alien(Sprite):
    '''Represents a single alien within the fleet'''
    
    def __init__(self, fleet: 'AlienFleet', x: float, y: float):
        '''
        Initialize an alien with reference to X-and-Y positioning

        Args:
            fleet (AlienFleet): The alien fleet; provides context
            x (float): Initialize horizontal position of the alien
            y (float): Initialize vertical position of the alien
        '''
        super().__init__()

        self.fleet = fleet
        self.screen = fleet.game.screen
        self.boundaries = fleet.game.screen.get_rect()
        self.settings = fleet.game.settings

        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(self.image, 
            (self.settings.alien_w, self.settings.alien_h)
            )
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def update(self):
        '''Updates the aliens position based on speed and direction'''
        temp_speed = self.settings.fleet_speed

        self.x += temp_speed * self.fleet.fleet_direction
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

    def check_edges(self):
        '''Checks the aliens have reached the hoirzontal edge of the screen

        Returns:
            bool: True if the alien touches or crosses designated boundaries
        '''
        return (
            self.rect.right >= self.boundaries.right 
            or self.rect.left <= self.boundaries.left
        )

    def draw_alien(self):
        '''Draws the alien on screen'''
        self.screen.blit(self.image, self.rect)

