import sys

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

def check_events(ai_settings, screen, ship, bullets):
    #handle keyboard and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN: 
            check_keydown_events(event, ai_settings, screen, ship, bullets)  
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
           
                


def update_screen(ai_background, ai_settings, screen, ship, aliens, bullets):
    #display last rendrend screen
    screen.fill([255, 255, 255])
    screen.blit(ai_background.image, ai_background.rect)
     #all bullets output behind ship and aliens images
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    #alien.blitme()
    pygame.display.flip()

def update_bullets(bullets):
    bullets.update()
        #to delete old bullet
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
             bullets.remove(bullet)

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
    alien.x = 2.5 * alien_width * alien_number
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
       




   