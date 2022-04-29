from button import Button


class EditorChooseState:
    def __init__(self, editorScene):
        self.editorScene = editorScene
        self.create_button = Button(500, 300, 140, 40, "Create new level!", "create")
        self.create_button.addActionReceiver(self)
        self.load_button = Button(500, 400, 140, 40, "Load level", "load")
        self.load_button.addActionReceiver(self)
        self.back_button = Button(500, 500, 140, 40, "Back", "back")
        self.back_button.addActionReceiver(self)

    def update(self):
        self.create_button.update()
        self.load_button.update()
        self.back_button.update()

    def draw(self):
        self.create_button.draw()
        self.load_button.draw()
        self.back_button.draw()

    def to_create(self):
        self.editorScene.state = self.editorScene.STATE_CREATE

    def to_load(self):
        self.editorScene.state = self.editorScene.STATE_LOAD

    def to_menu(self):
        self.editorScene.to_menu()

    def on_button(self, action):
        if action == "create":
            self.to_create()
        elif action == "load":
            self.to_load()
