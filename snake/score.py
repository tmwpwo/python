from turtle import *


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.sc = 0
        self.color("black")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update()


    def update(self):
        self.write(f"score:{self.sc}" , False, align='center', font=("Courier", 20, "normal"))
        
    def points(self):
        self.sc += 1
        self.clear()
        self.update()

    def the_end(self):
        self.goto(0,0)
        self.write("game over" , False, align='center', font=("Courier", 20, "normal"))

        
        