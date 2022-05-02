import button
import wrapper


class GameplayWinState:
    def __init__(self, gameplay_scene):
        self.gameplay_scene = gameplay_scene
        self.continue_button = button.Button(650, 520, 400, 165, "", "continue")
        self.continue_button.addActionReceiver(self)

    def on_button(self, action):
        if action == "continue":
            self.gameplay_scene.next_level()

    def draw(self):
        wrapper.loadImage("backgroundWin")
        wrapper.drawImage("backgroundWin", 0, 0, 1300, 700)
        wrapper.loadImage("buttonNext")
        wrapper.drawImage("buttonNext", 650, 520, 400, 165)

    def update(self):
        self.continue_button.update()
