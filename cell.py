from geometry import Line, Point

class Cell:
    def __init__(self, window):
        self._win = window
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(self._x2, self._y2), Point(self._x2, self._y1))
            self._win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(self._x2, self._y2), Point(self._x1, self._y2))
            self._win.draw_line(line)

    def draw_move(self, to_cell, undo=False):
        if undo:
            color = "gray"
        else:
            color = "red"
        my_center = Point(
            self._x1 + abs(self._x2 - self._x1) / 2,
            self._y2 - abs(self._y2 - self._y1) / 2
        )
        other_center = Point(
            to_cell._x1 + abs(to_cell._x2 - to_cell._x1) / 2,
            to_cell._y2 - abs(to_cell._y2 - to_cell._y1) / 2
        )
        line = Line(my_center, other_center)
        self._win.draw_line(line, color)
