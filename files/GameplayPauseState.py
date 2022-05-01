import wrapper
from button import Button


class GameplayPauseState:
    def __init__(self, gameplay_scene):
        self.gameplay_scene = gameplay_scene
        self.resume_button = Button(600, 400, 100, 50, "Resume", "resume", True)
        self.quit_button = Button(600, 500, 300, 50, "Quit to Levels", "quit")
        self.resume_button.addActionReceiver(self)
        self.quit_button.addActionReceiver(self)

    def on_button(self, action):
        if action == "resume":
            self.gameplay_scene.resume()
        elif action == "quit":
            self.gameplay_scene.to_levels()

    def draw(self):
        self.resume_button.draw()
        self.quit_button.draw()
        wrapper.drawText("Paused", (30, 113, 68), 29, "Courier", 600, 300)

    def update(self):
        self.resume_button.update()
        self.quit_button.update()
