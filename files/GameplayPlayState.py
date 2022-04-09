import json

from Ball import Ball
from Slider import Slider
from Brick import Brick
from button import Button


class GameplayPlayState:
    def __init__(self, gameplay_scene):
        self.gameplay_scene = gameplay_scene
        self.ball = Ball(self)
        self.bricks = []
        self.slider = Slider(600.0, 600.0, 100.0, 20.0, 300.0, 1000.0, 800.0)
        self.pause_button = Button(100, 100, 100, 40, "Pause", "pause")
        self.pause_button.addActionReceiver(self)
        self.build_level_of_version = {
            "1":self.build_level_v1
        }

    def loadLevel(self, level):
        f = open("Levels/" + str(level))
        dec = json.JSONDecoder()
        self.level_info = dec.decode(f.read())

    def buildLevel(self):
        try:
            level_version = self.level_info["game_version"]
        except AttributeError:
            print("ERROR: tried to build level, but didn't load it!")
            return
        if level_version in self.build_level_of_version.keys():
            self.build_level_of_version[level_version](self.level_info)
        else:
            self.build_error_level()

    def build_error_level(self):
        self.ball = Ball(self)
        self.bricks = []
        self.slider = Slider(600.0, 600.0, 100.0, 20.0, 300.0, 1000.0, 800.0)
        error_level = [
            "# #  ###  ##    #   ###  ###",
            "# #  # #  # #  # #   #   #  ",
            "# #  ###  # #  ###   #   ###",
            "# #  #    # #  # #   #   #  ",
            "###  #    ##   # #   #   ###"
        ]
        brick_y = 0
        for line in error_level:
            brick_y += 40
            brick_x = 300
            for char in line:
                if not char == " ":
                    self.bricks.append(Brick(brick_x, brick_y, 20, 40))
                brick_x += 20

    def build_level_v1(self, level_info):
        self.ball = Ball(self)
        self.bricks = []
        self.slider = Slider(600.0, 600.0, 100.0, 20.0, 300.0, 1000.0, 800.0)

        for brick_info in level_info["bricks"]:
            self.bricks.append(Brick(brick_info[0],
                                     brick_info[1],
                                     brick_info[2],
                                     brick_info[3]))

    def to_win(self):
        self.gameplay_scene.to_win()

    def to_lose(self):
        self.gameplay_scene.to_lose()

    def to_pause(self):
        self.gameplay_scene.to_pause()

    def on_button(self, action):
        if action == "pause":
            self.to_pause()

    def update(self):
        bricks_for_ball = []
        for brick in self.bricks:
            if brick.state == brick.SOLID:
                bricks_for_ball.append(brick)
        if len(bricks_for_ball) == 0:
            self.to_win()
        self.ball.update_without_moving(bricks_for_ball, self.slider)
        for brick in self.bricks:
            brick.update(self.ball)
        self.slider.update()
        self.ball.move()
        self.pause_button.update()

    def draw(self):
        self.ball.draw()
        self.slider.draw()
        for brick in self.bricks:
            brick.draw()
        self.pause_button.draw()
