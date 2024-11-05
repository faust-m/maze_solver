import time
from cell import Cell
from geometry import Point

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win
    ):
        self._x = x1
        self._y = y1
        self._cells = []
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._create_cells()

    def _create_cells(self):
        for i in range(self._num_rows):
            row = []
            for j in range(self._num_cols):
                row.append(Cell(self._win))
            self._cells.append(row)
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        top_left_coord = Point(
            self._cell_size_x * j + self._x,
            self._cell_size_y * i + self._y
        )
        bottom_right_coord = Point(
            top_left_coord.x + self._cell_size_x,
            top_left_coord.y + self._cell_size_y
        )
        self._cells[i][j].draw(top_left_coord.x, top_left_coord.y, bottom_right_coord.x, bottom_right_coord.y)
        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)