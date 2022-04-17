from BrickRenderer import BrickRenderer
import wrapper


class Brick(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.SOLID = 0
        self.BROKEN = 1
        self.state = self.SOLID
        self.renderer = BrickRenderer(self)
        wrapper.add_sound("explosion")

    def sound(self):
        wrapper.play_sound("explosion")

    def update(self, ball):
        left = max(self.x, ball.x - ball.radius)
        right = min(self.x + self.width, ball.x + ball.radius)
        top = max(self.y, ball.y - ball.radius)
        bottom = min(self.y + self.height, ball.y + ball.radius)
        width = right - left
        height = bottom - top
        if width > 0 and height > 0 and self.state == self.SOLID:
            self.state = self.BROKEN
            self.renderer.to_breaking()
            self.sound()
        self.renderer.update()

    def draw(self):
        self.renderer.draw()
