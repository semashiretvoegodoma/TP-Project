import wrapper


class Button(object):
    def __init__(self, x, y, width, height, text, action):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.action = action
        self.actionReceivers = set()

    def addActionReceiver(self, actionReceiver):
        self.actionReceivers.add(actionReceiver)

    def RemoveActionReciver(self, actionReceiver):
        self.actionReceivers.discard(actionReceiver)

    def update(self):
        if wrapper.mouse_down and wrapper.mouseInButton(self.x, self.y, self.width, self.height):
            for subscriber in self.actionReceivers:
                subscriber.onButton(self.action)

    def draw(self):
        wrapper.drawRect((150, 150, 150), (self.x, self.y, self.width, self.height))
        wrapper.drawText(self.text, (0, 0, 0), 36, "Arial", self.x, self.y)