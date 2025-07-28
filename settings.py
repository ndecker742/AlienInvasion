'''
settings.py
Nathaniel Decker
The purpose of this program is to maintain the settings for the game
27JUL2025
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
        self.difficulty_scale = 1.1
        
        self.ship_file = Path.cwd() / 'Assets' / 'images' / 'spaceship_small_blue.png'
        self.ship_w = 40
        self.ship_h = 60
        self.ship_speed = 5
        self.starting_ship_count = 3

        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'pink_laser.png'
        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'laserpew.ogg'
        self.impact_sound = Path.cwd() / 'Assets' / 'sound' / 'qubodup-crash.ogg'
        self.bullet_speed = 7
        self.bullet_w = 25
        self.bullet_h = 80
        self.bullet_amount = 5

        self.alien_file = Path.cwd() / 'Assets' / 'images' / 'alien_spaceship.png'
        self.alien_w = 40
        self.alien_h = 40
        self.fleet_speed = 1
        self.fleet_direction = 1
        self.fleet_drop_speed = 40

        self.button_w = 200
        self.button_h = 50
        self.button_color = (230, 41, 41)

        self.text_color = (255, 255, 255)
        self.button_font_size = 48
        self.HUD_font_size = 20
        self.font_file = Path.cwd() / 'Assets' / 'Fonts' / 'Silkscreen' / 'Silkscreen-Bold.ttf'

    def initialize_dynamic_settings(self):
        self.ship_speed = 5
        self.starting_ship_count = 3

        self.bullet_w = 25
        self.bullet_h = 80
        self.bullet_speed = 7
        self.bullet_amount = 5

        self.fleet_speed = 1
        self.fleet_drop_speed = 40
        self.alien_points = 50

    def increase_difficulty(self):
        self.ship_speed *= self.difficulty_scale
        self.bullet_speed *= self.difficulty_scale
        self.fleet_speed *= self.difficulty_scale