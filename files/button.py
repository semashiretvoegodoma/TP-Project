import wrapper


class Button(object):
    def __init__(self, x, y, width, height, text, action, activated_by_escape = False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.action = action
        self.actionReceivers = set()
        wrapper.add_sound("button")
        self.activated_by_escape = activated_by_escape

    def addActionReceiver(self, actionReceiver):
        self.actionReceivers.add(actionReceiver)

    def RemoveActionReciver(self, actionReceiver):
        self.actionReceivers.discard(actionReceiver)

    def sound(self):
        wrapper.play_sound("button")

    def update(self):
        if (wrapper.mouse_just_got_down and wrapper.mouseInButton(self.x, self.y, self.width, self.height)) or (self.activated_by_escape and wrapper.pressed_escape):
            for subscriber in self.actionReceivers:
                subscriber.on_button(self.action)
                self.sound()

    def draw(self):
        wrapper.drawRect((0, 0, 0), (self.x, self.y, self.width, self.height))
        wrapper.drawText(self.text, (255, 255, 255), 36, "Arial", self.x + 22, self.y + 14)
