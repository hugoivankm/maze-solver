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
        self._cells = [[None for _ in range(num_rows)]
                       for _ in range(num_cols)]
        
        self._win = win
        self._create_cells()

    def _create_cells(self):
        for row in range(self._num_rows):
            for col in range(self._num_cols):
                self._cells[col][row] = Cell(self._win)
        if self._win is None:
            return
        
        for col in range(self._num_cols):
            for row in range(self._num_rows):
                self._draw_cell(col, row) 
        
    def _draw_cell(self, i, j):
        
        cell_x1: int = self._x1 + (i * self._cell_size_x)
        cell_y1: int = self._y1 + (j * self._cell_size_y)
        cell_x2: int = cell_x1 + self._cell_size_x
        cell_y2: int = cell_y1 + self._cell_size_y
        cell: Cell = (self._cells[i][j])
        cell.draw(cell_x1, cell_y1, cell_x2, cell_y2)
        self._animate()
    
    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)