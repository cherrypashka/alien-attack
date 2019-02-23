import pygame.font

class Scoreboard():

    #class for uotput game information

    def __init__(self, ai_settings, screen, stats):

        #init atributs game score
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        #settings font for output score

        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        #preparation of the original image

        self.prep_score()

    def prep_score(self):

        #converts current score to graphic display
        score_str = str(self.stats.score)
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        #output score in the upper right screen

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)