from turtle import Turtle

START_POSITION = (0, -280)
MOVE_DISTANCE = 13
FINISH_LINE = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("gray")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)
    def go_down(self):
        self.backward(MOVE_DISTANCE)
    def go_right(self):
        self.right(MOVE_DISTANCE)
    def go_left(self):
        self.left(MOVE_DISTANCE)
    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE:
            return True
        else:
            return False

    def go_to_start(self):
        self.goto(START_POSITION)