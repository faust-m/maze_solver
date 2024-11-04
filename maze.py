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
        self.__x = x1
        self.__y = y1
        self.__cells = []
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.__create_cells()

    def __create_cells(self):
        pass