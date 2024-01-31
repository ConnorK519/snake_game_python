from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.get_high_score()
        self.update()

    def get_high_score(self):
        file = open("high_score.txt")
        self.high_score = file.read()
        file.close()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}", False, "center", ('Arial', 12, 'normal'))

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            file = open("high_score.txt", "w")
            file.write(str(self.high_score))
            file.close()
        self.score = 0
        self.update()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", False, "center", ('Arial', 12, 'normal'))

    def increase_score(self):
        self.score += 1
        self.update()
