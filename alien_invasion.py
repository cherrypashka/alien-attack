
import pygame

from setting import Settings

from ship import Ship

from background import Background

import game_functions as gf 


def run_game():
    #init game and create window objects"
    pygame.init()
    ai_settings = Settings()
    ai_background = Background('images/background_image.bmp', [0,0])
    screen = pygame.display.set_mode(
            (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien invasion")
    #creating a ship
    ship = Ship(ai_settings, screen)
        #start main game loop

    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_background, screen, ship)
        
run_game()




