import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
    #class for to control bullet released by ship
    def __init__(self, ai_settings, screen, ship):
    #create object for bullet in the current position of ship
        super(Bullet, self).__init__()
        self.screen = screen
    #creating bullet in [0,0] position and assigning the correct position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
        ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
    #bullet position is stored in float form
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color 
        self.speed_factor = ai_settings.bullet_speed_factor
    
    def update(self):
        #moving bullet up on the screen
        #update bullet position
        self.y -= self.speed_factor
        #update rect position
        self.rect.y = self.y
     
    def draw_bullet(self):
        #output bullet on screen
        pygame.draw.rect(self.screen, self.color, self.rect )
    