import button
import wrapper


class GameplayWinState:
    def __init__(self, gameplay_scene):
        self.gameplay_scene = gameplay_scene
        self.continue_button = button.Button(600, 400, 100, 40, "Continue", "continue")
        self.continue_button.addActionReceiver(self)

    def on_button(self, action):
        if action == "continue":
            self.gameplay_scene.next_level()

    def draw(self):
        wrapper.drawText("Congrats!", (255, 150, 150), 40, "Arial", 600, 300)
        self.continue_button.draw()

    def update(self):
        self.continue_button.update()
