import wrapper


class Ball:
    def __init__(self):
        self.x = 650
        self.y = 540
        self.radius = 20
        self.velocityX = 5
        self.velocityY = -10
        self.leftCollider = (0, 0, 10, 40)
        self.rightCollider = (30, 0, 10, 40)
        self.topCollider = (0, 0, 40, 10)
        self.bottomCollider = (0, 30, 40, 10)

    def handleCollisions(self, bricks, slider):
        if self.y > 680 or self.y < 20:
            self.velocityY *= -1
        if self.x > 920 or self.x < 320:
            self.velocityX *= -1


    def move(self):
        self.x += self.velocityX
        self.y += self.velocityY

    def update(self, bricks, slider):
        self.handleCollisions(bricks, slider)
        self.move()

    def draw(self):
        wrapper.drawCircle((0, 30, 120), (self.x, self.y), self.radius)
