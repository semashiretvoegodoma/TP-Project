import wrapper
import scene
from button import Button
import currentScene


class MenuScene(scene.Scene):
    def __init__(self, curScene):
        self.playButton = Button((1300 / 2) - 50, 300, 100, 30, "Play", "play")
        self.playButton.addActionReceiver(self)
        self.quitButton = Button((1300 / 2) - 50, 400, 100, 30, "Quit", "quit")
        self.quitButton.addActionReceiver(self)
        self.currentScene = curScene

    def draw(self):
        self.playButton.draw()
        self.quitButton.draw()

    def update(self):
        self.playButton.update()
        self.quitButton.update()

    def toLevels(self):
        self.currentScene.state = currentScene.CurrentScene.SCENE_LEVELS

    def ExitGame(self):
        wrapper.quit()

    def onButton(self, action):
        if action == "quit":
            self.ExitGame()
        elif action == "play":
            self.toLevels()
