import turtle

class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.speed(0)
        self.goto(0, 0)
        self.setheading(90)
    
    def move_up(self):
        self.setheading(90)
        new_x = self.xcor()
        new_y = self.ycor() + 20
        self.goto(new_x, new_y)
    
    def move_down(self):
        self.setheading(270)
        new_x = self.xcor()
        new_y = self.ycor() - 20
        self.goto(new_x, new_y)
        
    