'''
game_stats.py
Nathaniel Decker
The purpose of this program is to manage the game stats
27JUL2025
'''
from pathlib import Path
import json

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class GameStats():
    '''Manages all of the game stats for AlienInvasion'''
    
    def __init__(self, game: 'AlienInvasion'):
        '''
        Initializes the game stats

        Args:
            game (AlienInvasion): The game setting; provides context
        '''
        self.game = game
        self.settings = game.settings
        self.max_score = 0
        self.init_saved_scores()
        self.reset_stats()

    def init_saved_scores(self):
        '''Loads the saved high score. If NA, initializes a default score'''
        self.path = self.settings.scores_file
        if self.path.exists() and self.path.stat.__sizeof__() > 20:
            contents = self.path.read_text()
            scores = json.loads(contents)
            self.hi_score = scores.get('hi_score', 0)
        else:
            self.hi_score = 0
            self.save_scores()
            # save the file
    
    def save_scores(self):
        '''Logic for dumping and loading the saved high score'''
        scores = {
            'hi_score': self.hi_score
        }
        contents = json.dumps(scores, indent=4)
        try:
            self.path.write_text(contents)
        except FileNotFoundError as e:
            print(f'File Not Found: {e}')

    def reset_stats(self):
        '''resets the 'Every game' stats'''
        self.ships_left = self.settings.starting_ship_count
        self.score = 0
        self.level = 1

    def update(self, collisions):
        '''
        Updates the relevant scores

        Args:
            collisions (dict): Dict of collisions between sprite and bullet
        '''
        self._update_score(collisions)
        self._update_max_score()
        self._update_hi_score()

    def _update_max_score(self):
        '''Updates the max score'''
        if self.score > self.max_score:
            self.max_score = self.score

    def _update_hi_score(self):
        '''Updates the high score'''
        if self.score > self.hi_score:
            self.hi_score = self.score
            self.save_scores()
    
    def _update_score(self, collisions):
        '''
        Updates the score as aliens are killed

        Args:
            collisions (dict): Dict of collisions between sprite and bullet
        '''
        for alien in collisions.values():
            self.score += self.settings.alien_points

    def _update_level(self):
        '''Updates the level through increments'''
        self.level += 1

    


