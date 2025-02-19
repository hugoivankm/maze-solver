from Geometry.line import Line
from window import Window
from Geometry.point import Point


class Cell:
    def __init__(self, window: Window = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._window = window

    def draw(self, x1: int, y1: int, x2: int, y2: int) -> None:
        if self._window is None:
            return
        win = self._window

        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        top_wall = Line.create_line_from_coords(self._x1, self._y1,
                                                self._x2, self._y1)
        right_wall = Line.create_line_from_coords(self._x2, self._y1,
                                                  self._x2, self._y2)
        bottom_wall = Line.create_line_from_coords(self._x1, self._y2,
                                                   self._x2, self._y2)
        left_wall = Line.create_line_from_coords(self._x1, self._y1,
                                                 self._x1, self._y2)

        win.draw_line(
            top_wall, 'black'if self.has_top_wall else 'white')
        win.draw_line(
            right_wall, 'black' if self.has_right_wall else 'white')
        win.draw_line(
            bottom_wall, 'black' if self.has_bottom_wall else 'white')
        win.draw_line(
            left_wall, 'black' if self.has_left_wall else 'white')

    def draw_move(self, to_cell: 'Cell', undo=False):
        if self._window is None:
            return
        win = self._window

        fill_color = "gray" if undo else "red"

        center_x_a = abs(self._x1 + self._x2) // 2
        center_y_a = abs(self._y1 + self._y2) // 2
        point_a = Point(center_x_a, center_y_a)

        center_x_b = abs(to_cell._x1 + to_cell._x2) // 2
        center_y_b = abs(to_cell._y1 + to_cell._y2) // 2
        point_b = Point(center_x_b, center_y_b)

        mid_line = Line(point_a, point_b)
        win.draw_line(mid_line, fill_color=fill_color)
