from turtle import Turtle

class Message(Turtle):

    def __init__(self, size, message):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.write_message(size, message)

    def write_message(self, size, message):
        self.clear()
        self.goto(0, -size*5)
        self.write(message, align="center", font=("Courier", size, "normal"))