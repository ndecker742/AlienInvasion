'''
button.py
Nathaniel Decker
This program creates the button to start the game
27JUL2025
'''
import pygame.font

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Button:
    '''Manages functionality of the 'PLAY' button'''

    def __init__(self, game: 'AlienInvasion', msg):
        '''
        Initializes the button

        Args:
            game (AlienInvasion): The game setting; provides context
            msg (str): The displayed message on the button
        '''
        self.game = game
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.settings = game.settings
        self.font = pygame.font.Font(self.settings.font_file, 
            self.settings.button_font_size)
        self.rect = pygame.Rect(0, 0, self.settings.button_w, self.settings.button_h)
        self.rect.center = self.boundaries.center
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        '''
        Renders the button's text and centers it

        Args:
            msg (str): The button's text
        '''
        self.msg_image = self.font.render(msg, True, self.settings.text_color, None)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self):
        '''Draws the buttonm on the game screen'''
        self.screen.fill(self.settings.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def check_clicked(self, mouse_pos):
        '''
        Mangages the interaction between the mouse and the button

        Args:
            mouse_pos (tuple): The X-and-Y coords. of the mouse click

        Returns:
            bool: True if within the button; False if not
        '''
        return self.rect.collidepoint(mouse_pos)