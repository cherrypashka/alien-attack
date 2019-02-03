class Settings():
    #"class for store all game settings of Alien invasion
    def __init__(self):
        #init game settings
        self.screen_width = 1600
        self.screen_height = 1000
        self.ship_speed_factor = 30

        #bullet parametrs
        self.bullet_speed_factor = 20
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 220, 220, 220
        self.bullets_allowed = 3
