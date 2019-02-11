class Settings():

    #"class for store all game settings of Alien invasion

    def __init__(self):

        #init game settings

        self.screen_width = 1600
        self.screen_height = 1000
        self.ship_speed_factor = 30
        self.ship_limit =  3

        #settings of alien
        
        self.alien_speed_factor = 10
        self.fleet_drop_speed = 10

        #fleet direction = 1 means move to the right and -1 move to the left
        self.fleet_direction = 10


        #bullet parametrs

        self.bullet_speed_factor = 20
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 193, 0, 32
        self.bullets_allowed = 3
