'''
alien_fleet.py
Nathaniel Decker
This program manages specific function of the alien fleet
27JUL2025
'''
import pygame
from alien import Alien
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class AlienFleet:
    '''Represents the function of the entire alien fleet'''
    
    def __init__(self, game: 'AlienInvasion'):
        '''Initializes the alien fleet
        Args:
            game (AlienInvasion): The alien invasion game, provides context
        '''
        self.game = game
        self.settings = game.settings
        self.fleet = pygame.sprite.Group()
        self.fleet_direction = self.settings.fleet_direction
        self.fleet_drop_speed = self.settings.fleet_drop_speed

        self.create_fleet()

    def create_fleet(self):
        '''The creation of the alien fleet'''
        alien_w = self.settings.alien_w
        alien_h = self.settings.alien_h
        screen_w = self.settings.screen_w
        screen_h = self.settings.screen_h
        
        fleet_w, fleet_h = self.calculate_fleet_size(alien_w, screen_w, alien_h, screen_h)
        x_offset, y_offset = self.calculate_offsets(alien_w, alien_h, screen_w, fleet_w, fleet_h)

        self._create_drifted_fleet(alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset)

    def _create_drifted_fleet(self, alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset):
        '''
        Contains the logic for the drifted fleet

        Args:
            alien_w (int): The width of the alien
            alien_h (int): The height of the alien
            fleet_w (int): The amount of aliens that fit horizontally
            fleet_h (int): The amount of aliens that fit vertically
            x_offset (int): Centers the aliens horizontally
            y_offset (int): Centers the aliens vertically
        '''
        vertical_shift = 10  # Vertical offset per column

        for col in range(fleet_w):
            for row in range(fleet_h):
                current_x = alien_w * col + x_offset
                current_y = alien_h * row + y_offset + col * vertical_shift
                if col % 2 == 0 or row % 2 == 0:
                    continue
                self._create_alien(current_x, current_y)

    def calculate_offsets(self, alien_w, alien_h, screen_w, fleet_w, fleet_h):
        '''
        Calulates the ossets for proper centering

        Args:
            alien_w (int): The width of the alien
            alien_h (int): The height of the alien
            screen_w (int): The total width of the screen
            fleet_w (int): The amount of aliens that fit horizontally
            fleet_h (int): The amount of aliens that fit vertically

        Returns:
            x_offset (int): Centers the aliens horizontally
            y_offset (int): Centers the aliens vertically
        '''
        half_screen = self.settings.screen_h // 2
        fleet_horizontal_space = fleet_w * alien_w
        fleet_vertical_space = fleet_h * alien_h
        x_offset = int((screen_w - fleet_horizontal_space) // 2)
        y_offset = int((half_screen - fleet_vertical_space) // 2)
        return x_offset, y_offset

    def calculate_fleet_size(self, alien_w, screen_w, alien_h, screen_h):
        '''
        Calculates the amount of aliens that fit vertically and horizontally

        Args:
            alien_w (int): The width of the alien
            screen_w (int): The width of the screen
            alien_h (int): The height of the alien
            screen_h (int): The height of the screen

        Returns:
            fleet_w (int): The amount of aliens that fit horizontally
            fleet_h (int): The amount of aliens that fit vertically
        '''
        fleet_w = (screen_w // alien_w)
        fleet_h = ((screen_h / 2) // alien_h)

        if fleet_w % 2 == 0:
            fleet_w -= 1
        else:
            fleet_w -= 2

        if fleet_h % 2 == 0:
            fleet_h -= 1
        else:
            fleet_h -= 2

        return int(fleet_w), int(fleet_h)
    
    def _create_alien(self, current_x, current_y):
        '''
        Creates an invidual alien and adds it to the fleet

        Args:
            current_x (int): The specific X-coordinate the alien will be
            current_y (int): The specific Y-coordinate the alien will be
        '''
        new_alien = Alien(self, current_x, current_y)

        self.fleet.add(new_alien)

    def _check_fleet_edges(self):
        '''Moves the fleet down and switches direction when hittting an edge'''
        alien: Alien
        for alien in self.fleet:
            if alien.check_edges():
                self._drop_alien_fleet()
                self.fleet_direction *= -1
                break

    def _drop_alien_fleet(self):
        '''Moves the fleet down'''
        for alien in self.fleet:
            alien.y += self.fleet_drop_speed

    def update_fleet(self):
        '''Checks the boundaries and updates the fleet'''
        self._check_fleet_edges()
        self.fleet.update()

    def draw(self):
        '''Renders the fleet to the screen'''
        alien: 'Alien'
        for alien in self.fleet:
            alien.draw_alien()

    def check_collisions(self, other_group):
        '''
        Checks for collisions between the alien fleet and other Sprite group

        Args:
            other_group (pygame.sprite.Group): The group other than the aliens

        Returns:
            dict: A colliding of the alien sprite with what hit it
        '''
        return pygame.sprite.groupcollide(self.fleet, other_group, True, True)
    
    def check_fleet_bottom(self):
        '''
        Checks if the alien fleet hit the bottom of the screen

        Returns:
            True: The Aliens height is less than or equal to the screen height
            False: The Aliens height is more than the screens height
        '''
        alien: Alien
        for alien in self.fleet:
            if alien.rect.bottom >= self.settings.screen_h:
                return True
            return False
        
    def check_destroyed_status(self):
        '''
        Checks if the alien fleet has been completely destroyed

        Returns:
            bool: True if all aliens are destroyed; False if not
        '''
        return not self.fleet
