from turtle import Screen
from paddle import Paddle
from ball import Ball
from block_manager import BlockManager
from message import Message
import time

# ========== CONSTANTS ========== #
WIDTH, HEIGHT = [1000, 1000]
ROWS, BLOCKS_PER_ROW = [5, 8] # recommended: max 10 x 12

# ========== SETTING ========== #
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)  # disable automatic screen updates

paddle = Paddle(WIDTH, HEIGHT)
ball = Ball(HEIGHT)
block_manager = BlockManager(WIDTH, HEIGHT, ROWS, BLOCKS_PER_ROW)

# ========== INGAME CONTROLS ========== #
screen.listen()
screen.onkey(paddle.go_right, "Right")
screen.onkey(paddle.go_left, "Left")

# ========== GAME LOGIC ========== #
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with block
    for block in block_manager.all_blocks:
        # Collision with Block bottom
        if (block.left_bottom["x"] <= ball.xcor() <= block.right_bottom["x"])  and (block.left_bottom["y"] - 15) <= ball.ycor() <= (block.left_bottom["y"]):
            ball.bounce_y()
            block_manager.delete_block(block)
            block.destroy()
        # Detect collision with block-left
        if (block.left_bottom["y"] <= ball.ycor() <= block.left_top["y"]) and (block.left_bottom["x"] - 15) <= ball.xcor() <= (block.left_bottom["x"]):
            ball.bounce_x()
            block_manager.delete_block(block)
            block.destroy()
        # Detect collision with block-top
        if (block.left_top["x"] <= ball.xcor() <= block.right_top["x"]) and (block.left_top["y"] + 15) >= ball.ycor() >= (block.left_top["y"] ):
            ball.bounce_y()
            block_manager.delete_block(block)
            block.destroy()
        # Detect collision with block-right
        if (block.right_bottom["y"] <= ball.ycor() <= block.right_top["y"]) and (block.right_bottom["x"] + 15) >= ball.xcor() >= (block.right_bottom["x"]):
            ball.bounce_x()
            block_manager.delete_block(block)
            block.destroy()

    # Detect collision with vertical wall
    if ball.xcor() < - WIDTH/2 + 10 or ball.xcor() > WIDTH/2 - 20:
        ball.bounce_x()

    # Detect collision with horizontal wall
    if ball.ycor() > HEIGHT / 2 - 20:
        ball.bounce_y()

    # Detect missing the paddle
    if ball.ycor() < - HEIGHT / 2 + 20:
        text = f"You lost!\nDestroyed blocks: {ROWS*BLOCKS_PER_ROW - len(block_manager.all_blocks)}/{ROWS*BLOCKS_PER_ROW}"
        message = Message(int(WIDTH/30), text)
        game_is_on = False

    # Ball hits paddle (left side)
    if ball.ycor() < paddle.ycor() + 20 and (ball.xcor() >= paddle.xcor() - 100 and ball.xcor() < paddle.xcor()):
        ball.bounce_paddle_left()

    # Ball hits paddle (right side)
    if ball.ycor() < paddle.ycor() + 20 and (ball.xcor() <= paddle.xcor() + 100 and ball.xcor() >= paddle.xcor()):
        ball.bounce_paddle_right()

    if len(block_manager.all_blocks) == 0:
        text = f"You won!"
        message = Message(int(WIDTH / 30), text)
        game_is_on = False

screen.exitonclick()


