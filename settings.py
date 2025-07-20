'''
settings.py
Nathaniel Decker
The purpose of this program is to maintain the settings for the game
'''
from pathlib import Path
class Settings:
    '''Stores default credentials for Alien Invasion'''

    def __init__(self):
        '''Intitializes the default credentials for Alien Invasion'''
        self.name: str = 'Alien Invasion'
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'SpaceBackground1.png'
        self.bg_overlay_file = Path.cwd() / 'Assets' / 'images' / 'moon_overlay.png'
        
        self.ship_file = Path.cwd() / 'Assets' / 'images' / 'spaceship_small_blue.png'
        self.ship_w = 40
        self.ship_h = 60
        self.ship_speed = 5

        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'pink_laser.png'
        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'laserpew.ogg'
        self.bullet_speed = 7
        self.bullet_w = 25
        self.bullet_h = 80
        self.bullet_amount = 5