import pygame;
from pygame.sprite import Group;
from settings import Settings;
from ship import Ship;
import game_functions as gf;
from game_states import GameStates;
from button import Button;
from scoreboard import ScoreBoard;


def run_game():
    pygame.init();
    ai_settings = Settings();
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height));
    pygame.display.set_caption("Alien Invasion");
    play_button = Button(ai_settings, screen, "Play");
    states = GameStates(ai_settings);
    sb = ScoreBoard(ai_settings, screen, states);
    ship = Ship(ai_settings, screen);
    bullets = Group();
    aliens = Group();
    gf.create_fleet(ai_settings, screen, ship, aliens);
    while True:
        gf.check_events(ai_settings, screen, ship, bullets, aliens, states, play_button, sb);
        if(states.game_active):
            ship.update();
            gf.update_bullets(ai_settings, screen, ship, bullets, aliens, states, sb);
            gf.update_aliens(ai_settings, screen, ship, bullets, aliens, states, sb);
        gf.update_screen(ai_settings, screen, ship, bullets, aliens, states, play_button, sb);
        

run_game();
