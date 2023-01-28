import tkinter as tk

class World:
    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=(cols*10), height=(rows*10))
        self.canvas.pack()
        self.sharks = []
        self.fishes = []

    def add_shark(self, shark):
        self.sharks.append(shark)

    def add_fish(self, fish):
        self.fishes.append(fish)

    def display_grid(self):
        self.root.update_idletasks()
        
    def is_empty(self, x, y):
        for fish in self.fishes:
             if fish.x == x and fish.y == y:
               return False
        for shark in self.sharks:
            if shark.x == x and shark.y == y:
                return False
        return True