'''
bullet.py
Nathaniel Decker
The purpose of this program is to manage the different aspects of the bullet
20JUL2025
'''
import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Bullet(Sprite):
    '''Represents the projectiles fired by the ship'''
    
    def __init__(self, game: 'AlienInvasion'):
        '''
        Initialize a bullet with positional and visual aspects

        Args:
            game (AlienInvasion): The game setting; provides context
        '''
        super().__init__()

        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load(self.settings.bullet_file)
        self.image = pygame.transform.scale(self.image, 
            (self.settings.bullet_w, self.settings.bullet_h)
            )
        
        self.rect = self.image.get_rect()
        self.rect.midtop = game.ship.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        '''Updates the position of the bullet'''
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        '''Draws the bullet on screen'''
        self.screen.blit(self.image, self.rect)

