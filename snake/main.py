from turtle import *
import time
import snake
import food
import score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("snake")
screen.tracer(0)
speed = 20


snake = snake.Snake()
food = food.Food()
scoreboard =  score.Scoreboard()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_on = True 
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move(speed)

    if snake.head.distance(food) < 15:
        food.eaten()
        scoreboard.points()
        snake.extend()
        
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        game_on = False
        scoreboard.the_end()

    # for part in snake.snake_parts:


screen.exitonclick()
