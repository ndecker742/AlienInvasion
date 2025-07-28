'''
game_stats.py
Nathaniel Decker
The purpose of this program is to manage the game stats
27JUL2025
'''
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class GameStats():
    '''Keeps track of game stats'''
    
    def __init__(self, game: 'AlienInvasion'):
        '''
        Initializes the game stats

        Args:
            game (AlienInvasion): The game setting; provides context
        '''
        self.game = game
        self.settings = game.settings
        self.max_score = 0
        self.reset_stats()

    def reset_stats(self):
        self.ships_left = self.settings.starting_ship_count
        self.score = 0
        self.level = 1

    def update(self, collisions):
        # update score
        self._update_score(collisions)

        # update max score
        self._update_max_score()

        # update high score

    def _update_max_score(self):
        if self.score > self.max_score:
            self.max_score = self.score
        # print(f"Max: {self.max_score}")
    
    def _update_score(self, collisions):
        for alien in collisions.values():
            self.score += self.settings.alien_points
        # print(f"Basic: {self.score}")


    def _update_level(self):
        self.level += 1

    


