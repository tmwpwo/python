from turtle import *
import time
position = [(0,20), (0,40), (0,60)]


class Snake:      

    def __init__(self):
        self.snake_parts = []
        self.creation()
        self.head = self.snake_parts[0]

    def creation(self):
        for i in position:
            self.new_part(i)
            
    def new_part(self, i):
        new_part = Turtle("square")
        new_part.penup()
        new_part.goto(i)
        self.snake_parts.append(new_part)

    def extend(self):
        self.new_part(self.snake_parts[-1].position())

    def move(self, speed):
        for parts in range(len(self.snake_parts)- 1, 0, -1):
                x = self.snake_parts[parts - 1].xcor()
                y = self.snake_parts[parts - 1].ycor()
                self.snake_parts[parts].goto(x, y)
        self.head.forward(speed)
            
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)