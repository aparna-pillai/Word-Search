from tkinter import *

class Sudoku(Frame):
    def __init__(self, master):
        """Initialize Frame."""
        super(Sudoku, self).__init__(master, background="orange2")
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        pass