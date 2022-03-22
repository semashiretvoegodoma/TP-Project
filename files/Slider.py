import wrapper


class Slider(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def update(self):
        if wrapper.arrowLeft():
            self.x -= 7
        if wrapper.arrowRight():
            self.x += 7

    def draw(self):
        wrapper.drawRect((40, 240, 75), (self.x, self.y, self.width, self.height))
