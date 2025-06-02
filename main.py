from tkinter import *
from utils import *

grid_rows = 30
grid_columns = 30
cell_size = 20
current_source = (0, 0)
current_destination = (grid_rows-1, grid_columns-1)

heading_text = "Path Finding Visualizer"
grid = [[0]*grid_columns for i in range(grid_rows)]

grid[current_source[0]][current_source[1]] = 2
grid[current_destination[0]][current_destination[1]] = 3


def draw(event, grid_view, point_options):

    global current_source, current_destination

    i = event.x // cell_size
    j = event.y // cell_size
    x1 = i * cell_size
    y1 = j * cell_size
    x2 = x1 + cell_size
    y2 = y1 + cell_size

    if (i>=0 and j>=0 and i<grid_rows and j<grid_columns):
        current_option = point_options.get()
        if (current_option == "Wall" and grid[i][j] != 2 and grid[i][j] != 3):
            grid[i][j] = 1
            grid_view.create_rectangle(x1, y1, x2, y2, fill="black", outline="black")
        elif (current_option == "Free Space" and grid[i][j] != 2 and grid[i][j] != 3):
            grid[i][j] = 0
            grid_view.create_rectangle(x1, y1, x2, y2, fill="white", outline="black")
        elif (current_option == "Source" and grid[i][j] != 3):
            grid[current_source[0]][current_source[1]] = 0
            grid_view.create_rectangle(current_source[0]*cell_size, current_source[1]*cell_size, current_source[0]*cell_size+cell_size, current_source[1]*cell_size+cell_size, fill="white", outline="black")
            grid[i][j] = 2
            grid_view.create_rectangle(x1, y1, x2, y2, fill="green", outline="black")
            current_source = (i, j)
        elif (current_option == "Destination" and grid[i][j] != 2):
            grid[current_destination[0]][current_destination[1]] = 0
            grid_view.create_rectangle(current_destination[0]*cell_size, current_destination[1]*cell_size, current_destination[0]*cell_size+cell_size, current_destination[1]*cell_size+cell_size, fill="white", outline="black")
            grid[i][j] = 3
            grid_view.create_rectangle(x1, y1, x2, y2, fill="blue", outline="black")
            current_destination = (i, j)
 

def create_grid(grid_view):
    for i in range(grid_rows):
        for j in range(grid_columns):
            x1 = cell_size*i
            y1 = cell_size*j
            x2 = x1+cell_size
            y2 = y1+cell_size
            color = getCellColor(grid, i, j)
            grid_view.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")


def main():


    """ ------------------------------------ Tkinter window variables --------------------------------- """
    root = Tk()

    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.geometry("+50+50")

    """ ------------------------------- Heading of the visualizer -------------------------------- """
    heading = Label(root, text=heading_text, height=2, font=("Courier", 20, "bold"))
    heading.grid(row=0, column=0, sticky="nsew")

    """ ---------------- Menu to choose which algorithm we are going to run ------------------- """
    menu_bar = Frame(root, height=5, background="green")
    menu_bar.grid(row=1, column=0)

    algorithm_options = StringVar()
    algorithm_options.set("DFS Search")

    algorithm_option_values = ["DFS Search", "BFS Search", "A* Search", "Best First Search"]

    algorithm_dropdown = OptionMenu(menu_bar, algorithm_options, *algorithm_option_values)
    algorithm_dropdown.grid(row=0, column=0, sticky="nsew")

    point_options = StringVar()
    point_options.set("Wall")

    point_option_values = ["Source", "Destination", "Free Space", "Wall"]

    point_dropdown = OptionMenu(menu_bar, point_options, *point_option_values)
    point_dropdown.grid(row=0, column=1, sticky="nsew")

    " -------------------------------------- Main Grid View --------------------------------------"""
    grid_view = Canvas(root, width=grid_columns*cell_size, height=grid_rows*cell_size)
    grid_view.grid(row=2, column=0, sticky="nsew")

    create_grid(grid_view)

    grid_view.bind("<Button-1>", lambda event: draw(event, grid_view, point_options))
    grid_view.bind("<B1-Motion>", lambda event: draw(event, grid_view, point_options))

    """ --------------------------------- Button container  ------------------------------------- """
    button_container = Frame(root, height=5)
    button_container.grid(row=3, column=0)

    start_button = Button(button_container, text="Start", width=10, bg="green", fg="white", font=("courier", 10, "bold"))
    start_button.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

    stop_button = Button(button_container, text="Reset", width=10, bg="blue", fg="white", font=("courier", 10, "bold"))
    stop_button.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

    root.mainloop()

if __name__=="__main__":
    main()