from tkinter import *


class Home_page(Frame):
    def __init__(self, master, instructions, word_search):
        """Initialize Frame."""
        self.instructions = instructions
        self.word_search = word_search
        super(Home_page, self).__init__(master, background="orange2")
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self, text="", bg="orange2"
              ).grid(row=0, column=0, sticky=N)

        Label(self, text="Phoenix", font="Courier 40 bold", bg="orange2",
              fg="firebrick3").grid(row=0, column=1, sticky=N)

        Label(self, text="", bg="orange2",
              ).grid(row=0, column=2, sticky=N)

        Label(self,
              text="Word Search", font="Courier 30 bold", bg="orange2",
              fg="firebrick3").grid(row=1, column=1, sticky=N)

        Label(self,
              text="Can you solve them all?", font="Courier 20 italic", bg="orange2",
              fg="firebrick3").grid(row=2, column=1, sticky=N)

        Label(self, text="", bg="orange2",
              ).grid(row=3, column=2, sticky=N)

        Button(self, text="Instructions", bg="maroon", fg="Light Gray",
               font="Courier 25", bd=5, command=self.instructions
               ).grid(row=4, column=1, sticky=N)

        Label(self, text="", bg="orange2",
              ).grid(row=5, column=2, sticky=N)

        Button(self, text="Word Search", bg="maroon", fg="Light Gray",
               font="Courier 25", bd=5, command=self.wordSearch
               ).grid(row=6, column=1, sticky=N)

        Label(self, text="", bg="orange2",
              ).grid(row=7, column=2, sticky=N)

    def instructions(self):
        self.instructions()

    def wordSearch(self):
        self.word_search()
