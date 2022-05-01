# UI element to fill in with text
import time
import wrapper


class LineEdit:
    def __init__(self, XYWH, color=(0, 0, 0), text_color=(255, 255, 255)):
        self.XYWH = XYWH
        self.color = color
        self.text_color = text_color
        self.text = ""
        self.last_update_time = time.time()
        self.time_between_letters = 0.2

    def update(self):
        if time.time() - self.last_update_time < self.time_between_letters:
            pass

        self.last_update_time = time.time()
        key = wrapper.last_key_pressed
        if key == "":
            return
        elif key == "backspace":
            if not self.text == "":
                self.text = self.text[:-1]
        elif key == "space":
            self.text += " "
        else:
            self.text += key

    def draw(self):
        wrapper.drawRect(self.color, self.XYWH)
        wrapper.drawText(self.text, self.text_color, 40, "Arial", self.XYWH[0], self.XYWH[1])
