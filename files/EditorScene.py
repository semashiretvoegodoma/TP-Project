import wrapper
from EditorEditingState import EditorEditingState
from EditorChooseState import EditorChooseState
from EditorLoadLevelState import EditorLoadLevelState
from EditorNewLevelState import EditorNewLevelState


class EditorScene:
    def __init__(self, currentScene):
        self.currentScene = currentScene
        self.STATE_CHOOSE_VARIANT = 0
        self.STATE_LOAD = 1
        self.STATE_CREATE = 2
        self.STATE_EDIT = 3
        self.state = self.STATE_CHOOSE_VARIANT
        self.choose_state = EditorChooseState(self)
        self.load_state = EditorLoadLevelState(self)
        self.create_state = EditorNewLevelState(self)
        self.edit_state = EditorEditingState(self)
        self.state_dict = {
            self.STATE_CHOOSE_VARIANT: self.choose_state,
            self.STATE_LOAD: self.load_state,
            self.STATE_CREATE: self.create_state,
            self.STATE_EDIT: self.edit_state
        }

    def to_menu(self):
        self.currentScene.state = self.currentScene.SCENE_MENU

    def to_editing(self, filepath):
        self.state = self.STATE_EDIT
        self.edit_state.set_path(filepath)

    def update(self):
        self.state_dict[self.state].update()

    def draw(self):
        wrapper.loadImage("backgroundEditor")
        wrapper.drawImage("backgroundEditor", 0, 0, 1300, 700)
        self.state_dict[self.state].draw()
