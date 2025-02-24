import unittest

from Maze.maze import Maze
from Maze.cell import Cell


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_large(self):
        num_cols = 16
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_breaking_entrance_and_exit(self):
        num_rows = 12
        num_cols = 16
        m1: Maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        top_left: Cell = m1._cells[0][0]
        bottom_right: Cell = m1._cells[m1._num_cols - 1][m1._num_rows - 1]
        m1._break_entrance_and_exit()

        self.assertEqual(top_left.has_top_wall, False)
        self.assertEqual(
            bottom_right.has_bottom_wall,
            False
        )

    def test_reset_cells_visited(self):
        num_cols = 8
        num_rows = 10
        m1: Maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._break_entrance_and_exit()
        m1._break_walls_r(0, 0)
        m1._reset_cells_visited()

        any_visited = False
        for col in range(m1._num_cols):
            for row in range(m1._num_rows):
                if (m1._cells[col][row]).is_visited:
                    any_visited = True
        self.assertFalse(any_visited)


if __name__ == "__main__":
    unittest.main()
