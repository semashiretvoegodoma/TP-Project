import json

from EditingField import EditingField
from button import Button
import wrapper


class EditorEditingState:
    def __init__(self, editor_scene):
        self.editor_scene = editor_scene
        self.opened_from = "create"
        self.filepath = ""
        self.editing_field = EditingField()
        self.save_button = Button(200, 30, 220, 92, "", "save")
        self.save_button.addActionReceiver(self)
        self.quit_button = Button(10, 600, 220, 92, "", "quit")
        self.quit_button.addActionReceiver(self)
        self.grid_button = Button(730, 30, 380, 92, "", "grid")
        self.grid_button.addActionReceiver(self)

    def set_path(self, filepath):
        self.filepath = filepath

    def set_opened_from(self, source: str):
        self.opened_from = source
        if source == "create":
            self.editing_field.rects = []

    def save_level(self):
        rects_as_lists = []
        for rect in self.editing_field.rects:
            offsetted_rect = (rect[0] + 300, rect[1], rect[2], rect[3])
            rects_as_lists.append(list(offsetted_rect))
        jsonable = {
            "game_version": "1",
            "bricks": rects_as_lists
        }
        open(self.filepath, "w").write(json.dumps(jsonable))

    def load_level(self):
        print("load for editing: " + self.filepath)
        self.editing_field.rects = []
        try:
            rects_as_lists = json.loads(open(self.filepath, "r").read())["bricks"]
            for rect_list in rects_as_lists:
                rect_list[0] -= 300
                self.editing_field.rects.append(tuple(rect_list))
        except FileNotFoundError:
            print("ERROR in EditorEditingState. Can't load level" + self.filepath + " for editing. File not found.")
        except PermissionError:
            print("ERROR in EditorEditingState. Permission to open level " + self.filepath + " for editing denied.")
        except json.JSONDecodeError as error:
            print("ERROR in EditorEditingState. Something is incorrect in " + self.filepath +
                  " because it can't be decoded. JSON message:")
            print(error.msg)

    def on_button(self, action):
        if action == "save":
            self.save_level()
        elif action == "grid":
            self.editing_field.toggle_grid()
        elif action == "quit":
            if self.opened_from == "load":
                self.editor_scene.state = self.editor_scene.STATE_LOAD
            else:
                self.editor_scene.state = self.editor_scene.STATE_CREATE

    def update(self):
        self.editing_field.update()
        self.save_button.update()
        self.grid_button.update()
        self.quit_button.update()

    def draw(self):
        wrapper.loadImage("background")
        wrapper.drawImage("background", 0, 0, 1300, 700)
        wrapper.loadImage("buttonBack")
        wrapper.drawImage("buttonBack", 10, 600, 220, 92)
        wrapper.loadImage("buttonSave")
        wrapper.drawImage("buttonSave", 200, 30, 220, 92)
        wrapper.loadImage("buttonToggleGrid")
        wrapper.drawImage("buttonToggleGrid", 730, 30, 380, 92)
        self.editing_field.draw()
