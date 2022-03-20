

class GameplayPlayState(object):
    def __init__(self):
        self.ball = Ball()
        self.bricks = []
        for i in range(0,10):
            for j in range(0, 10):
                self.bricks.append(Brick(300 + 70*i, 30*j, 70, 30))
        self.slider = Slider(600, 600, 100, 20)

    def buildLevel(self):
        for brick in self.bricks:
            del brick

        for i in range(0, 10):
            for j in range(0, 10):
                self.bricks.append(Brick(300 + 70 * i, 30 * j, 70, 30))

