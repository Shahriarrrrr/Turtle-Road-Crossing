from turtle import Turtle, Screen


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.left(90)
        self.goto(0, -250)
        self.shape("turtle")
        self.move()

    def move(self):
        self.forward(10)
