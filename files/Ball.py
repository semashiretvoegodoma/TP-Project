import wrapper


class Ball:
    def __init__(self):
        self.x = 650
        self.y = 540
        self.radius = 20
        self.velocityX = 0
        self.velocityY = -10

    def handleCollisions(self, bricks, slider):
        if self.y > 680 or self.y < 20:
            self.velocityY *= -1

    def move(self):
        self.x += self.velocityX
        self.y += self.velocityY

    def update(self, bricks, slider):
        self.handleCollisions(bricks, slider)
        self.move()

    def draw(self):
        wrapper.drawCircle((0, 30, 120), (self.x, self.y), self.radius)
