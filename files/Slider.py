import time

import wrapper


class Slider:
    def __init__(self, x, y, width, height, leftBoundary, rightBoundary, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.leftBoundary = leftBoundary
        self.rightBoundary = rightBoundary
        self.speed = speed
        self.last_mouse_pos = wrapper.mouse_pos()
        self.last_x = x

    def arrow_control(self):
        if wrapper.arrowLeft():
            self.x -= self.speed * wrapper.delta_time
        if wrapper.arrowRight():
            self.x += self.speed * wrapper.delta_time

    def mouse_control(self):
        self.x += wrapper.mouse_pos()[0] - self.last_mouse_pos[0]
        self.last_mouse_pos = wrapper.mouse_pos()

    def get_velocity(self):
        return (self.x - self.last_x) / wrapper.delta_time

    def update(self):
        self.last_x = self.x
        if wrapper.mouse_pos() == self.last_mouse_pos:
            self.arrow_control()
        else:
            self.mouse_control()
        self.x = max(self.leftBoundary, min(self.rightBoundary - self.width, self.x))

    def draw(self):
        wrapper.drawRect((40, 240, 75), (self.x, self.y, self.width, self.height))
