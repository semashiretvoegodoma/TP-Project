import wrapper
from button import Button


class GameplayPauseState:
    def __init__(self, gameplay_scene):
        self.gameplay_scene = gameplay_scene
        self.resume_button = Button(600, 400, 100, 50, "Resume", "resume")
        self.resume_button.addActionReceiver(self)

    def on_button(self, action):
        if action == "resume":
            self.gameplay_scene.resume()

    def draw(self):
        self.resume_button.draw()
        wrapper.drawText("Paused", (30, 113, 68), 29, "Courier", 600, 300)

    def update(self):
        self.resume_button.update()
