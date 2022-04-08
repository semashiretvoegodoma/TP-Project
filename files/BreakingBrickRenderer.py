import wrapper


class BreakingBrickRenderer:
    def __init__(self, renderer):
        self.brick_renderer = renderer
        self.degree = 0.0
        self.speed = 4.0

    def draw(self):
        red = 150.0 + self.degree * (255.0 - 150.0)
        green = 30.0 + self.degree * (255.0 - 30.0)
        blue = 20.0 + self.degree * (255.0 - 20.0)
        x = self.brick_renderer.brick.x
        y = self.brick_renderer.brick.y
        width = self.brick_renderer.brick.width
        height = self.brick_renderer.brick.height
        wrapper.drawRect((red, green, blue), (x, y, width, height))

    def update(self):
        if (self.degree + self.speed * wrapper.delta_time) < 1.0:
            self.degree = self.degree + self.speed * wrapper.delta_time
        else:
            self.degree = 1.0
            self.brick_renderer.to_broken()
