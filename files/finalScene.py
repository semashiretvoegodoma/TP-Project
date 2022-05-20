import random
import time
import math

import scene
import wrapper


class FinalWinScene(scene.Scene):
    def __init__(self, current_scene):
        self.current_scene = current_scene
        self.creators = ["STEVE", "SIMON", "YAROMIR"]
        random.shuffle(self.creators)
        self.time_moment = time.time()

    def draw(self):
        wrapper.loadImage("background")
        wrapper.drawImage("background", 0, 0, 1300, 700)
        wrapper.drawText("YOU WENT THROUGH THE GAME!", (253, 203, 23), 70, "Arial", 60, 80)
        red = int(128 + 128 * math.sin((time.time() - self.time_moment) * 1.6564))
        green = int(128 + 128 * math.sin((time.time() - self.time_moment) * 2.0566))
        blue = int(128 + 128 * math.sin((time.time() - self.time_moment) * 3.6563))
        size = int(50 + 40 * math.sin((time.time() - self.time_moment) * 1.6))
        x = int(300 + 300 * math.sin(time.time() - self.time_moment - 5))
        y = int(300 + 200 * math.sin((time.time() - self.time_moment - 4) * 1.1))
        wrapper.drawText("CREATORS:", (red, green, blue), size, "Comic Sans", x, y)
        fonts = ["Comic Sans", "Courier", "Arial", "Verdana"]
        random.shuffle(fonts)
        wrapper.drawText(self.creators[0], (255, 0, 0), 35, fonts[0], 320, 360)
        wrapper.drawText(self.creators[1], (0, 200, 0), 35, fonts[1], 320, 420)
        wrapper.drawText(self.creators[2], (0, 0, 255), 35, fonts[2], 320, 480)

    def update(self):
        if wrapper.mouse_just_got_down:
            self.current_scene.state = self.current_scene.SCENE_MENU
