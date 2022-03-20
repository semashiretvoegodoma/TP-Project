class Ball:
    def __init__(self):
        self.x = 650
        self.y = 540
        self.radius = 20
        self.velocityX = 0
        self.velocityY = -10

    def handleCollisions(self, bricks, slider):
        pass

    def move(self):
        self.x += self.velocityX
        self.y += self.velocityY

    def update(self, bricks, slider):
        self.handleCollisions(bricks, slider)
        self.move()
