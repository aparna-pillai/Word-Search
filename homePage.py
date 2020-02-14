from tkinter import *
from PIL import Image, ImageTk, ImageFont, ImageDraw


class Home_page(Frame):
    def __init__(self, master, instructions, word_search, sudoku, crossword):
        """Initialize Frame."""
        self.instructions = instructions
        self.word_search = word_search
        self.sudoku = sudoku
        self.crossword = crossword
        super(Home_page, self).__init__(master, background="orange2")
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        imagePIL = Image.open("e1f11c68f493c36538593420538bf451.png")
        imageSmall = imagePIL.resize(600, 400)
        draw = ImageDraw.Draw(imageSmall)
        font = ImageFont.truetype("Courier bold", 40)
        draw.text((20, 50), "Phoenix Puzzles", "firebrick3", font=font)
        font = ImageFont.truetype(("Courier bold", 35))
        draw.text((50, 50), "Fun Brain Games", "firebrick 3", font=font)
        imageSmall.save("e1f11c68f493c36538593420538bf451.png")

        image1 = Image.open("e1f11c68f493c36538593420538bf451.png")
        photo = ImageTk.PhotoImage(image1)
        bgLbl = Label(Home_page, image=photo)
        bgLbl.place(x=0, y=0, relwidth=1, relheight=1)

        Label(self, text="", bg="orange2"
              ).grid(row=0, column=0, sticky=N)

        Label(self, text="Phoenix Puzzles", font="Courier 40 bold", bg="orange2",
              fg="firebrick3").grid(row=0, column=1, sticky=N)

        Label(self, text="", bg="orange2",
              ).grid(row=0, column=2, sticky=N)

        Label(self,
              text="Fun Brain Games", font="Courier 30 bold", bg="orange2",
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

        Button(self, text="Sudoku", bg="maroon", fg="Light Gray",
               font="Courier 25", bd=5, command=self.Sudoku
               ).grid(row=8, column=1, sticky=N)

        Label(self, text="", bg="orange2",
              ).grid(row=9, column=2, sticky=N)

        Button(self, text="Crossword", bg="maroon", fg="Light Gray",
               font="Courier 25", bd=5, command=self.cross_word
               ).grid(row=10, column=1, sticky=N)

        Label(self, text="", bg="orange2",
              ).grid(row=11, column=2, sticky=N)

    def instructions(self):
        self.instructions()

    def wordSearch(self):
        self.word_search()

    def Sudoku(self):
        self.sudoku()

    def cross_word(self):
        self.crossword()
