import wrapper
from button import Button


class EditorChooseState:
    def __init__(self, editorScene):
        self.editorScene = editorScene
        self.create_button = Button(410, 300, 513, 100, "", "create")
        self.create_button.addActionReceiver(self)
        self.load_button = Button(500, 430, 420, 90, "", "load")
        self.load_button.addActionReceiver(self)
        self.back_button = Button(10, 600, 220, 92, "", "back")
        self.back_button.addActionReceiver(self)

    def update(self):
        self.create_button.update()
        self.load_button.update()
        self.back_button.update()

    def draw(self):
        wrapper.loadImage("buttonBack")
        wrapper.drawImage("buttonBack", 10, 600, 220, 92)
        wrapper.loadImage("buttonCreateNewLevel")
        wrapper.drawImage("buttonCreateNewLevel", 410, 300, 513, 100)
        wrapper.loadImage("buttonLoadLevel")
        wrapper.drawImage("buttonLoadLevel", 500, 430, 420, 90)

    def to_create(self):
        self.editorScene.state = self.editorScene.STATE_CREATE

    def to_load(self):
        self.editorScene.load_state.refresh_level_buttons()
        self.editorScene.state = self.editorScene.STATE_LOAD

    def to_menu(self):
        self.editorScene.to_menu()

    def on_button(self, action):
        if action == "create":
            self.to_create()
        elif action == "load":
            self.to_load()
        elif action == "back":
            self.to_menu()
