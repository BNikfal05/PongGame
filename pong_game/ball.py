from turtle import Turtle

BALL_WIDTH = 20 / 20
BALL_LENGTH = 20 / 20


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.turtlesize(BALL_WIDTH, BALL_LENGTH)
        self.move_speed = 0.1
        self.x_move = 10
        self.y_move = 10

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9
