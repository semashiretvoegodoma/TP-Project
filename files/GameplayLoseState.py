import wrapper


class GameplayLoseState:
    def __init__(self, gameplay_scene):
        self.gameplay_scene = gameplay_scene

    def draw(self):
        wrapper.drawText("You lose :(", (0, 99, 85), 56, "Consolas", 400, 200)

    def update(self):
        if wrapper.isMousePressed():
            self.gameplay_scene.retry()
