import time
from math import copysign
import wrapper


class Ball:
    def __init__(self):
        self.x = 650.0
        self.y = 540.0
        self.radius = 10.0
        self.velocityX = 200.0
        self.velocityY = -600.0
        self.collider = (-self.radius, -self.radius, self.radius, self.radius)
        self.walls = (300.0, 0.0, 1000.0, 700.0)
        self.lastUpdateTime = time.time()

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

    def handle_collisions(self, bricks, slider):
        self.handle_wall_collisions()
        self.handle_bricks_collisions(bricks)

    def move(self):
        deltaTime = time.time() - self.lastUpdateTime
        self.lastUpdateTime = time.time()
        self.x += self.velocityX * deltaTime
        self.y += self.velocityY * deltaTime

    def update(self, bricks, slider):
        self.handle_collisions(bricks, slider)
        self.move()

    def draw(self):
        wrapper.drawCircle((0, 30, 120), (round(self.x), round(self.y)), round(self.radius))
