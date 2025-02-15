from window import Window
from Geometry import Line


def main():
    win = Window(800, 600)
    lineA = Line.Line.create_line_from_coords(10, 10, 200, 200)
    lineB = Line.Line.create_line_from_coords(300, 300, 300, 500)
    lineC = Line.Line.create_line_from_coords(400, 25, 700, 25)
    
    win.draw_line(lineA, "black")
    win.draw_line(lineB, "red")
    win.draw_line(lineC, "blue")
    win.wait_for_close()


main()