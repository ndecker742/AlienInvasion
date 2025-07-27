'''
arsenal.py
Nathaniel Decker
The purpose of this program is to manage the different aspects of the gun
27JUL2025
'''
import pygame
from bullet import Bullet
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Arsenal:
    '''Manages functionality of the arsenal for the Alien Invasion'''
    
    def __init__(self, game: 'AlienInvasion'):
        '''
        Initialize the arsenal with gamewide aceess
        
        Args:
            game (AlienInvasion): The game setting; provides context
        '''
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()

    def update_arsenal(self):
        '''Updates all bullets and removes off-screen bullets'''
        self.arsenal.update()
        self._remove_bullets_offscreen()

    def _remove_bullets_offscreen(self):
        '''Removes the offscreen bullets'''
        for bullet in self.arsenal.copy():
            if bullet.rect.bottom <= 0:
                self.arsenal.remove(bullet)

    def draw(self):
        '''Draws the bullets to the screen'''
        for bullet in self.arsenal:
            bullet.draw_bullet()

    def fire_bullet(self):
        '''
        Fires a bullet if the arsenal is less than the allowed amount

        Returns:
            True: The amount of bullets on screen is less than allowed amount
            False: The amount of bullets on screen is more than allowed amount
        '''
        if len(self.arsenal) < self.settings.bullet_amount:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)
            return True
        return False
    
