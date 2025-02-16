from tkinter import Canvas
from .point import Point


class Line:
    def __init__(self, pointA: Point, pointB: Point):
        self.x1 = pointA.x
        self.y1 = pointA.y
        self.x2 = pointB.x
        self.y2 = pointB.y
        
    def draw(self, canvas: Canvas, fill_color: str) -> None:
        canvas.create_line(
            self.x1,
            self.y1,
            self.x2,
            self.y2,
            fill=fill_color,
            width=2
        )

    @staticmethod
    def create_line_from_coords(x1: int, y1: int, x2: int, y2: int) -> 'Line':
        return Line(Point(x1, y1), Point(x2, y2))
       
