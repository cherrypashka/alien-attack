import sys

import pygame

def check_events(ship):
    #handle keyboard and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False
                


def update_screen(ai_background, screen, ship):
    #display last rendrend screen
    screen.fill([255, 255, 255])
    screen.blit(ai_background.image, ai_background.rect)
    ship.blitme()
    pygame.display.flip()