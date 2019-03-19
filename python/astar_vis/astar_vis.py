from p5 import *
import numpy as np

grid = np.array([[-1]*16 for n in range(16)]) # list comprehension

grid[0,0] = 1
grid[15,15] = 1

w = 50 # width of each cell

def setup():
    size(800,600)
    
def draw():    
    x,y = 0,0 # starting position

    for row in grid:
        for col in row:
          if col == 1:
              fill(250,0,0)
          else:
              fill(255)
          rect((x, y), w, w)
          x = x + w  # move right
        y = y + w # move down
        x = 0 # rest to left edge
              
        
def mouse_pressed(event):
    grid[event.y//w,event.x//w] = -1 * grid[event.y//w,event.x//w]  
    print(grid)
    # integer division is good here!

# def mouse_dragged(event):
	# grid[event.y//w,event.x//w] = -1 * grid[event.y//w,event.x//w]  

run()