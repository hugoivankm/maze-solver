import time
from window import Window
from .cell import Cell


class Maze:
    def __init__(
        self,
        x1: int,
        y1: int,
        num_rows: int,
        num_cols: int,
        cell_size_x: int,
        cell_size_y: int,
        win: 'Window' = None,
    ):

        if num_cols < 1 or num_rows < 1:
            raise ValueError("number of rows and number of colors \
                              must be greater or equal to 1")

        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._cells = []
        self._win = win
        self._create_cells()

    def _create_cells(self):
        for _ in range(self._num_cols):
            col_cells = []
            for _ in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)

        for col in range(self._num_cols):
            for row in range(self._num_rows):
                self._draw_cell(col, row)

    def _draw_cell(self, col, row):
        if self._win is None:
            return
        
        cell_x1: int = self._x1 + (col * self._cell_size_x)
        cell_y1: int = self._y1 + (row * self._cell_size_y)
        cell_x2: int = cell_x1 + self._cell_size_x
        cell_y2: int = cell_y1 + self._cell_size_y
        cell: Cell = self._cells[col][row]
        cell.draw(cell_x1, cell_y1, cell_x2, cell_y2)
        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        top_left: Cell = self._cells[0][0]
        top_left.has_top_wall = False
        self._draw_cell(0, 0)

        bottom_right: Cell = self._cells[self._num_cols -
                                         1][self._num_rows - 1]
        bottom_right.has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)
