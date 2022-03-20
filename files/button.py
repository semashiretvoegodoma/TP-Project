from wrapper import drawRect
from wrapper import drawText


class Button(object):
    def __init__(self, x, y, width, height, text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.actionRecievers = {}

    def addActionReceiver(self, actionReceiver):
        self.actionReceivers.add(actionReceiver)

    def RemoveActionReciver(self, actionReceiver):
        self.actionReceivers.discard(actionReceiver)

    def update(self):
        raise NotImplementedError

    def draw(self):
        drawRect((150, 150, 150), (self.x, self.y, self.width. self.height))
        drawText(self.text, (0, 0, 0), self.x, self.y)