import os

import scene
from button import Button
import gameplayScene
import currentScene
import json


class LevelsScene(scene.Scene):
    def __init__(self, curScene, gpScene):
        self.refresh_level_buttons()
        self.backButton = Button(100, 100, 100, 50, "back", "menu")
        self.backButton.addActionReceiver(self)
        self.gameplayScene = gpScene
        self.curScene = curScene

    def to_menu(self):
        self.curScene.state = currentScene.CurrentScene.SCENE_MENU

    def to_gameplay(self, level):
        self.gameplayScene.startLevel(level)
        self.curScene.state = currentScene.CurrentScene.SCENE_GAMEPLAY

    def refresh_level_buttons(self):
        level_filenames = os.listdir("Levels")
        self.levelsButtons = []
        i = 0
        for filename in level_filenames:
            print(filename)
            self.levelsButtons.append(Button(300 + 140 * (i % 5),
                                             20 + 80 * (i // 5),
                                             120, 50, filename, "level " + str(i + 1)))
            self.levelsButtons[i].addActionReceiver(self)
            i += 1

    def on_button(self, action):
        if action == "menu":
            self.to_menu()
        elif action[:5] == "level":
            self.to_gameplay(action[6:])

    def draw(self):
        self.backButton.draw()
        for b in self.levelsButtons:
            b.draw()

    def update(self):
        self.backButton.update()
        for b in self.levelsButtons:
            b.update()
