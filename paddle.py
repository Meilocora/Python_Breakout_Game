from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.penup()
        self.shape("square")
        self.setposition(x=0, y=-screen_height/2+screen_height/20)
        self.color("blue")
        self.shapesize(stretch_len=screen_width/100, stretch_wid=1)
        self.speed = screen_width / 20
        self.screen_width = screen_width

    def go_right(self):
        if self.xcor() <= (self.screen_width / 2) - self.screen_width/8 :
            new_x = self.xcor() + self.speed
            self.goto(x=new_x, y=self.ycor())

    def go_left(self):
        if self.xcor() >= (- self.screen_width / 2) + self.screen_width/8 :
            new_x = self.xcor() - self.speed
            self.goto(x=new_x, y=self.ycor())