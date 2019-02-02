import pygame

class Ship():
    def __init__(self, ai_settings, screen):
    #init ship and set his zero position
        self.screen = screen
        self.ai_settings = ai_settings
    #download image and getting rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
    #every ship should appear at bottom of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
    # save senter ship coordinates
        self.center = float(self.rect.centerx)
    # move flag
        self.moving_right = False 
        self.moving_left = False

    
    def update(self):
    #update ship position comnsidering the flag
    #update atribut center, not rect
        if self.moving_right:
            self.center += self.ai_settings.ship_speed_factor 
        if self.moving_left:
            self.center -= self.ai_settings.ship_speed_factor
    #updare atribut rect on self.center base
        self.rect.centerx = self.center

    def blitme(self):
        #draw ship in count position
        self.screen.blit(self.image, self.rect)