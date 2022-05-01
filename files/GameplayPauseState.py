import wrapper
from button import Button


class GameplayPauseState:
    def __init__(self, gameplay_scene):
        self.gameplay_scene = gameplay_scene
        self.resume_button = Button(900, 200, 270, 112, "", "resume")
        self.quit_button = Button(692, 350, 475, 112, "", "quit")
        self.resume_button.addActionReceiver(self)
        self.quit_button.addActionReceiver(self)

    def on_button(self, action):
        if action == "resume":
            self.gameplay_scene.resume()
        elif action == "quit":
            self.gameplay_scene.to_levels()

    def draw(self):
        wrapper.loadImage("backgroundPause")
        wrapper.drawImage("backgroundPause", 0, 0, 1300, 700)
        wrapper.loadImage("buttonResume")
        wrapper.drawImage("buttonResume", 900, 200, 270, 112)
        wrapper.loadImage("buttonQuitToLevels")
        wrapper.drawImage("buttonQuitToLevels", 692, 350, 475, 112)

    def update(self):
        self.resume_button.update()
        self.quit_button.update()
