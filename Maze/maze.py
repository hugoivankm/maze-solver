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
        win: 'Window',
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._cells = [[None for _ in range(num_cols)]
                       for _ in range(num_rows)]
        self._win = win
        self._create_cells()

    def _create_cells(self):
        for col in range(self._num_cols):
            for row in range(self._num_rows):
                self._cells[row][col] = Cell(self._win)
        
        for col in range(self._num_cols):
            for row in range(self._num_rows):
                self._draw_cell(col, row) 
        
    def _draw_cell(self, i, j):
        cell_x1: int = self._x1 + (i * self._cell_size_x)
        cell_y1: int = self._y1 + (j * self._cell_size_y)
        cell_x2: int = cell_x1 + self._cell_size_x
        cell_y2: int = cell_y1 + self._cell_size_y
        cell: Cell = (self._cells[j][i])
        cell.draw(cell_x1, cell_y1, cell_x2, cell_y2)
        self._animate()
    
    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)