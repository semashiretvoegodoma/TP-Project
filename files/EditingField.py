import wrapper


class EditingField:
    def __init__(self):
        self.rects = []
        self.grid_on = True
        self.XYWH = (310, 130, 700, 500)
        self.grid_cell_size = 25
        self.grid_size = (self.XYWH[2] // self.grid_cell_size, self.XYWH[3] // self.grid_cell_size)
        self.is_creating_rect = False
        self.current_rectXY = (0, 0)

    def toggle_grid(self):
        self.grid_on = not self.grid_on

    def start_rect(self, x, y):
        """x and y are relative to field left top corner"""
        self.is_creating_rect = True
        self.current_rectXY = (x, y)

    def abandon_rect(self):
        self.is_creating_rect = False

    def finish_rect(self, x, y):
        """x and y are relative to field left top corner"""
        if not self.is_creating_rect:
            return
        self.is_creating_rect = False
        w = x - self.current_rectXY[0]
        h = y - self.current_rectXY[1]
        if w == 0 or h == 0:
            return
        self.rects.append(self.to_drawable((self.current_rectXY[0], self.current_rectXY[1], w, h)))

    def snap_to_grid(self, x, y):
        """x and y relative to top left corner of field"""
        x1 = self.grid_cell_size * round(x / self.grid_cell_size)
        y1 = self.grid_cell_size * round(y / self.grid_cell_size)
        return x1, y1

    def to_drawable(self, rectXYWH):
        w = rectXYWH[2]
        h = rectXYWH[3]
        if w < 0 and h < 0:
            return rectXYWH[0] + w, rectXYWH[1] + h, -w, -h
        elif w < 0:
            return rectXYWH[0] + w, rectXYWH[1], -w, h
        elif h < 0:
            return rectXYWH[0], rectXYWH[1] + h, w, -h
        else:
            return rectXYWH[0], rectXYWH[1], w, h

    def del_all_containing(self, x, y):
        """x and y relative to top left corner of field"""
        i = 0
        while i < len(self.rects):
            if wrapper.dotInRect(*(self.rects[i]), x, y):
                del self.rects[i]
            i += 1

    def update(self):
        if not wrapper.mouseInButton(*self.XYWH):
            self.abandon_rect()
            return
        pos = wrapper.mouse_pos()
        x = pos[0] - self.XYWH[0]
        y = pos[1] - self.XYWH[1]
        if wrapper.rmb_just_got_down:
            self.del_all_containing(x, y)
        if self.grid_on:
            snapped = self.snap_to_grid(x, y)
            x = snapped[0]
            y = snapped[1]
        if wrapper.mouse_just_got_down:
            self.start_rect(x, y)
        if not wrapper.mouse_down:
            self.finish_rect(x, y)

    def draw_borders(self):
        wrapper.drawRect((0, 0, 0), (self.XYWH[0], self.XYWH[1], 2, self.XYWH[3]))
        wrapper.drawRect((0, 0, 0), (self.XYWH[0], self.XYWH[1], self.XYWH[2], 2))
        wrapper.drawRect((0, 0, 0), (self.XYWH[0], self.XYWH[1] + self.XYWH[3], self.XYWH[2], 2))
        wrapper.drawRect((0, 0, 0), (self.XYWH[0] + self.XYWH[2], self.XYWH[1], 2, self.XYWH[3]))

    def draw_grid(self):
        for i in range(1, self.grid_size[0]):
            x = self.XYWH[0] + i * self.grid_cell_size
            y = self.XYWH[1]
            wrapper.drawRect((100, 100, 100), (x, y, 2, self.XYWH[3]))
        for i in range(1, self.grid_size[1]):
            x = self.XYWH[0]
            y = self.XYWH[1] + i * self.grid_cell_size
            wrapper.drawRect((100, 100, 100), (x, y, self.XYWH[2], 2))

    def draw_rects(self):
        for rect in self.rects:
            drawable = (rect[0]+self.XYWH[0], rect[1]+self.XYWH[1], rect[2], rect[3])
            wrapper.drawRect((150, 20, 30), drawable)

    def draw_current_rect(self):
        if self.grid_on:
            snapped = self.snap_to_grid(wrapper.mouse_pos()[0] - self.XYWH[0],
                                        wrapper.mouse_pos()[1] - self.XYWH[1])
        else:
            snapped = (wrapper.mouse_pos()[0] - self.XYWH[0], wrapper.mouse_pos()[1] - self.XYWH[1])
        end_x = snapped[0]
        end_y = snapped[1]
        w = end_x - self.current_rectXY[0]
        h = end_y - self.current_rectXY[1]
        drawable_relative_rect = self.to_drawable((self.current_rectXY[0], self.current_rectXY[1], w, h))
        drawable_rect = tuple([sum(x) for x in zip(drawable_relative_rect, (self.XYWH[0], self.XYWH[1], 0, 0))])
        wrapper.drawRect((150, 20, 30), drawable_rect)

    def draw(self):
        self.draw_borders()
        if self.grid_on:
            self.draw_grid()
        self.draw_rects()
        if self.is_creating_rect:
            self.draw_current_rect()
