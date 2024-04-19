import turtle

class Score(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 1
        self.goto(-150, 260)
        self.color('black')
        self.update_score()
    
    def write_score(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
        
    
        
    def update_score(self):
        self.clear()
        self.write_score()
        
    
        
    def increase_score(self):
        self.score += 1
        
    
    
class Higher_Score(Score):
    def __init__(self):
        super().__init__()
        self.score = self.get_higher_score()
        self.goto(150,260)
        self.update_score()
    
    def save_higher_score(self):
        with open('high_score.txt', 'w') as f:
            f.write(str(self.score))
            
    def get_higher_score(self):
        try:
            with open('high_score.txt', 'r') as f:
                score = int(f.read())
                return score
        except FileNotFoundError:
            return 0
    
    def write_score(self):
        self.write(f"Highest score: {self.score}", align="center", font=("Arial", 24, "normal"))
