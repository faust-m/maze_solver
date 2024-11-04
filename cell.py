from line import Line, Point

class Cell:
    def __init__(
            self,
            window, 
            top_left_coord,
            bottom_right_coord,
            left_wall=True,
            right_wall=True,
            top_wall=True,
            bottom_wall=True
    ):
        self.__win = window
        self.__x1 = top_left_coord.x
        self.__y1 = top_left_coord.y
        self.__x2 = bottom_right_coord.x
        self.__y2 = bottom_right_coord.y
        self.center = Point(
            self.__x1 + abs(self.__x2 - self.__x1) / 2,
            self.__y2 - abs(self.__y2 - self.__y1) / 2
        )
        self.has_left_wall = left_wall
        self.has_right_wall = right_wall
        self.has_top_wall = top_wall
        self.has_bottom_wall = bottom_wall

    def draw(self, fill_color="black"):
        if self.has_left_wall:
            self.__win.draw_line(
                Line(
                    Point(self.__x1, self.__y1),
                    Point(self.__x1, self.__y2)
                ),
                fill_color
            )
        if self.has_right_wall:
            self.__win.draw_line(
                Line(
                    Point(self.__x2, self.__y2),
                    Point(self.__x2, self.__y1)
                ),
                fill_color
            )
        if self.has_top_wall:
            self.__win.draw_line(
                Line(
                    Point(self.__x1, self.__y1),
                    Point(self.__x2, self.__y1)
                ),
                fill_color
            )
        if self.has_bottom_wall:
            self.__win.draw_line(
                Line(
                    Point(self.__x2, self.__y2),
                    Point(self.__x1, self.__y2)
                ),
                fill_color
            )

    def draw_move(self, to_cell, undo=False):
        if undo:
            self.__win.draw_line(Line(self.center, to_cell.center), "gray")
        else:
            self.__win.draw_line(Line(self.center, to_cell.center), "red")

