from maze import Maze
from window import Window

def main():
    win = Window(800, 600)
    maze = Maze(10, 10, 6, 7, 100, 100, win)
    win.wait_for_close()



if __name__ == "__main__":
    main()
