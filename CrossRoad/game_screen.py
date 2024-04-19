import turtle


class Game_Screen():
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.colormode(255)
        self.screen.title("Pong")
        self.screen.setup(600,600)
        self.screen.screensize(600, 600)
        self.screen.tracer(0)
        self.screen.listen()