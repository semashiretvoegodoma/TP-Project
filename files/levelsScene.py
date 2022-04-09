import scene
from button import Button
import gameplayScene
import currentScene


class LevelsScene(scene.Scene):
    def __init__(self, curScene, gpScene):
        self.levelsButtons = [Button(700, 20, 200, 50, "level 1", "level")]
        self.levelsButtons[0].addActionReceiver(self)
        self.backButton = Button(700, 100, 200, 50, "back", "menu")
        self.backButton.addActionReceiver(self)
        self.gameplayScene = gpScene
        self.curScene = curScene

    def toMenu(self):
        self.curScene.state = currentScene.CurrentScene.SCENE_MENU

    def toGameplay(self):
        self.gameplayScene.startLevel(1)
        self.curScene.state = currentScene.CurrentScene.SCENE_GAMEPLAY

    def on_button(self, action):
        if action == "level":
            self.toGameplay()
        elif action == "menu":
            self.toMenu()

    def draw(self):
        self.backButton.draw()
        for b in self.levelsButtons:
            b.draw()

    def update(self):
        self.backButton.update()
        for b in self.levelsButtons:
            b.update()
