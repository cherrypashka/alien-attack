import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    #class present one alien
    def __init__(self, ai_settings, screen):

        #init alien and his first position
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #load alien image and set rect as atribut
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #every new alien appears to left top of corner
        self.rect.x = 40
        self.rect.y = 40

        #save exact alien position
        self.x = float(self.rect.x)

    def blitme(self):
        #displays alien in its current positions
        self.screen.blit(self.image, self.rect)
