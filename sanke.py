from turtle import Turtle
START_POSITION = [(0,0), (-20,0), (-40,0)] 
MOVE_DIST = 20

class Sanke:

    def __init__(self):
        self.segments = []
        self.create_snake()
    def create_snake(self):
        for position in START_POSITION:
            sq = Turtle("square")
            sq.color("black")
            sq.penup()
            sq.goto(position)
            self.segments.append(sq)
    
    def move(self):
        for seg_num in range(len(self.segments) -1 , 0,-1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DIST)

