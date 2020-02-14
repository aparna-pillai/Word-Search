from tkinter import *


class Home_page(Frame):
    def __init__(self, master, word_search, sudoku, crossword):
        """Initialize Frame."""
        self.word_search = word_search
        self.sudoku = sudoku
        self.crossword = crossword
        super(Home_page, self).__init__(master, background="orange2")
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self, text="", bg="orange2"
              ).grid(row=0, column=0, sticky=N)

        Label(self, text="Brain Puzzles", font="Courier 40 bold", bg="orange2",
              fg="firebrick3").grid(row=0, column=1, sticky=N)

        Label(self, text="", bg="orange2",
              ).grid(row=0, column=2, sticky=N)

        Label(self,
              text="and Fun Games", font="Courier 30 bold", bg="orange2",
              fg="firebrick3").grid(row=1, column=1, sticky=N)

        Label(self,
              text="Can you solve them all?", font="Courier 20 italic", bg="orange2",
              fg="firebrick3").grid(row=2, column=1, sticky=N)

        Label(self, text="", bg="orange2",
              ).grid(row=4, column=2, sticky=N)

        Button(self, text="Word Search", bg="orange2", fg="black",
               font="Courier 25", bd=5, command=self.wordSearch
               ).grid(row=5, column=1, sticky=N)

        Label(self, text="", bg="orange2",
              ).grid(row=6, column=2, sticky=N)

        Button(self, text="Sudoku", bg="orange2", fg="black",
               font="Courier 25", bd=5, command=self.Sudoku
               ).grid(row=7, column=1, sticky=N)

        Label(self, text="", bg="orange2",
              ).grid(row=8, column=2, sticky=N)

        Button(self, text="Crossword", bg="orange2", fg="black",
               font="Courier 25", bd=5, command=self.cross_word
               ).grid(row=10, column=1, sticky=N)

        Label(self, text="", bg="orange2",
              ).grid(row=11, column=2, sticky=N)

    def wordSearch(self):
        self.word_search()

    def Sudoku(self):
        self.sudoku()

    def cross_word(self):
        self.crossword()
