import turtle
import random


class Car(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("red")
        self.penup()
        self.speed(0)
        self.color(self.random_color())
        self.y_positions = [ i * 20 for i in range(-12, 14)]
        self.x_positions = [i * 20 for i in range(-100, -10, 2)]
        
        self.goto(random.choice(self.x_positions), random.choice(self.y_positions))

    def move(self):
        if self.xcor() > 300:
            self.return_car_to_left()
        self.forward(10)
        
    def return_car_to_left(self):
        self.goto(random.choice(self.x_positions), random.choice(self.y_positions))

    def random_color(self):
         return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))