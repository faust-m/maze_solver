from geometry import Line, Point

class Cell:
    def __init__(self, window = None):
        self._win = window
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        if not self._win:
            return
        left_wall = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
        right_wall = Line(Point(self._x2, self._y2), Point(self._x2, self._y1))
        top_wall = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
        bottom_wall = Line(Point(self._x2, self._y2), Point(self._x1, self._y2))
        left_wall_color = right_wall_color = top_wall_color = bottom_wall_color = "black"
        if not self.has_left_wall:
            left_wall_color = "white"
        if not self.has_right_wall:
            right_wall_color = "white"
        if not self.has_top_wall:
            top_wall_color = "white"
        if not self.has_bottom_wall:
            bottom_wall_color = "white"
        self._win.draw_line(left_wall, left_wall_color)
        self._win.draw_line(right_wall, right_wall_color)
        self._win.draw_line(top_wall, top_wall_color)
        self._win.draw_line(bottom_wall, bottom_wall_color)

    def draw_move(self, to_cell, undo=False):
        if not self._win:
            return
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
