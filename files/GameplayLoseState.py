import wrapper


class GameplayLoseState:
    def __init__(self, gameplay_scene):
        self.gameplay_scene = gameplay_scene

    def draw(self):
        wrapper.loadImage("backgroundLose")
        wrapper.drawImage("backgroundLose", 0, 0, 1300, 700)

    def update(self):
        if wrapper.isMousePressed():
            self.gameplay_scene.retry()
