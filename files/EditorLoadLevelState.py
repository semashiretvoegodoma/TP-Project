import pathlib
import wrapper
from button import Button
from levelsScene import LevelsScene


class EditorLoadLevelState(LevelsScene):
    def __init__(self, editor_scene):
        self.editor_scene = editor_scene
        self.refresh_level_buttons()
        self.backButton = Button(100, 100, 100, 50, "Back", "menu")
        self.backButton.addActionReceiver(self)

    def to_menu(self):
        self.editor_scene.state = self.editor_scene.STATE_CHOOSE_VARIANT

    def to_path(self, level):
        return "Levels/" + level

    def to_gameplay(self, level):
        self.editor_scene.edit_state.set_opened_from("load")
        self.editor_scene.edit_state.set_path(self.to_path(level))
        self.editor_scene.edit_state.load_level()
        self.editor_scene.state = self.editor_scene.STATE_EDIT

    def draw(self):
        wrapper.drawText("BUILD NEW LEVEL", (0, 0, 0), 40, "Arial", 20, 530)
        wrapper.drawText("Choose one from the list", (0, 0, 0), 20, "Arial", 20, 630)
        LevelsScene.draw(self)
