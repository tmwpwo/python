from turtle import *
from sanke import Sanke
import time

scren = Screen()
scren.setup(width=500, height=500)
scren.bgcolor("white")
scren.title("SANKE")
scren.tracer(0)


snake = Sanke()


game = True
while game:
    scren.update()
    time.sleep(0.9)

    snake.move()



scren.exitonclick()
