class Settings():

    #"class for store all game settings of Alien invasion

    def __init__(self):

        #init game settings

        self.screen_width = 1600
        self.screen_height = 1000
        self.ship_speed_factor = 30
        self.ship_limit =  3
        self.bg_color = (0, 0, 0)

        #bullet parametrs

        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 193, 0, 32
        self.bullets_allowed = 3

        self.fleet_drop_speed = 15
    
        #game acceleration rate

        self.speedup_scale = 1.1

        #point for 1 aliens accelerations rate
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):

    #initializes the settings that change during the game
        self.ship_speed_factor = 20
        self.bullet_speed_factor = 20
        self.alien_speed_factor = 10

    #fleet direction = 1 means move to the right and -1 move to the left
        self.fleet_direction = 1

        #point for 1 aliens
        self.alien_points = 50

    def increase_speed(self):

    #increases settings of speed
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
    



