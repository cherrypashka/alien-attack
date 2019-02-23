import sys

from time import sleep

import pygame

from bullet import Bullet

from alien import Alien



def check_keydown_events(event, ai_settings, screen, ship, bullets):
    
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def fire_bullet(ai_settings, screen, ship, bullets):

    #launch  bullet if it max not get
    #create new new bullet and including it to the bullets group
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):

    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets):

    #handle keyboard and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN: 
            check_keydown_events(event, ai_settings, screen, ship, bullets)  
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button( ai_settings, screen, stats, play_button, ship, aliens, bullets,  mouse_x, mouse_y)

def check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    
    #starst the game after if button play is terned
    #if play_button.rect.collidepoint(mouse_x, mouse_y):

    button_cliked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_cliked and not stats.game_active:

        #invisible mouse cursor 
        pygame.mouse.set_visible(False)

        #reset game statistics
        stats.reset_stats()
        stats.game_active  = True    

        #clean lists of aliens and bullets
        aliens.empty()
        bullets.empty()

        #create new fleet and accomondation ship on the center of screen
        create_fleet(ai_settings, screen, ship, aliens) 
        ship.center_ship() 
                


def update_screen(ai_background, ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):

    #display last rendrend screen
    screen.fill([255, 255, 255])
    screen.blit(ai_background.image, ai_background.rect)
     #all bullets output behind ship and aliens images
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    #output score
    sb.show_score()

    #Play ia displayed if game inactive
    if not stats.game_active:
        play_button.draw_button()

    pygame.display.flip()

def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    bullets.update()
    
    #to delete old bullet
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
             bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)

def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    
    if collisions:
        for alien in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()

    if len(aliens) == 0:
    #to derstroy existing bullets? increase speed  and create new fleet
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, ship, aliens)


def get_number_aliens_x(ai_settings, alien_width):

    #create aliens fleet
    #create alien and calculating numbers of aliens in the range
    #interval between neighboring aliens = 1 width of alien
    available_space_x = ai_settings.screen_width - alien_width
    number_aliens_x  = int(available_space_x / (2 * alien_width)) - 1
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):

    available_space_y = (ai_settings.screen_height - 40 - ship_height)
    number_rows = int(available_space_y / (alien_height + 60))
    # number_rows = int(available_space_y / (2 * alien_height ))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
   
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width / 2
    alien.x = 5 + 2.5 * alien_width * alien_number
    alien.rect.x = alien.x 
    alien.rect.y = 10 + (alien.rect.height + 30) * row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):

    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width / 2)
    number_rows = get_number_rows(ai_settings, ship.rect.height,
    alien.rect.height)

    #creating first range of aliens

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(
                ai_settings, screen, aliens, alien_number, row_number)
       
def check_fleet_edges(ai_settings, aliens):
    
    #react when aliens reached end of the edge screen
    
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):

    #"""lowers the entire fleet and changes the direction of the fleet"""
    
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):

    # processing treatment ship with alien
    #reduction ship_left
    if stats.ships_left > 0:
        stats.ships_left -= 1

        #cleaning lists of aliens and bullets
        aliens.empty()
        bullets.empty()

        # create new fleet and location ship on center
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        #pause
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    #check go whether aliens to the edge of screen

    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break

def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):

    #lowers the entire fleet and changes the direction of the fleet 
    #and then updates the position of all aliens in the fleet
    check_fleet_edges(ai_settings, aliens)
    #update positions of all aliens
    aliens.update()

    #Check collisions between alien and ship
    if pygame.sprite.spritecollideany(ship, aliens):

        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
    
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)    
   