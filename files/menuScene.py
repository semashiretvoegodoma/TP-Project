import wrapper
import scene
from button import Button
import currentScene


class MenuScene(scene.Scene):
    def __init__(self, curScene):
        self.playButton = Button(553, 253, 205, 70, "", "play")
        self.playButton.addActionReceiver(self)
        self.editorButton = Button(553, 353, 205, 70, "", "editor")
        self.editorButton.addActionReceiver(self)
        self.quitButton = Button(553, 453, 205, 70, "", "quit")
        self.quitButton.addActionReceiver(self)
        self.currentScene = curScene

    def draw(self):
        wrapper.loadImage("buttonStart")
        wrapper.loadImage("buttonEditor")
        wrapper.loadImage("buttonQuit")

        wrapper.drawImage("buttonStart", 550, 250, 213, 78)
        wrapper.drawImage("buttonEditor", 550, 350, 213, 78)
        wrapper.drawImage("buttonQuit", 550, 450, 213, 78)

    def update(self):
        self.playButton.update()
        self.editorButton.update()
        self.quitButton.update()

    def toLevels(self):
        self.currentScene.state = currentScene.CurrentScene.SCENE_LEVELS

    def ExitGame(self):
        wrapper.quit()

    def toEditor(self):
        self.currentScene.state = currentScene.CurrentScene.SCENE_EDITOR

    def on_button(self, action):
        if action == "quit":
            self.ExitGame()
        elif action == "play":
            self.toLevels()
        elif action == "editor":
            self.toEditor()
