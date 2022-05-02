import time
from math import copysign, sqrt
from random import random

import wrapper


class Ball:
    def __init__(self, gameplay_play_state):
        self.gameplay_play_state = gameplay_play_state
        self.x = 650.0
        self.y = 540.0
        self.radius = 10.0
        self.velocity_magnitude = 500.0
        self.velocityX = (random() - 0.5) * self.velocity_magnitude
        self.velocityY = 0
        self.calc_velocity_y(-1)
        self.collider = (-self.radius, -self.radius, self.radius, self.radius)
        self.walls = (300.0, 0.0, 1000.0, 700.0)
        self.is_meteor = False
        self.penetration = False
        self.is_additional = False
        self.exclude_additional = False
        wrapper.add_sound("bounce")

    def calc_velocity_y(self, sign):
        velocity_magnitude_squared = self.velocity_magnitude * self.velocity_magnitude
        velocity_x_squared = self.velocityX * self.velocityX
        self.velocityY = sign * sqrt(velocity_magnitude_squared - velocity_x_squared)

    def calc_velocity_x(self, sign):
        velocity_magnitude_squared = self.velocity_magnitude * self.velocity_magnitude
        velocity_y_squared = self.velocityY * self.velocityY
        self.velocityY = sign * sqrt(velocity_magnitude_squared - velocity_y_squared)

    def make_velocities_ok(self):
        if self.velocityX > self.velocity_magnitude * 0.9:
            self.velocityX = self.velocity_magnitude * 0.9
        if self.velocityY > self.velocity_magnitude * 0.9:
            self.velocityY = self.velocity_magnitude * 0.9
        if self.velocityX < - self.velocity_magnitude * 0.9:
            self.velocityX = - self.velocity_magnitude * 0.9
        if self.velocityY < - self.velocity_magnitude * 0.9:
            self.velocityY = - self.velocity_magnitude * 0.9

    def sound(self):
        wrapper.play_sound("bounce")

    def keep_inside(self, other_left, other_top, other_right, other_bottom):
        if other_top > self.y - self.radius:
            self.velocityY = abs(self.velocityY)
            return "top"
        if other_bottom < self.y + self.radius:
            self.velocityY = -abs(self.velocityY)
            return "bottom"
        if other_left > self.x - self.radius:
            self.velocityX = abs(self.velocityX)
            return "left"
        if other_right < self.x + self.radius:
            self.velocityX = -abs(self.velocityX)
            return "right"
        return None

    def keep_outside(self, brick):
        left = max(self.x - self.radius, brick.x)
        right = min(self.x + self.radius, brick.x + brick.width)
        top = max(self.y - self.radius, brick.y)
        bottom = min(self.y + self.radius, brick.y + brick.height)
        width = right - left
        height = bottom - top
        if width > 0 and height > 0:
            if self.is_meteor:
                if self.penetration:
                    pass
                else:
                    if width > height:
                        self.velocityY = copysign(self.velocityY, self.y - (brick.y + brick.height / 2))
                    else:
                        self.velocityX = copysign(self.velocityX, self.x - (brick.x + brick.width / 2))
                self.penetration = not self.penetration
            else:
                if width > height:
                    self.velocityY = copysign(self.velocityY, self.y - (brick.y + brick.height / 2))
                else:
                    self.velocityX = copysign(self.velocityX, self.x - (brick.x + brick.width / 2))
            return "impact"
        return None

    def handle_bricks_collisions(self, bricks):
        result = None
        for brick in bricks:
            if self.keep_outside(brick):
                result = "impact"
        return result

    def handle_wall_collisions(self):
        side = self.keep_inside(*self.walls)
        if side == "bottom":
            if self.is_additional:
                self.exclude_additional = True
            else:
                self.gameplay_play_state.to_lose()
        return side

    def handle_slider_collisions(self, slider):
        left = max(self.x - self.radius, slider.x)
        right = min(self.x + self.radius, slider.x + slider.width)
        top = max(self.y - self.radius, slider.y)
        bottom = min(self.y + self.radius, slider.y + slider.height)
        width = right - left
        height = bottom - top
        if width > 0 and height > 0:
            if width > height:  # front impact
                # self.velocityX = (random() - 0.5) * self.velocity_magnitude
                print(self.velocityX, " + ", slider.get_velocity())
                self.velocityX = self.velocityX + slider.get_velocity() / 5
                self.make_velocities_ok()
                self.calc_velocity_y(-1)
            else:  # side impact
                self.velocityY = random() * self.velocity_magnitude
                x_sign = +1 if self.x > slider.x else -1
                self.calc_velocity_x(x_sign)
            return "impact"
        return None

    def handle_collisions(self, bricks, slider):
        wall_result = self.handle_wall_collisions()
        brick_result = self.handle_bricks_collisions(bricks)
        slider_result = self.handle_slider_collisions(slider)
        if wall_result or brick_result or slider_result:
            self.sound()

    def move(self):
        self.x += self.velocityX * wrapper.delta_time
        self.y += self.velocityY * wrapper.delta_time

    def update_without_moving(self, bricks, slider):
        self.handle_collisions(bricks, slider)

    def draw(self):
        if not self.is_additional:
            wrapper.drawCircle((0, 30, 120), (round(self.x), round(self.y)), round(self.radius))
        else:
            wrapper.drawCircle((255, 130, 2), (round(self.x), round(self.y)), round(self.radius))
