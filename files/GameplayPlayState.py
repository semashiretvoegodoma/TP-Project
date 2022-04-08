from Ball import Ball
from Slider import Slider
from Brick import Brick


class GameplayPlayState(object):
    def __init__(self):
        self.ball = Ball()
        self.bricks = []
        self.slider = Slider(600.0, 600.0, 100.0, 20.0, 300.0, 1000.0, 800.0)

    def buildLevel(self):
        for brick in self.bricks:
            del brick

        for i in range(1, 9):
            for j in range(1, 10):
                if ((i+j) % 7) == 0:
                    self.bricks.append(Brick(300 + 70 * i, 30 * j, 70, 30))


    def update(self):
        self.ball.update(self.bricks, self.slider)
        for brick in self.bricks:
            brick.update(self.ball)
        self.slider.update()

    def draw(self):
        self.ball.draw()
        self.slider.draw()
        for brick in self.bricks:
            brick.draw()
