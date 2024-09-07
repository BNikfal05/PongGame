from turtle import Turtle

PADDLE_LENGTH = 20 / 20
PADDLE_WIDTH = 100 / 20


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.turtlesize(PADDLE_WIDTH, PADDLE_LENGTH)
        self.color('white')
        self.penup()
        self.goto(position)
        self.speed('fastest')
        self.x_move = 20
        self.y_move = 20

    def go_up(self):
        self.new_y = self.ycor() + self.y_move
        self.goto(self.xcor(), self.new_y)

    def go_down(self):
        self.new_y = self.ycor() - self.y_move
        self.goto(self.xcor(), self.new_y)
