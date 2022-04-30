import os.path

import wrapper
import pathlib
from button import Button
from LineEdit import LineEdit


class EditorNewLevelState:
    def __init__(self, editor_scene):
        self.editor_scene = editor_scene
        self.create_button = Button(20, 550, 200, 40, "CREATE!", "create")
        self.create_button.addActionReceiver(self)
        self.back_button = Button(320, 550, 200, 40, "Back", "back")
        self.back_button.addActionReceiver(self)
        self.line_edit = LineEdit((320, 230, 200, 60))

    def get_level_path(self):
        return str(pathlib.Path(__file__).parent.resolve()) + "/Levels/" + self.line_edit.text

    def on_button(self, action):
        if action == "create":
            if self.line_edit.text == "":
                return
            self.editor_scene.to_editing(self.get_level_path())
        elif action == "back":
            self.editor_scene.state = self.editor_scene.STATE_CHOOSE_VARIANT

    def update(self):
        self.create_button.update()
        self.back_button.update()
        self.line_edit.update()

    def draw(self):
        wrapper.drawText("BUILD NEW LEVEL", (0, 0, 0), 40, "Arial", 20, 30)
        wrapper.drawText("Name the level:", (0, 0, 0), 20, "Arial", 20, 230)
        self.line_edit.draw()
        level_name = self.line_edit.text
        path_to_level = self.get_level_path()
        wrapper.drawText("Level will be saved as " + path_to_level, (0, 0, 0), 20, "Arial", 20, 330)
        if level_name == "":
            status_text = "Give a name to level"
        else:
            if os.path.exists(path_to_level):
                status_text = "The file will be OVERWRITTEN"
            else:
                status_text = "The file doesn't exist, a new will be created"
        wrapper.drawText(status_text, (0, 0, 0), 20, "Arial", 20, 380)
        # wrapper.drawText("SELECT VERSION", (0, 0, 0), 20, "Arial", 20, 430)
        self.create_button.draw()
        self.back_button.draw()

