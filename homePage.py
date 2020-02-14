from tkinter import *


class Home_page(Frame):
    def __init__(self, master, instructions, word_search, sudoku, crossword):
        """Initialize Frame."""
        self.instructions = instructions
        self.word_search = word_search
        self.sudoku = sudoku
        self.crossword = crossword
        super(Home_page, self).__init__(master, background="coral")
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self, text="", bg="coral"
              ).grid(row=0, column=0, sticky=N)

        Label(self, text="Phoenix Puzzles", font="Courier 40 bold", bg="coral",
              fg="Gold").grid(row=0, column=1, sticky=N)

        Label(self, text="", bg="coral",
              ).grid(row=0, column=2, sticky=N)

        Label(self,
              text="Fun Brain Games", font="Courier 30 bold", bg="coral",
              fg="firebrick3").grid(row=1, column=1, sticky=N)

        Label(self,
              text="Can you solve them all?", font="Courier 20 italic", bg="coral",
              fg="firebrick3").grid(row=2, column=1, sticky=N)

        Label(self, text="", bg="coral",
              ).grid(row=3, column=2, sticky=N)

        Button(self, text="Instructions", bg="maroon", fg="Light Gray",
               font="Courier 25", bd=5, command=self.instructions
               ).grid(row=4, column=1, sticky=N)

        Label(self, text="", bg="coral",
              ).grid(row=5, column=2, sticky=N)

        Button(self, text="Word Search", bg="maroon", fg="Light Gray",
               font="Courier 25", bd=5, command=self.wordSearch
               ).grid(row=6, column=1, sticky=N)

        Label(self, text="", bg="coral",
              ).grid(row=7, column=2, sticky=N)

        Button(self, text="Sudoku", bg="maroon", fg="Light Gray",
               font="Courier 25", bd=5, command=self.Sudoku
               ).grid(row=8, column=1, sticky=N)

        Label(self, text="", bg="coral",
              ).grid(row=9, column=2, sticky=N)

        Button(self, text="Crossword", bg="maroon", fg="Light Gray",
               font="Courier 25", bd=5, command=self.cross_word
               ).grid(row=10, column=1, sticky=N)

        Label(self, text="", bg="coral",
              ).grid(row=11, column=2, sticky=N)

    def instructions(self):
        self.instructions()

    def wordSearch(self):
        self.word_search()

    def Sudoku(self):
        self.sudoku()

    def cross_word(self):
        self.crossword()
