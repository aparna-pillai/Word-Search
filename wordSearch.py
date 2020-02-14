from tkinter import *


class Word_Search(Frame):
    def __init__(self, master, next_screen):
        """Initialize Frame."""
        self.next_screen = next_screen
        super(Word_Search, self).__init__(master, background="black")
        self.grid()
        self.choosing_widgets()

    def choosing_widgets(self):
        Label(self, text="Choose your level!", bg="black", font="Courier 25", fg="red").grid(row=1, column=0, sticky=W)

        Label(self, text="Easy: wordsearch_level1.txt", bg="black", font="Courier 18", fg="orangered"
              ).grid(row=2, column=0, columnspan=100, sticky=W)

        Label(self, text="Medium: wordsearch_level2.txt", bg="black", font="Courier 18", fg="tomato"
              ).grid(row=3, column=0, columnspan=100, sticky=W)

        Label(self, text="Hard: wordsearch_level3.txt", bg="black", font="Courier 18", fg="orange"
              ).grid(row=4, column=0, columnspan=100, sticky=W)

        Label(self, text="", bg="black", font="Courier 15"
              ).grid(row=5, column=0, sticky=W)

        Label(self, text="Load Cipher File:", bg="black", font="Courier 15", fg="gold"
              ).grid(row=6, column=0, sticky=W)

        self.file_ent = Entry(self, bg="black")
        self.file_ent.grid(row=7, column=0, sticky=W)

        self.load_file_bttn = Button(self, text="Load", command=self.load_file,
                                     font="Courier 15", bg="black", fg="yellow"
                                     ).grid(row=8, column=0, sticky=W)

    def load_file(self):
        file_name = self.file_ent.get()
        text_file = open(file_name, "r")
        self.next_screen(text_file)
