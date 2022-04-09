import scene
from button import Button
import gameplayScene
import currentScene
import json


class LevelsScene(scene.Scene):
    def __init__(self, curScene, gpScene):
        f = open("Levels/levels_info")
        dec = json.JSONDecoder()
        levels = int(dec.decode(s=f.read())["levels_amount"])
        f.close()
        self.levelsButtons = []
        for i in range(0, levels):
            self.levelsButtons.append(Button(300 + 140 * (i % 5),
                                             20 + 80 * (i // 5),
                                             120, 50, "Level "+str(i + 1), "level "+str(i + 1)))
            self.levelsButtons[i].addActionReceiver(self)
        self.backButton = Button(100, 100, 100, 50, "back", "menu")
        self.backButton.addActionReceiver(self)
        self.gameplayScene = gpScene
        self.curScene = curScene

    def to_menu(self):
        self.curScene.state = currentScene.CurrentScene.SCENE_MENU

    def to_gameplay(self, level):
        self.gameplayScene.startLevel(level)
        self.curScene.state = currentScene.CurrentScene.SCENE_GAMEPLAY

    def on_button(self, action):
        if action == "menu":
            self.to_menu()
        elif action[:5] == "level":
            self.to_gameplay(int(action[6:]))

    def draw(self):
        self.backButton.draw()
        for b in self.levelsButtons:
            b.draw()

    def update(self):
        self.backButton.update()
        for b in self.levelsButtons:
            b.update()
