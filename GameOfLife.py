# Conway's Game of Life
# Mike Gallant - 2017
# mgall15@lsu.edu

# Rules:
# Any live cell with fewer than two live neighbours dies,
#   as if caused by underpopulation.
# Any live cell with two or three live neighbours lives
#   on to the next generation.
# Any live cell with more than three live neighbours
#   dies, as if by overpopulation.
# Any dead cell with exactly three live neighbours becomes
#   a live cell, as if by reproduction.

import random
from tkinter import *


def toggle(cells):
    if cells['bg'] == "white":
        cells['bg'] = "black"
    else:
        cells['bg'] = "white"


class GameOfLife(Frame):
    def __init__(self, parent):
        super(GameOfLife, self).__init__()
        self.parent = parent
        self.parent.title("Conway's Game of Life")
        self.grid = Grid()
        self.build_ui()
        self.generate = False

    def build_ui(self):
        self.top_frame = Frame(self.parent).pack(side=TOP)

        self.set_dem = Button(self.top_frame, text="Start", command=self.start, height=1)
        self.set_dem.pack(side=LEFT)
        self.randomize = Button(self.top_frame, text="Randomize", command=self.rand_board, height=1)
        self.randomize.pack(side=LEFT)
        self.reset = Button(self.top_frame, text="Reset", command=self.reset_board, height=1)
        self.reset.pack(side=LEFT)

        self.build_board()

    def build_board(self):
        self.life_frame = Frame(self.parent, height=str(self.get_height()+2), width=str(self.get_width()+2))
        self.life_frame.pack(side=LEFT)

        self.cells = [[Button(self.life_frame, bg="white", width=2, height=1) for x in range(self.get_width() + 2)]
                             for y in range(self.get_height() + 2)]

        for y in range(1, self.get_height() + 1):
            for x in range(1, self.get_width() + 1):
                self.cells[y][x].grid(row=y, column=x, sticky=W+E)
                self.cells[y][x]['command'] = lambda i=y, j=x: toggle(self.cells[i][j])

    def get_height(self):
        return 25

    def get_width(self):
        return 40

    def start(self):
        self.generate = True
        self.simulate_life()

    def simulate_life(self):
        if self.empty_board():
            self.generate = False

        t = []
        for y in range(1, self.get_height()+1):
            for x in range(1, self.get_width()+1):
                if self.check_cell(y, x):
                    t.append(self.cells[y][x])

        for derp in t:
            toggle(derp)

        if self.generate:
            self.after(50, self.simulate_life)

    def check_cell(self, y, x):
        buddy_num = 0

        if self.cells[y + 1][x]['bg'] == "black":
            buddy_num += 1
        if self.cells[y - 1][x]['bg'] == "black":
            buddy_num += 1
        if self.cells[y][x + 1]['bg'] == "black":
            buddy_num += 1
        if self.cells[y][x - 1]['bg'] == "black":
            buddy_num += 1
        if self.cells[y - 1][x + 1]['bg'] == "black":
            buddy_num += 1
        if self.cells[y + 1][x + 1]['bg'] == "black":
            buddy_num += 1
        if self.cells[y + 1][x - 1]['bg'] == "black":
            buddy_num += 1
        if self.cells[y - 1][x - 1]['bg'] == "black":
            buddy_num += 1

        if self.cells[y][x]['bg'] == "black" and buddy_num < 2:
            return True
        elif self.cells[y][x]['bg'] == "black" and buddy_num > 3:
            return True
        elif self.cells[y][x]['bg'] == "white" and buddy_num == 3:
            return True
        else:
            return False

    def empty_board(self):
        for y in range(1, self.get_height()+1):
            for x in range(1, self.get_width()+1):
                if self.cells[y][x]['bg'] == "black":
                    return False
        return True

    def rand_board(self):
        self.reset_board()
        for y in range(1, self.get_height()+1):
            for x in range(1, self.get_width()+1):
                derp = random.randint(0, 100)
                if derp <= 20:
                    self.cells[y][x]['bg'] = "black"

    def reset_board(self):
        self.generate = False
        for y in range(1, self.get_height()+1):
            for x in range(1, self.get_width()+1):
                self.cells[y][x]['bg'] = "white"

if __name__ == "__main__":
    root = Tk()
    life = GameOfLife(root)
    root.mainloop()
