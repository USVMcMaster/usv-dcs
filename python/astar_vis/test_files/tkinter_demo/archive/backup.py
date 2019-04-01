import tkinter as tk
from demo_settings import *

class UI(tk.Tk):

    def __init__(self):

        super().__init__()
        
        canvas = tk.Canvas(tk.TK, FRAME_WIDTH, FRAME_HEIGHT)
        canvas.pack()

        POS_X = (self.winfo_screenwidth() - FRAME_WIDTH)/2
        POS_Y = (self.winfo_screenheight() - FRAME_HEIGHT)/2

        self.geometry('%dx%d+%d+%d' % (FRAME_WIDTH, FRAME_HEIGHT, POS_X, POS_Y))
        self.title('Interactive Astar Demo')

        self.bind('<Button-1>', self.click)

        self.draw_grid()

    def gen_grid(self):
        grid = []
        for row in range(10):
            grid.append([])

            for coloumn in range(10):
                grid[row].append(0)

        grid[1][5] = 1

        for row in range(10):
            for column in range(10):
                colour = WHITE

                if grid[row][column] == 1:
                    color = GREEN

                    canvas.create_rectangle((MARGIN + GRID_WIDTH) * column + MARGIN,
                              (MARGIN + GRID_HEIGHT) * row + MARGIN,
                              GRID_WIDTH,
                              GRID_HEIGHT)




    def click(self, event):
        self.coords = event.x, event.y
        print(self.coords)

    def exit(self, event):

        if ord(event.char) == 27: #ESC char
            exit(0)

if __name__ == "__main__":
    


    UI().mainloop()





    # def center_window(width=WIDTH, height=HEIGHT):
    # # get screen width and height
    # screen_width = root.winfo_screenwidth()
    # screen_height = root.winfo_screenheight()

    # # calculate position x and y coordinates
    # x = (screen_width/2) - (width/2)
    # y = (screen_height/2) - (height/2)
    # root.geometry('%dx%d+%d+%d' % (width, height, x, y))





















# def create_grid(event=None):
#     w = c.winfo_width() # Get current width of canvas
#     h = c.winfo_height() # Get current height of canvas
#     c.delete('grid_line') # Will only remove the grid_line

#     # Creates all vertical lines at intevals of 100
#     for i in range(0, w, 100):
#         c.create_line([(i, 0), (i, h)], tag='grid_line')

#     # Creates all horizontal lines at intevals of 100
#     for i in range(0, h, 100):
#         c.create_line([(0, i), (w, i)], tag='grid_line')

# root = tk.Tk()

# c = tk.Canvas(root, height=1000, width=1000, bg='white')
# c.pack(fill=tk.BOTH, expand=True)

# c.bind('<Configure>', create_grid)
# root.mainloop()
