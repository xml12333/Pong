from turtle import Turtle
MOVE_SIZE = 20
class Paddle(Turtle):
    def __init__(self,init_pos):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(5.0, 1.0, 1)
        self.speed("fastest")
        self.goto(init_pos)

    def up(self):
        self.sety(self.pos()[1]+MOVE_SIZE)

    def down(self):
        self.sety(self.pos()[1]-MOVE_SIZE)
