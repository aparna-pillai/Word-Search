from tkinter import *
import random


class Word_Search2(Frame):
    def __init__(self, master, text_file):
        """Initialize Frame."""
        self.text_file = text_file
        super(Word_Search2, self).__init__(master, background="orange2")
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        letter_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                       "T", "U", "V", "W", "X", "Y", "Z"]
        line_list = []
        for line in self.text_file:
            for char in line:
                if char == ".":
                    random_char = random.choice(letter_list)
