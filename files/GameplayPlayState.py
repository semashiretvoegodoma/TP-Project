from Ball import Ball
from Slider import Slider
from Brick import Brick


class GameplayPlayState:
    def __init__(self, gameplay_scene):
        self.gameplay_scene = gameplay_scene
        self.ball = Ball(self)
        self.bricks = []
        self.slider = Slider(600.0, 600.0, 100.0, 20.0, 300.0, 1000.0, 800.0)

    def loadLevel(self, levelNum):
        pass

    def buildLevel(self):
        self.ball = Ball(self)
        self.bricks = []
        self.slider = Slider(600.0, 600.0, 100.0, 20.0, 300.0, 1000.0, 800.0)

        for i in range(1, 9):
            for j in range(1, 10):
                if ((i+j) % 7) == 0:
                    self.bricks.append(Brick(300 + 70 * i, 30 * j, 70, 30))

    def to_win(self):
        self.gameplay_scene.to_win()

    def to_lose(self):
        self.gameplay_scene.to_lose()

    def update(self):
        bricks_for_ball = []
        for brick in self.bricks:
            if brick.state == brick.SOLID:
                bricks_for_ball.append(brick)
        if len(bricks_for_ball) == 0:
            self.to_win()
        self.ball.update_without_moving(bricks_for_ball, self.slider)
        for brick in self.bricks:
            brick.update(self.ball)
        self.slider.update()
        self.ball.move()

    def draw(self):
        self.ball.draw()
        self.slider.draw()
        for brick in self.bricks:
            brick.draw()
