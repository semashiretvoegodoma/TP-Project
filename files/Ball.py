import time
from math import copysign, sqrt
from random import random

import wrapper


class Ball:
    def __init__(self):
        self.x = 650.0
        self.y = 540.0
        self.radius = 10.0
        self.velocity_magnitude = 800.0
        self.velocityX = (random() - 0.5) * self.velocity_magnitude
        self.velocityY = 0
        self.calc_velocity_y(-1)
        self.collider = (-self.radius, -self.radius, self.radius, self.radius)
        self.walls = (300.0, 0.0, 1000.0, 700.0)

    def calc_velocity_y(self, sign):
        velocity_magnitude_squared = self.velocity_magnitude * self.velocity_magnitude
        velocity_x_squared = self.velocityX * self.velocityX
        self.velocityY = sign * sqrt(velocity_magnitude_squared - velocity_x_squared)

    def calc_velocity_x(self, sign):
        velocity_magnitude_squared = self.velocity_magnitude * self.velocity_magnitude
        velocity_y_squared = self.velocityY * self.velocityY
        self.velocityY = sign * sqrt(velocity_magnitude_squared - velocity_y_squared)

    def keep_inside(self, other_left, other_top, other_right, other_bottom):
        if other_top > self.y - self.radius:
            self.velocityY = abs(self.velocityY)
        if other_bottom < self.y + self.radius:
            self.velocityY = -abs(self.velocityY)
        if other_left > self.x - self.radius:
            self.velocityX = abs(self.velocityX)
        if other_right < self.x + self.radius:
            self.velocityX = -abs(self.velocityX)

    def keep_outside(self, brick):
        left = max(self.x - self.radius, brick.x)
        right = min(self.x + self.radius, brick.x + brick.width)
        top = max(self.y - self.radius, brick.y)
        bottom = min(self.y + self.radius, brick.y + brick.height)
        width = right - left
        height = bottom - top
        if width > 0 and height > 0:
            if width > height:
                self.velocityY = copysign(self.velocityY, self.y - (brick.y + brick.height / 2))
            else:
                self.velocityX = copysign(self.velocityX, self.x - (brick.x + brick.width / 2))

    def handle_bricks_collisions(self, bricks):
        for brick in bricks:
            self.keep_outside(brick)

    def handle_wall_collisions(self):
        self.keep_inside(*self.walls)

    def handle_slider_collisions(self, slider):
        left = max(self.x - self.radius, slider.x)
        right = min(self.x + self.radius, slider.x + slider.width)
        top = max(self.y - self.radius, slider.y)
        bottom = min(self.y + self.radius, slider.y + slider.height)
        width = right - left
        height = bottom - top
        if width > 0 and height > 0:
            if width > height and self.y < slider.y:
                self.velocityX = (random() - 0.5) * self.velocity_magnitude
                self.calc_velocity_y(-1)
            else:
                self.velocityY = random() * self.velocity_magnitude
                x_sign = +1 if self.x > slider.x else -1
                self.calc_velocity_x(x_sign)

    def handle_collisions(self, bricks, slider):
        self.handle_wall_collisions()
        self.handle_bricks_collisions(bricks)
        self.handle_slider_collisions(slider)

    def move(self):
        self.x += self.velocityX * wrapper.delta_time
        self.y += self.velocityY * wrapper.delta_time

    def update_without_moving(self, bricks, slider):
        self.handle_collisions(bricks, slider)

    def draw(self):
        wrapper.drawCircle((0, 30, 120), (round(self.x), round(self.y)), round(self.radius))
