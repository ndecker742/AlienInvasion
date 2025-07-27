'''
game_stats.py
Nathaniel Decker
The purpose of this program is to manage the game stats
27JUL2025
'''
class GameStats():
    '''Keeps track of game stats'''
    
    def __init__(self, ship_limit):
        '''
        Initializes the game stats

        Args:
            ship_limit (int): Amount of ships before 'Game Over'
        '''
        self.ships_left = ship_limit


