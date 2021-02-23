from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 360


class Snake:
    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_body(position)

    def add_body(self, position):
        snake = Turtle("square")
        snake.penup()
        snake.color("white")
        snake.goto(position)
        self.snakes.append(snake)

    def extend_snake(self):
        self.add_body(self.snakes[-1].position())

    def move(self):
        length_segments = len(self.snakes)
        for num_segment in range(length_segments - 1, 0, -1):
            new_x = self.snakes[num_segment - 1].xcor()
            new_y = self.snakes[num_segment - 1].ycor()
            self.snakes[num_segment].goto(new_x, new_y)
        self.snakes[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
