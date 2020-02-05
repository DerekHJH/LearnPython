import pygame;
from pygame.sprite import Sprite;
class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        super(Ship, self).__init__();
        self.screen = screen;
        self.screen_rect = screen.get_rect();
        self.image = pygame.image.load("images/ship.bmp");
        self.rect = self.image.get_rect();
        self.ai_settings = ai_settings;
        self.reset();
    def reset(self):
        self.rect.centerx=self.screen_rect.centerx;
        self.rect.bottom=self.screen_rect.bottom;

        self.paralell = float(self.rect.centerx);
        self.vertical = float(self.rect.centery);
        
        self.moving_right = False;
        self.moving_left = False;
        self.moving_up = False;
        self.moving_down = False;

    def update(self):
        if(self.moving_right and self.rect.right < self.screen_rect.right):
            self.paralell += self.ai_settings.ship_speed;
        elif(self.moving_left and self.rect.left > self.screen_rect.left):
            self.paralell -= self.ai_settings.ship_speed;
        elif(self.moving_up and self.rect.top > self.screen_rect.top):
            self.vertical -= self.ai_settings.ship_speed;
        elif(self.moving_down and self.rect.bottom < self.screen_rect.bottom):
            self.vertical += self.ai_settings.ship_speed;

        self.rect.centerx = self.paralell;
        self.rect.centery = self.vertical;
    def blitme(self):
        #According to self.rect, we draw the image on the screen;
        self.screen.blit(self.image, self.rect);
