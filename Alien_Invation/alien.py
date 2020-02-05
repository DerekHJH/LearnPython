import pygame;
from pygame.sprite import Sprite;

class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__();
        self.ai_settings = ai_settings;
        self.screen = screen;
        self.screen_rect = self.screen.get_rect();
        self.image = pygame.image.load("images/alien.bmp");
        self.rect = self.image.get_rect();
        self.rect.x = self.rect.width;
        self.rect.y = self.rect.height;
        self.x = float(self.rect.x);

    def blitme(self):
        self.screen.blit(self.image, self.rect);

    def update(self):
        self.x = self.rect.x;
        self.x += self.ai_settings.alien_speed * self.ai_settings.fleet_direction;
        self.rect.x = self.x;
    
    def check_edges(self):
        if(self.rect.right >= self.screen_rect.right):
            return True;
        elif(self.rect.left<=self.screen_rect.left):
            return True;
        return False;
