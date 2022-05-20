import wrapper


class Brick(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def update(self, ball):
        pass

    def draw(self):
        wrapper.drawRect((150, 20, 30), (self.x, self.y, self.width, self.height))
