import pygame

from setting import Settings

from ship import Ship

from background import Background

import game_functions as gf  

from pygame.sprite import Group

from alien import Alien

from game_stats import GameStats 

from button import Button


def run_game():
    #init game and create window objects"
    pygame.init()
    ai_settings = Settings()
    ai_background = Background('images/background_image.bmp', [0,0])
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien invasion")

    #create play button
    play_button = Button(ai_settings, screen, "Play")
    
    #create instance for storage game statistics
    stats = GameStats(ai_settings)

    #creating a ship
    ship = Ship(ai_settings, screen)
    #create droup for bullet storage
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # create alien
    #start main game loop

    while True:
        gf.check_events(ai_settings, screen,stats, play_button, ship, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship,  aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(
            ai_background, ai_settings, screen, stats, ship, aliens, bullets, play_button)
run_game()




