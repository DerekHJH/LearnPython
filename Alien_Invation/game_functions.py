import sys;
import pygame;
from bullet import Bullet;
from alien import Alien;
from time import sleep;


def fire_bullet(ai_settings, screen, ship, bullets):
    if(len(bullets) < ai_settings.bullets_allowed):
        new_bullet = Bullet(ai_settings, screen, ship);
        bullets.add(new_bullet);

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if(event.key == pygame.K_RIGHT):
        ship.moving_right = True;
    elif(event.key == pygame.K_LEFT):
        ship.moving_left = True;
    elif(event.key == pygame.K_UP):
        ship.moving_up = True;
    elif(event.key == pygame.K_DOWN):
        ship.moving_down = True;
    elif(event.key == pygame.K_SPACE):
        fire_bullet(ai_settings, screen, ship, bullets); 
    elif(event.key == pygame.K_q):
        sys.exit();
        

def check_keyup_events(event, ai_settings, screen, ship, bullets):
    if(event.key == pygame.K_RIGHT):
        ship.moving_right = False;
    elif(event.key == pygame.K_LEFT):
        ship.moving_left = False;
    elif(event.key == pygame.K_UP):
        ship.moving_up = False;
    elif(event.key == pygame.K_DOWN):
        ship.moving_down = False;


def check_events(ai_settings, screen, ship, bullets, aliens, states, play_button, sb):
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            sys.exit();
        elif(event.type == pygame.KEYDOWN):
            check_keydown_events(event, ai_settings, screen, ship, bullets);  
        elif(event.type == pygame.KEYUP):
            check_keyup_events(event, ai_settings, screen, ship, bullets);
        elif(event.type == pygame.MOUSEBUTTONDOWN):
            mouse_x, mouse_y = pygame.mouse.get_pos();
            check_play_button(ai_settings, screen, ship, bullets, aliens, states, play_button, sb, mouse_x, mouse_y);

def check_play_button(ai_settings, screen, ship, bullets, aliens, states, play_button, sb, mouse_x, mouse_y):
    if(play_button.rect.collidepoint(mouse_x, mouse_y) and states.game_active==False):
        ai_settings.initialize_dynamic_settings();
        pygame.mouse.set_visible(False);#Let the cursor disappear 
        states.reset();

        sb.prep_score();
        sb.prep_highest_score();
        sb.prep_level();
        sb.prep_ships();

        states.game_active = True;
        aliens.empty();
        bullets.empty();
        create_fleet(ai_settings, screen, ship, aliens);
        ship.reset();
        
def update_screen(ai_settings, screen, ship, bullets, aliens, states, play_button, sb):
    screen.fill(ai_settings.bg_color); 
    ship.blitme();
    for bullet in bullets.sprites():
        bullet.blitme();
    aliens.draw(screen);
    sb.blitme();
    if(states.game_active == False):
        play_button.blitme();
    #The latest drawn, the latest shown
    pygame.display.flip();

def update_bullets(ai_settings, screen, ship, bullets, aliens, states, sb):
    bullets.update();
    for bullet in bullets.copy():
        if(bullet.rect.bottom <= 0):
            bullets.remove(bullet);
    check_bullet_alien_collisions(ai_settings, screen, ship, bullets, aliens, states, sb);
    
def check_bullet_alien_collisions(ai_settings, screen, ship, bullets, aliens, states, sb):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True);
    #True --- Disappear  False ---Continue to exist
    if(collisions):
        for alienss in collisions.values():
            states.score += ai_settings.alien_points * len(alienss);
            sb.prep_score();
        check_highest_score(states, sb);
        
    if(len(aliens)==0):
        bullets.empty();
        ai_settings.increase_speed();
        states.level += 1;
        sb.prep_level();
        create_fleet(ai_settings, screen, ship, aliens);

def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width;
    number_aliens_x = int(available_space_x / (2 * alien_width));
    return number_aliens_x;

def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y = (ai_settings.screen_height - 3 * alien_height - ship_height);
    number_rows = int(available_space_y / (2 * alien_height));
    return number_rows;

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen);
    alien.rect.x = alien.rect.width + 2 * alien.rect.width * alien_number;
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number;
    aliens.add(alien);

def create_fleet(ai_settings, screen, ship, aliens):
    alien = Alien(ai_settings, screen);
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width); 
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height);
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number); 

def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if(alien.check_edges()):
            change_fleet_direction(ai_settings, aliens);
            break;

def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed;
    ai_settings.fleet_direction *= -1;

def ship_hit(ai_settings, screen, ship, bullets, aliens, states, sb):
    if(states.ships_left > 0):
        states.ships_left -= 1;
        sb.prep_ships();
        aliens.empty();
        bullets.empty();
        create_fleet(ai_settings, screen, ship, aliens);
        ship.reset();
        sleep(0.5);
    else:
        states.game_active = False;
        pygame.mouse.set_visible(True);

def check_aliens_bottom(ai_settings, screen, ship, bullets, aliens, states, sb):
    screen_rect = screen.get_rect();
    for alien in aliens.sprites():
        if(alien.rect.bottom >= screen_rect.bottom):
            ship_hit(ai_settings, screen, ship, bullets, aliens, states, sb);
            break;

def update_aliens(ai_settings, screen, ship, bullets, aliens, states, sb):
    check_fleet_edges(ai_settings, aliens);
    aliens.update();
    check_aliens_bottom(ai_settings, screen, ship, bullets, aliens, states, sb);
    if(pygame.sprite.spritecollideany(ship, aliens)):
        ship_hit(ai_settings, screen, ship, bullets, aliens, states, sb);
        
def check_highest_score(states, sb):
    if(states.score > states.highest_score):
        states.highest_score = states.score;
        sb.prep_highest_score();









