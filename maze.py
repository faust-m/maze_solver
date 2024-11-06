import time
import random
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
            win = None,
            seed = None
    ):
        self._x = x1
        self._y = y1
        self._cells = []
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._seed = None
        if seed:
            self._seed = random.seed(seed)
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
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _draw_cell(self, i, j):
        top_left_coord = Point(
            self._cell_size_x * j + self._x,
            self._cell_size_y * i + self._y
        )
        bottom_right_coord = Point(
            top_left_coord.x + self._cell_size_x,
            top_left_coord.y + self._cell_size_y
        )
        self._cells[i][j].draw(
            top_left_coord.x,
            top_left_coord.y,
            bottom_right_coord.x,
            bottom_right_coord.y
        )
        self._animate()

    def _animate(self):
        if not self._win:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(self._num_rows - 1, self._num_cols - 1)

    def _break_walls_r(self, i, j):
        current = self._cells[i][j]
        current.visited = True
        while True:
            to_visit = []
            if i - 1 >= 0 and not self._cells[i - 1][j].visited:
                to_visit.append((i - 1, j))
            if j - 1 >= 0 and not self._cells[i][j - 1].visited:
                to_visit.append((i, j - 1))
            if j + 1 < self._num_cols and not self._cells[i][j + 1].visited:
                to_visit.append((i, j + 1))
            if i + 1 < self._num_rows and not self._cells[i + 1][j].visited:
                to_visit.append((i + 1, j))
            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
            next_cell = to_visit[random.randrange(0, len(to_visit))]
            if next_cell[0] == i - 1:
                current.has_top_wall = False
                self._cells[i - 1][j].has_bottom_wall = False
            elif next_cell[0] == i + 1:
                current.has_bottom_wall = False
                self._cells[i + 1][j].has_top_wall = False
            elif next_cell[1] == j - 1:
                current.has_left_wall = False
                self._cells[i][j - 1].has_right_wall = False
            elif next_cell[1] == j + 1:
                current.has_right_wall = False
                self._cells[i][j + 1].has_left_wall = False
            self._break_walls_r(next_cell[0], next_cell[1])

    def _reset_cells_visited(self):
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._cells[i][j].visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        current = self._cells[i][j]
        current.visited = True
        if current is self._cells[-1][-1]:
            return True
        if (
            i - 1 >= 0 
            and not current.has_top_wall 
            and not self._cells[i - 1][j].visited
        ):
            current.draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            current.draw_move(self._cells[i - 1][j], True)
        if (
            i + 1 < len(self._cells) 
            and not current.has_bottom_wall 
            and not self._cells[i + 1][j].visited
        ):
            current.draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            current.draw_move(self._cells[i + 1][j], True)
        if (
            j - 1 >= 0 
            and not current.has_left_wall 
            and not self._cells[i][j - 1].visited
        ):
            current.draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            current.draw_move(self._cells[i][j - 1], True)
        if (
            j + 1 < len(self._cells[i]) 
            and not current.has_right_wall 
            and not self._cells[i][j + 1].visited
        ):
            current.draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            current.draw_move(self._cells[i][j + 1], True)
        return False
