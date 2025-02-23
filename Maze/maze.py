import time
from window import Window
from .cell import Cell
import random


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
        initial_seed=0
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
        random.seed(initial_seed)

    def _create_cells(self):
        for _ in range(self._num_cols):
            col_cells = []
            for _ in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)

        for col in range(self._num_cols):
            for row in range(self._num_rows):
                self._draw_cell(col, row)

    def _draw_cell(self, col: int, row: int):
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

    def get_list_cells_to_visit(self, col, row):
        valid_cells_indexes = []
        for i in range(-1, 2, 2):
            if self.__is_valid_cell(col, row + i):
                valid_cells_indexes.append((col, row + i))
            if self.__is_valid_cell(col + i, row):
                valid_cells_indexes.append((col + i, row))
        return valid_cells_indexes

    def __is_valid_cell(self, col: int, row: int) -> bool:
        if col < 0 or row < 0 or col >= self._num_cols or row >= self._num_rows:
            return False

        current: Cell = self._cells[col][row]
        if current.is_visited:
            return False
        return True

    def _break_walls_r(self, col: int, row: int) -> None:
        # Mark the current cell as visited
        current_cell: Cell = self._cells[col][row]
        current_cell.is_visited = True
        while True:
            # Create a list of cells to visit
            to_visit = self.get_list_cells_to_visit(col, row)

            if len(to_visit) == 0:
                self._draw_cell(col, row)
                return
            else:
                coords: tuple = random.choice(to_visit)
                next_cell: Cell = self._cells[coords[0]][coords[1]]

                current_col = col
                current_row = row
                next_col = coords[0]
                next_row = coords[1]

                if next_col - current_col == 1:
                    # Moving Right
                    current_cell.has_right_wall = False
                    next_cell.has_left_wall = False

                elif next_col - current_col == -1:
                    # Moving Left
                    current_cell.has_left_wall = False
                    next_cell.has_right_wall = False

                elif next_row - current_row == 1:
                    # Moving Down
                    current_cell.has_bottom_wall = False
                    next_cell.has_top_wall = False

                elif next_row - current_row == -1:
                    # Moving up
                    current_cell.has_top_wall = False
                    next_cell.has_bottom_wall = False

                else:
                    raise ValueError("Invalid movement in the maze")

                self._break_walls_r(next_col, next_row)

    def _reset_cells_visited(self):
        for col in range(self._num_cols):
            for row in range(self._num_rows):
                (self._cells[col][row]).is_visited = False

    def has_direct_path(self, current_col, current_row, next_col, next_row) -> bool:
        current_cell: Cell = self._cells[current_col][current_row]
        next_cell: Cell = self._cells[next_col][next_row]

        if next_col - current_col == 1:
            # Moving Right
            if not (current_cell.has_right_wall or next_cell.has_left_wall):
                return True
            return False
        elif next_col - current_col == -1:
            # Moving Left
            if not (current_cell.has_left_wall or next_cell.has_right_wall):
                return True
            return False
        elif next_row - current_row == 1:
            # Moving Down
            if not (current_cell.has_bottom_wall or next_cell.has_top_wall):
                return True
            return False

        elif next_row - current_row == -1:
            # Moving up
            if not (current_cell.has_top_wall or next_cell.has_bottom_wall):
                return True
            return False
        else:
            raise ValueError("Invalid movement in the maze")

    def solve(self) -> bool:
        return self.solve_r(0, 0)

    def solve_r(self, col, row) -> bool:
        self._animate()
        current_cell: Cell = self._cells[col][row]
        current_cell.is_visited = True

        exit_cell: Cell = self._cells[self._num_cols -
                                      1][self._num_rows - 1]

        if current_cell is exit_cell:
            return True

        to_visit = self.get_list_cells_to_visit(col, row)
        if len(to_visit) == 0:
            self._draw_cell(col, row)
            return False

        for coords in to_visit:
            next_cell: Cell = self._cells[coords[0]][coords[1]]
            current_col = col
            current_row = row
            next_col = coords[0]
            next_row = coords[1]

            if self.has_direct_path(current_col, current_row, next_col, next_row):
                current_cell.draw_move(next_cell)
                if self.solve_r(next_col, next_row):
                    return True
                else:
                    current_cell.draw_move(next_cell, undo=True)

        return False
