import wrapper


class Slider(object):
    def __init__(self, x, y, width, height, leftBoundary, rightBoundary, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.leftBoundary = leftBoundary
        self.rightBoundary = rightBoundary
        self.speed = speed

    def update(self):
        if wrapper.arrowLeft():
            self.x -= self.speed * wrapper.deltaTime()
        if wrapper.arrowRight():
            self.x += self.speed * wrapper.deltaTime()
        self.x = max(self.leftBoundary, min(self.rightBoundary - self.width, self.x))

    def draw(self):
        wrapper.drawRect((40, 240, 75), (self.x, self.y, self.width, self.height))
