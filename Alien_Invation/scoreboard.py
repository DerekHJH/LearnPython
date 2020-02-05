import pygame.font;
from pygame.sprite import Group;
from ship import Ship;
class ScoreBoard():
    def __init__(self, ai_settings, screen, states):
        self.screen = screen;
        self.screen_rect = screen.get_rect();
        self.ai_settings = ai_settings;
        self.states = states;

        self.text_color = (30, 30, 30);
        self.font = pygame.font.SysFont(None, 48);

        self.prep_score();
        self.prep_highest_score();
        self.prep_level();
        self.prep_ships();

    def prep_score(self):
        rounded_score = int(round(self.states.score, -1));#round to the nearest 10
        score_str = "{:,}".format(rounded_score);
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color);

        self.score_rect = self.score_image.get_rect();
        self.score_rect.right = self.screen_rect.right - 20;
        self.score_rect.top = 20;
    
    def prep_highest_score(self):
        rounded_highest_score = int(round(self.states.highest_score, -1));#round to the nearest 10
        highest_score_str = "{:,}".format(rounded_highest_score);
        self.highest_score_image = self.font.render(highest_score_str, True, self.text_color, self.ai_settings.bg_color);

        self.highest_score_rect = self.highest_score_image.get_rect();
        self.highest_score_rect.right = self.screen_rect.centerx;
        self.highest_score_rect.top = self.score_rect.top;

    def prep_level(self):
        level_str = str(self.states.level);
        self.level_image = self.font.render(level_str, True, self.text_color, self.ai_settings.bg_color);

        self.level_rect = self.level_image.get_rect();
        self.level_rect.right = self.score_rect.right;
        self.level_rect.top = self.score_rect.bottom + 10;
    def prep_ships(self):
        self.ships = Group();
        for ship_number in range(self.states.ships_left):
            ship = Ship(self.ai_settings, self.screen);
            ship.rect.x = 10 + ship_number * ship.rect.width;
            ship.rect.y = 10;
            self.ships.add(ship);

    def blitme(self):
        self.screen.blit(self.score_image, self.score_rect);
        self.screen.blit(self.highest_score_image, self.highest_score_rect);
        self.screen.blit(self.level_image, self.level_rect);
        self.ships.draw(self.screen);
