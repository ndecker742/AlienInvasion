'''
hud.py
Nathaniel Decker
This programs creates and initalizes the HUD
27JUL2025
'''
import pygame.font


class HUD:
    '''Manages the HUD for the Alien Invasion game'''

    def __init__(self, game):
        '''
        Initializes the different neccessary items for the HUD

        Args:
            game (AlienInvasion): The game setting; provides context
        '''
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.game_stats = game.game_stats
        self.font = pygame.font.Font(self.settings.font_file,
            self.settings.HUD_font_size)
        self.padding = 20
        self.update_scores()
        self._setup_life_image()
        self._update_level()

    def _setup_life_image(self):
        '''Loads and scales the image used to represent the lives'''
        self.life_image = pygame.image.load(self.settings.ship_file)
        self.life_image = pygame.transform.scale(self.life_image, (
            self.settings.ship_w, self.settings.ship_h
            ))
        self.life_rect = self.life_image.get_rect()

    def update_scores(self):
        '''Update the different scores as played'''
        self._update_max_score()
        self._update_score()
        self._update_hi_score()
    
    def _update_score(self):
        '''Used to update the player's current score while playing'''
        score_str = f'Score: {self.game_stats.score: ,.0f}'
        self.score_image = self.font.render(score_str, True,
            self.settings.text_color, None)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.left = self.padding
        self.score_rect.top = self.padding

    def _update_max_score(self):
        '''Used to update the player's max score while playing'''
        max_score_str = f'Max-Score: {self.game_stats.max_score: ,.0f}'
        self.max_score_image = self.font.render(max_score_str, True,
            self.settings.text_color, None)
        self.max_score_rect = self.max_score_image.get_rect()
        self.max_score_rect.right = self.boundaries.right - self.padding
        self.max_score_rect.top = self.padding

    def _update_hi_score(self):
        '''Used to update the player's high score while playing'''
        hi_score_str = f'Hi-Score: {self.game_stats.hi_score: ,.0f}'
        self.hi_score_image = self.font.render(hi_score_str, True,
            self.settings.text_color, None)
        self.hi_score_rect = self.hi_score_image.get_rect()
        self.hi_score_rect.right = self.max_score_rect.right
        self.hi_score_rect.top = self.score_rect.bottom + self.padding

    def _update_level(self):
        '''Used to update the player's level as they play'''
        level_str = f'Level: {self.game_stats.level: ,.0f}'
        self.level_image = self.font.render(level_str, True,
            self.settings.text_color, None)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.hi_score_rect.right
        self.level_rect.top = self.hi_score_rect.bottom + self.padding

    def _draw_lives(self):
        '''Draws the life figures onto the screen'''
        current_x = self.padding
        current_y = self.boundaries.bottom - self.life_rect.height - self.padding
        for _ in range(self.game_stats.ships_left):
            self.screen.blit(self.life_image, (current_x, current_y))
            current_x += self.life_rect.width + self.padding

    def draw(self):
        '''Draws the remaining HUD elements to the screen'''
        self.screen.blit(self.hi_score_image, self.hi_score_rect)
        self.screen.blit(self.max_score_image, self.max_score_rect)
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self._draw_lives()

    

