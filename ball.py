from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.shapesize(1.0,1.0)
        self.x_move = 10
        self.y_move = 10
    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def check_y(self):
        if self.ycor() > 280 or self.ycor() < -280:
            self.y_move *= -1

    def check_x(self):
        self.x_move *= -1

    def reset(self):
        self.goto(0,0)
        self.check_x()


