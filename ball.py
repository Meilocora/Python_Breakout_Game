from turtle import Turtle

class Ball(Turtle):

    def __init__(self, screen_height):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.setposition(x=0, y=-screen_height/3)
        self.color("white")
        self.speed(10)
        self.x_move = 5
        self.y_move = 10
        self.move_speed = 0.05

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def bounce_paddle_left(self):
        self.x_move = -5
        self.y_move = 10

    def bounce_paddle_right(self):
        self.x_move = 5
        self.y_move = 10
