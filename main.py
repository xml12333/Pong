from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from score import Score
s = Screen()
s.setup(width=800, height=600)
s.bgcolor("black")
s.title("Pong")
s.tracer(0)

p1 = Paddle((350, 0))
p2 = Paddle((-350, 0))
s.listen()
s.onkey(key="Up", fun=p1.up)
s.onkey(key="Down", fun=p1.down)
s.onkey(key="w", fun=p2.up)
s.onkey(key="s", fun=p2.down)
b = Ball()
score = Score()
game_on = True
speed = 0.1
while game_on:
    s.update()
    b.move()
    sleep(speed)
    b.check_y()
    if b.distance(p1) < 50 and b.xcor()>320 or b.distance(p2) < 50 and b.xcor()<-320:
        b.check_x()
        if speed >=0.01:
            speed -= 0.01
    if b.xcor()>420:
        b.reset()
        score.l_point()
        speed = 0.1
    if b.xcor()<-420:
        b.reset()
        score.r_point()
        speed = 0.1
s.exitonclick()
