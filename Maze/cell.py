from Geometry.Line import Line
from window import Window


class Cell:
    def __init__(self, x1: int, y1: int, x2: int, y2: int):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

    def draw(self, window: Window, fill_color: str):

        if self.has_top_wall:
            top_wall = Line.create_line_from_coords(self._x1, self._y1,
                                                    self._x2, self._y1)
            window.draw_line(top_wall, fill_color=fill_color)
        if self.has_right_wall:
            right_wall = Line.create_line_from_coords(self._x2, self._y1,
                                                      self._x2, self._y2)
            window.draw_line(right_wall, fill_color=fill_color)
        if self.has_bottom_wall:
            bottom_wall = Line.create_line_from_coords(self._x1, self._y2,
                                                       self._x2, self._y2)
            window.draw_line(bottom_wall, fill_color=fill_color)
        if self.has_left_wall:
            left_wall = Line.create_line_from_coords(self._x1, self._y1,
                                                     self._x1, self._y2)
            window.draw_line(left_wall, fill_color=fill_color)
