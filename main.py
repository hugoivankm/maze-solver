from window import Window
from Maze.cell import Cell


def main():
    win = Window(800, 600)
    
    cellA = Cell(200, 200, 240, 240)
    cellA.draw(win, "blue")
    
    cellB = Cell(40, 40, 80, 80)
    cellB.has_left_wall = False
    cellB.draw(win, "red")
    
    cellC = Cell(80, 80, 120, 120)
    cellC.has_right_wall = False
    cellC.draw(win, "black")
    
    cellD = Cell(120, 120, 160, 160)
    cellD.has_bottom_wall = False
    cellD.draw(win, "green")
    
    cellE = Cell(160, 160, 200, 200)
    cellE.has_top_wall = False
    cellE.draw(win, "red")
    
    win.wait_for_close()


main()