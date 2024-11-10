from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Monaco", 15, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.score = 0
        self.high_score = self.read_file()
        self.hideturtle()
        self.update_scoreboard()

    def read_file(self):
        with open("data.txt", "r") as file:
            return int(file.read())

    def write_file(self, high_score):
        with open("data.txt", "w") as file:
            file.write(str(high_score))

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_file(self.high_score)
        self.score = 0
        self.update_scoreboard()

    def get_score(self):
        self.score += 1
        self.update_scoreboard()
