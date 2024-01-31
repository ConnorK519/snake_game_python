from turtle import Turtle

MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.snake_parts = []
        self.create_snake()
        self.head = self.snake_parts[0]

    def create_snake(self):
        start_locations = [(0, 0), (-20, 0), (-40, 0)]
        for pos in start_locations:
            self.add_part(pos)

    def move(self):
        for num in range(len(self.snake_parts) - 1, 0, -1):
            new_x = self.snake_parts[num - 1].xcor()
            new_y = self.snake_parts[num - 1].ycor()
            self.snake_parts[num].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def add_part(self, coords):
        snake = Turtle("square")
        snake.penup()
        snake.color("green")
        snake.setpos(coords)
        self.snake_parts.append(snake)

    def grow(self):
        self.add_part(self.snake_parts[-1].position())

    def reset(self):
        for part in self.snake_parts:
            part.goto(1000, 1000)
        self.snake_parts.clear()
        self.create_snake()
        self.head = self.snake_parts[0]
