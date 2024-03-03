from turtle import Turtle

GAP_X, GAP_Y = [0.9, 0.8]

class Block(Turtle):

    def __init__(self, color, x_pos, y_pos, width, height, id):
        super().__init__()
        self.shape("square")
        self.penup()
        self.setposition(x=x_pos, y=y_pos)
        self.color(color)
        self.shapesize(stretch_len=width/20*GAP_X, stretch_wid=height/20*GAP_Y) # Default size 20px
        self.id = id
        # Coordinates of edges to Detect collision with ball ingame
        self.left_bottom = {"x": round(x_pos - width / 2), "y": round(y_pos - height / 2)}
        self.left_top = {"x": round(x_pos - width / 2), "y": round(y_pos + height / 2)}
        self.right_top = {"x": round(x_pos + width / 2), "y": round(y_pos + height / 2)}
        self.right_bottom = {"x": round(x_pos + width / 2), "y": round(y_pos - height / 2)}

    def destroy(self):
        self.hideturtle()
        self.clear()