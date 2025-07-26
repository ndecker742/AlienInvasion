'''
ship.py
Nathaniel Decker
The purpose of this file is to control the different aspects of the ship
20JUL2025
'''
import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import Arsenal

class Ship:
    '''Manages functionality of the ship for Alien Invasion'''
    
    def __init__(self, game: 'AlienInvasion', arsenal: 'Arsenal'):
        '''
        Initialize the players ship with display, image, and movement logic

        Args:
            game (AlienInvasion): The game setting; provides context
            arsenal (Arsenal): The weapon system assigned to the ship
        '''
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()

        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(self.image, 
            (self.settings.ship_w, self.settings.ship_h)
            )
        
        self.rect = self.image.get_rect()
        self._center_ship()
        self.moving_right = False
        self.moving_left = False
        self.arsenal = arsenal

    def _center_ship(self):
        self.rect.midbottom = self.boundaries.midbottom
        self.x = float(self.rect.x)

    def update(self):
        '''Updates the position and ammo of the ship'''
        self._update_ship_movement()
        self.arsenal.update_arsenal()

    def _update_ship_movement(self):
        '''Controls the ship speed and limits it to the boundary'''
        temp_speed = self.settings.ship_speed
        if self.moving_right and self.rect.right < self.boundaries.right:
            self.x += temp_speed
        if self.moving_left and self.rect.left > self.boundaries.left:
            self.x -= temp_speed

        self.rect.x = self.x

    def draw(self):
        '''Renders the ship and its arsenal to the screen'''
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)

    def fire(self):
        '''
        Fires a bullet from the ships arsenal

        Returns:
            A bullet object is criteria is met
        '''
        return self.arsenal.fire_bullet()
    

    def check_collisions(self, other_group):
        if pygame.sprite.spritecollideany(self, other_group):
            self._center_ship()
            return True
        return False