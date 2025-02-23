from window import Window
from Maze.maze import Maze
import time


def main():
    num_rows = 10
    num_cols = 12
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) // num_cols
    cell_size_y = (screen_y - 2 * margin) // num_rows
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols,
                cell_size_x, cell_size_y, win, initial_seed=time.time())
    maze._break_entrance_and_exit()
    maze._break_walls_r(0, 0)
    maze._reset_cells_visited()
    maze.solve()

    win.wait_for_close()


if __name__ == "__main__":
    main()
