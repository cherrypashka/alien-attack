import pygame.font

class Button():
    def __init__(self, ai_settings, screen, msg):
        #initiation butoon atributs
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # assignment property and size of button
        self.width, self.height = 200, 50
        self.button_color = (0, 0, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        #Create rect object of button and alignment to the center of screen
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        #message of button is created olny once
        self.prep_msg(msg)

    def prep_msg(self, msg):
        #converts the message into a rectangle converts the message into a rectangle and aligns the text to the center
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        #display empty button and and message output
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
