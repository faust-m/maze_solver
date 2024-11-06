import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_rows
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols
        )
    
    def test_maze_draw_cells_zero(self):
        num_cols = 3
        num_rows = 3
        m1 = Maze(0, 0, num_rows, num_cols, 100, 100)
        self.assertEqual(
            (m1._cells[0][0]._x1, m1._cells[0][0]._y1, m1._cells[0][0]._x2, m1._cells[0][0]._y2),
            (0, 0, 100, 100)
        )

    def test_maze_draw_cells_nonzero(self):
        num_cols = 3
        num_rows = 3
        m1 = Maze(10, 10, num_rows, num_cols, 100, 100)
        self.assertEqual(
            (m1._cells[1][1]._x1, m1._cells[1][1]._y1, m1._cells[1][1]._x2, m1._cells[1][1]._y2),
            (110, 110, 210, 210)
        )

    def test_maze_entrance_exit(self):
        num_cols = 3
        num_rows = 3
        m1 = Maze(10, 10, num_rows, num_cols, 100, 100)
        self.assertFalse(m1._cells[0][0].has_top_wall)
        self.assertFalse(m1._cells[-1][-1].has_bottom_wall)

    def test_maze_reset_cells_visited(self):
        num_cols = 2
        num_rows = 2
        m1 = Maze(10, 10, num_rows, num_cols, 100, 100)
        for i in range(len(m1._cells)):
            for j in range(len(m1._cells[i])):
                self.assertFalse(m1._cells[i][j].visited)



if __name__ == "__main__":
    unittest.main()