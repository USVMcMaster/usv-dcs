from tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, BOTTOM
from demo_settings import *

class UI(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent

        self.row, self.col = -1, -1

        self.__initUI()
    
    def __initUI(self):
        self.parent.title("Astar demo")
        self.pack(fill=BOTH)
        self.canvas = Canvas(self,
                            width=WIDTH,
                            height=HEIGHT)
        self.canvas.pack(fill=BOTH, side=BOTTOM)

        self.__draw_grid()

        self.canvas.bind("<Button-1>", self.__cell_clicked)

    def __draw_grid(self):

        print("draw")

        for i in range(AMOUNT):
            

        # for i in range(100):

        #     x0 = MARGIN + i * SIDE
        #     y0 = MARGIN
        #     x1 = MARGIN + i * SIDE
        #     y1 = HEIGHT - MARGIN


        #     self.canvas.create_rectangle(x0, y0, x1, y1, fill="green")

        #     x0 = MARGIN
        #     y0 = MARGIN + i * SIDE
        #     x1 = WIDTH - MARGIN
        #     y1 = MARGIN + i * SIDE
        #     self.canvas.create_rectangle(x0, y0, x1, y1, fill="black")

    # def __draw_cursor(self):
    #     self.canvas.delete("cursor")
    #     if self.row >= 0 and self.col >= 0:
    #         x0 = MARGIN + self.col * SIDE + 1
    #         y0 = MARGIN + self.row * SIDE + 1
    #         x1 = MARGIN + (self.col + 1) * SIDE - 1
    #         y1 = MARGIN + (self.row + 1) * SIDE - 1
    #         self.canvas.create_rectangle(x0, y0, x1, y1,outline="red", tags="cursor")

    def __cell_clicked(self, event):

        # Get mouse x,y coordinates
        x, y = event.x, event.y

        # Check if mouse is within grid object
        if (MARGIN < x < WIDTH - MARGIN and MARGIN < y < HEIGHT - MARGIN):
            self.canvas.focus_set()

            # Convert x,y to row,col
            row, col = (y - MARGIN) / CELL_SIZE, (x - MARGIN) / CELL_SIZE
            print("x:",x, "y:", y, "row:", round(row), "col:", round(col))

    def exit(self, event):

        if ord(event.char) == 27: #ESC char
            exit(0)

if __name__ == "__main__":
    
    root = Tk()
    UI(root)
    root.geometry("%dx%d" % (WIDTH, HEIGHT + 40))
    root.mainloop()
