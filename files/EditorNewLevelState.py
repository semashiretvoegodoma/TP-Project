import os.path

import wrapper
import pathlib
from button import Button
from LineEdit import LineEdit

class EditorNewLevelState:
    def __init__(self, editor_scene):
        self.editor_scene = editor_scene
        self.create_button = Button(450, 600, 240, 92, "", "create")
        self.create_button.addActionReceiver(self)
        self.back_button = Button(10, 600, 220, 92, "", "back")
        self.back_button.addActionReceiver(self)
        self.line_edit = LineEdit((530, 288, 230, 80))

    def get_level_path(self):
        return str(pathlib.Path(__file__).parent.resolve()) + "/Levels/" + self.line_edit.text

    def on_button(self, action):
        if action == "create":
            if self.line_edit.text == "":
                return
            self.editor_scene.edit_state.set_opened_from("create")
            self.editor_scene.to_editing(self.get_level_path())
        elif action == "back":
            self.editor_scene.state = self.editor_scene.STATE_CHOOSE_VARIANT

    def update(self):
        self.create_button.update()
        self.back_button.update()
        self.line_edit.update()

    def draw(self):
        wrapper.loadImage("backgroundNewLevel")
        wrapper.drawImage("backgroundNewLevel", 0, 0, 1300, 700)
        wrapper.drawText("Name the level:", (0, 0, 0), 70, "Arial", 20, 285)
        self.line_edit.draw()
        level_name = self.line_edit.text
        path_to_level = self.get_level_path()
        wrapper.drawText("Level will be saved as " + path_to_level, (0, 0, 0), 20, "Arial", 20, 400)
        if level_name == "":
            status_text = "Status: give a name to level"
        else:
            if os.path.exists(path_to_level):
                status_text = "Status: the file will be OVERWRITTEN"
            else:
                status_text = "Status: the file doesn't exist, a new will be created"
        wrapper.drawText(status_text, (0, 0, 0), 50, "Arial Bold", 20, 210)
        wrapper.loadImage("buttonCreate")
        wrapper.drawImage("buttonCreate", 450, 600, 240, 92)
        wrapper.drawImage("buttonBack", 10, 600, 220, 92)
