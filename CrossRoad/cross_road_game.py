from cars import Car
from game_screen import Game_Screen
from player import Player
from score import Score, Higher_Score
import turtle
import time

class Cross_Road:
    def __init__(self, difficulty : int):
        
        # Create a docstring
        """
        This class is the main class of the game
        It creates all the other classes and controls the game loop
        """
        
        # Game state
        self.game_on = True
        
        # Game settings
        self.difficult = 'hard' if difficulty == 2 else 'easy'
        self.velocity_increase_by_each_level = 0.87 if self.difficult == 'easy' else 0.72
        self.velocity = 0.1
        
        #Screen
        self.game_screen = Game_Screen()
        
        #Player
        self.player = Player()
        self.move_player_to_home()
        
        #Score
        self.score = Score()
        self.higher_score = Higher_Score()
        
        # Cars
        self.cars = []
        
        # Class methods calls
        self.__game_controls()
        self.create_cars()
        self.run()
        
    def create_cars(self):
        range_ = 65 if self.difficult == 'easy' else 80
        for i in range(range_):
            self.cars.append(
                Car())
    
    def __game_controls(self):
        """
        Create the controls for the game
        """
        self.game_screen.screen.onkeypress(self.player.move_up, 'w' )
        self.game_screen.screen.onkeypress(self.player.move_down, 's' )
        
    def move_cars(self):
        """
        Move the cars across the screen
        direction is from left to right
        """
        for car in self.cars:
            car.move()
            
    def check_colision(self):
        """
        Check if the player has collided with a car
        If so, end the game
        """
        for car in self.cars:
            if self.player.distance(car) < 20:
                    self.game_over()
            
    def check_if_player_win(self):
        """
        Check if the player has reached the top of the screen
        If so, start a new level
        """
        if self.player.position()[1] > self.game_screen.screen.screensize()[1] / 2:
            self.__next_level()
            
    
    def move_all_cars_to_left(self):
        for car in self.cars:
            car.return_car_to_left()
            
    def move_player_to_home(self):
        new_x = 0
        new_y = (self.game_screen.screen.screensize()[1] // 2) * -1 + self.player.shapesize()[0] * 20 
        self.player.goto(new_x, new_y + 10)
        

    def __next_level(self):
        """
        This method is only called if player reach a new level
        if so, move all cars to a new cord on left of screen
        increase the level, and move player to bottom"""
        
        self.move_all_cars_to_left()
        
        
        self.move_player_to_home()
        
        self.score.increase_score()
        self.score.update_score()
        
        if self.score.score > self.higher_score.score:
            self.higher_score.score = self.score.score
            self.higher_score.update_score()
            self.higher_score.save_higher_score()
        
        self.velocity *= self.velocity_increase_by_each_level
        
    def game_over(self):
        self.game_on = False
        self.game_screen.screen.clear()
        self.game_screen.screen.bgcolor('black')
        self.player.hideturtle()
        self.player.goto(0, 0)
        self.player.write('Game Over', align='center', font=('Arial', 50, 'bold'))

        
        
    def run(self):
        while self.game_on:
            
            self.check_if_player_win()
            self.check_colision()
            self.game_screen.screen.update()
            self.move_cars()
            time.sleep(self.velocity)
        self.game_screen.screen.mainloop()

            
            
a = Cross_Road(difficulty=2)