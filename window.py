from tkinter import Tk, BOTH, Canvas
from Geometry.Line import Line


class Window:
    def __init__(self, width: int, height: int):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg="white",
                               width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__is_running = False
         
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
       
    def wait_for_close(self):
        self.__is_running = True
        while self.__is_running:
            self.redraw()

    def close(self):
        self.__is_running = False
   
    def draw_line(self, line: Line, fill_color: str):
        line.draw(self.__canvas, fill_color)