from turtle import Turtle, Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
import time

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
SCREEN_UPPER_LIMIT = 280
SCREEN_LOWER_LIMIT = -280
SCREEN_RIGHT_LIMIT = 380
SCREEN_LEFT_LIMIT = -380

screen = Screen()
screen.bgcolor('black')
screen.title('Pong')
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(r_paddle.go_up, 'Up')
screen.onkeypress(r_paddle.go_down, 'Down')
screen.onkeypress(l_paddle.go_up, 'w')
screen.onkeypress(l_paddle.go_down, 's')


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    scoreboard.update_scoreboard()
    ball.move()

    if ball.ycor() > SCREEN_UPPER_LIMIT or ball.ycor() < SCREEN_LOWER_LIMIT:
        ball.bounce_y()

    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    if (ball.xcor() > SCREEN_RIGHT_LIMIT):
        ball.reset_position()
        scoreboard.increase_score_left()

    if (ball.xcor() < SCREEN_LEFT_LIMIT):
        ball.reset_position()
        scoreboard.increase_score_right()

    print(ball.move_speed)
screen.exitonclick()
