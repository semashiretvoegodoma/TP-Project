import wrapper


class SolidBrickRenderer:
    def __init__(self, renderer):
        self.brick_renderer = renderer

    def draw(self):
        x = self.brick_renderer.brick.x
        y = self.brick_renderer.brick.y
        width = self.brick_renderer.brick.width
        height = self.brick_renderer.brick.height
        wrapper.drawRect((150, 20, 30), (x, y, width, height))

    def update(self):
        pass
