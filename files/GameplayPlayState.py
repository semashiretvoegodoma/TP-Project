import json
import wrapper
import random

import wrapper
from Ball import Ball
from Slider import Slider
from Brick import Brick
from button import Button

class GameplayPlayState:
    def __init__(self, gameplay_scene):
        self.gameplay_scene = gameplay_scene
        self.ball = Ball(self)
        self.additional_balls = []
        self.bricks = []
        self.slider = Slider(600.0, 600.0, 100.0, 20.0, 300.0, 1000.0, 800.0)
        self.pause_button = Button(35, 100, 200, 83, "", "pause", True)
        self.pause_button.addActionReceiver(self)
        self.build_level_of_version = {
            "1": self.build_level_v1
        }
        self.time_of_bonuses = {"slider" : -1.0, "ball" : -1.0, "meteor" : -1.0, "added_balls" : -1.0}

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
    
    def try_to_generate_bonus(self):
        generated_int = random.randint(0, 7)
        if generated_int == 0:
            if self.slider.width == 100:
                self.slider.width += 50
            self.time_of_bonuses["slider"] = 0.0
        if generated_int == 1:
            if self.ball.radius == 10.0:
                self.ball.radius *= 5.0
            self.time_of_bonuses["ball"] = 0.0
        if generated_int == 2:
            if not self.ball.is_meteor:
                self.ball.is_meteor = True
                self.ball.penetration = True
            self.time_of_bonuses["meteor"] = 0.0
        if generated_int == 3:
            self.additional_balls.append(Ball(self))
            self.additional_balls[len(self.additional_balls)-1].is_additional = True
            self.time_of_bonuses["added_balls"] = 0.0

    def check_bonus(self, delta_time):
        TIME_OF_ACTIVATED_BONUS = 5.0
        if self.time_of_bonuses["slider"] != -1.0:
            self.time_of_bonuses["slider"] += delta_time
            if self.time_of_bonuses["slider"] > TIME_OF_ACTIVATED_BONUS:
                self.slider.width = 100
                self.time_of_bonuses["slider"] = -1.0
        if self.time_of_bonuses["ball"] != -1.0:
            self.time_of_bonuses["ball"] += delta_time
            if self.time_of_bonuses["ball"] > TIME_OF_ACTIVATED_BONUS:
                self.ball.radius = 10.0
                self.time_of_bonuses["ball"] = -1.0
        if self.time_of_bonuses["meteor"] != -1.0:
            self.time_of_bonuses["meteor"] += delta_time
            if self.time_of_bonuses["meteor"] > TIME_OF_ACTIVATED_BONUS:
                self.ball.is_meteor = False
                self.ball.penetration = False
                self.time_of_bonuses["meteor"] = -1.0
        if self.time_of_bonuses["added_balls"] != -1.0:
            self.time_of_bonuses["added_balls"] += delta_time
            if self.time_of_bonuses["added_balls"] > TIME_OF_ACTIVATED_BONUS:
                self.additional_balls.clear()
                self.time_of_bonuses["added_balls"] = -1.0

    def to_win(self):
        if len(self.additional_balls) != 0:
            self.additional_balls.clear()
        self.time_of_bonuses = {"slider" : -1.0, "ball" : -1.0, "meteor" : -1.0, "added_balls" : -1.0}
        self.gameplay_scene.to_win()

    def to_lose(self):
        if len(self.additional_balls) != 0:
            self.additional_balls.clear()
        self.time_of_bonuses = {"slider" : -1.0, "ball" : -1.0, "meteor" : -1.0, "added_balls" : -1.0}
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
        if len(self.additional_balls) != 0:
            for i in range(len(self.additional_balls)):
                self.additional_balls[i].update_without_moving(bricks_for_ball, self.slider)
        for brick in self.bricks:
            state_brick = brick.update(self.ball)
            if len(self.additional_balls) != 0:
                for i in range(len(self.additional_balls)):
                    brick.update(self.additional_balls[i])
            if state_brick:
                self.try_to_generate_bonus()
        self.slider.update()
        self.ball.move()
        if len(self.additional_balls) != 0:
            tmp = []
            for i in range(len(self.additional_balls)):
                if not self.additional_balls[i].exclude_additional:
                    tmp.append(self.additional_balls[i])
            if len(tmp) == 0:
                self.time_of_bonuses["added_balls"] = -1.0
            self.additional_balls = tmp
            for i in range(len(self.additional_balls)):
                self.additional_balls[i].move()
        self.pause_button.update()
        self.check_bonus(wrapper.delta_time)

    def draw(self):
        wrapper.loadImage("backgroundPlay")
        wrapper.drawImage("backgroundPlay", 0, 0, 1300, 700)
        self.ball.draw()
        if len(self.additional_balls) != 0:
            for i in range(len(self.additional_balls)):
                self.additional_balls[i].draw()
        self.slider.draw()
        for brick in self.bricks:
            brick.draw()
        wrapper.loadImage("buttonPause")
        wrapper.drawImage("buttonPause", 35, 100, 200, 83)
